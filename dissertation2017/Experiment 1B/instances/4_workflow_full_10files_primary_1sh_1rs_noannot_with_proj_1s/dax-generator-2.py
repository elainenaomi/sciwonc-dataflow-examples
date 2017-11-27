#!/usr/bin/env python


from Pegasus.DAX3 import *
import sys
import os
import json
import re
import ast
import collections
import pprint

##################################################
# for sorting alpha + num
##################################################

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


##################################################
# CONSTANTS
##################################################

PATH = os.path.dirname(os.path.realpath(__file__))
#PATH = os.getcwd()

PATTERN = "*"

##################################################
# INIT
##################################################


# Create a abstract dag
dax = ADAG("example_workflow")


with open(PATH + '/config.json') as configFile:
    configData = json.load(configFile)

    lastFilesIt = 0
    filesIt = 0
    files = []

    executablesIt = 0
    executables = []

    numTaskIt = 0

    for task in configData["tasks"]:

        #################################################
        # FILE
        #################################################

        # filter(function, iterable) is equivalent to [item for item in iterable if function(item)]
        dirnamesList = filter(os.path.isdir, os.listdir(PATH))
        dirnamesList.sort(key=numericalSort)

        taskDirList = [elem for elem in dirnamesList if elem.find(task['prefixFolder']) > -1]

        totalTasks = len(taskDirList)

        fileNamespace = {}

        if totalTasks > 0:

            if (task.has_key("fileInputPath")):

                if (task.has_key("fileInputPathLimit")):
                    limitFile =  task["fileInputPathLimit"]
                    countFileInput = 0
                else:
                    limitFile = None

                if (task.has_key("fileInputPathSkip")):
                    skipFile = task["fileInputPathSkip"]
                    countSkipInput = 0
                else:
                    skipFile = None


                addFile = True
                skipAddFile = False


                for (dirpath, dirnames, filenames) in os.walk(task["fileInputPath"]):

                    filenames.sort(key=numericalSort)

                    for filename in filenames:


                        if skipFile:

                            if countSkipInput < skipFile:
                                countSkipInput += 1
                                skipAddFile = True
                            else:
                                skipAddFile = False



                        if skipAddFile:
                            continue
                        else:

                            if limitFile:
                                if countFileInput < limitFile:
                                    addFile = True
                                    countFileInput += 1
                                else:
                                    addFile = False
                            else:
                                addFile = True

                            if addFile:
                                fileTask = []
                                fileTaskIt = 0

                                fileTask.append(File(filename))
                                fileTask[fileTaskIt].addPFN(PFN("file://"+ task["fileInputPath"] + filename, "local"))
                                dax.addFile(fileTask[fileTaskIt])

                                fileTaskIt += 1
                                fileNamespace[filename] = fileTask
                            else:
                                break;

            if (task.has_key("prefixConfig")):



                for dirname in taskDirList:

                    fileNamespace[dirname] = []

                    for (dirpath, dirnames, filenames) in os.walk(PATH +"/"+ dirname):

                        fileTask = []
                        fileTaskIt = 0

                        for config in filenames:

                            if (config.find(task["prefixConfig"], 0, len(task["prefixConfig"])) > -1):

                                fileTask.append(File(config))
                                fileTask[fileTaskIt].addPFN(PFN("file://"+ PATH +"/"+ dirname + "/" + config, "local"))
                                dax.addFile(fileTask[fileTaskIt])

                                fileTaskIt += 1

                        fileNamespace[dirname] = fileTask
                        
            if (task.has_key("fileInput")):

                for dirname in taskDirList:

                    if fileNamespace.has_key(dirname):
                        fileTask = fileNamespace[dirname]
                        fileTaskIt = len(fileTask)
                    else:
                        fileTask = []
                        fileTaskIt = 0

                    for (dirpath, dirnames, filenames) in os.walk(PATH +"/"+ dirname):
                        for fileInput in filenames:
                            for f in task["fileInput"]:

                                if (fileInput.find(f, 0, len(f)) > -1):

                                    fileTask.append(File(fileInput))
                                    fileTask[fileTaskIt].addPFN(PFN("file://"+ PATH +"/"+ dirname + "/" + fileInput, "local"))
                                    dax.addFile(fileTask[fileTaskIt])

                                    fileTaskIt += 1
                                    #print "\n"+fileInput


                    fileNamespace[dirname] = fileTask

                #pprint.pprint(fileNamespace)


            if fileNamespace:
                files.append(fileNamespace)
                filesIt += 1

        #################################################
        # EXECUTABLE
        #################################################

        execNamespace = {}

        if totalTasks > 0:

            if (task.has_key("prefixTask")):

                for dirname in taskDirList:
                    #print dirname

                    for (dirpath, dirnames, filenames) in os.walk(PATH +"/"+ dirname):

                        execTask = []
                        execTaskIt = 0

                        for execFile in filenames:


                            if (execFile.find(task["prefixTask"], 0, len(task["prefixTask"]) ) > -1):

                                execTask.append(Executable(namespace=configData["namespace"], name=dirname, version="1.0", \
                                os=configData["os"], arch=configData["arch"], installed=False))

                                execTask[execTaskIt].addPFN(PFN("file://"+ PATH +"/"+ dirname + "/" + execFile, "condorpool"))
                                dax.addExecutable(execTask[execTaskIt])

                                execTaskIt += 1

                    execNamespace[dirname] = execTask

            if len(execTask) > 0:
                executables.append(execNamespace)
                executablesIt += 1

        numTaskIt += 1


    #################################################
    #################################################
    #################################################
    # JOB
    #################################################

    jobsIt = 0
    jobs = []


    totalJobs = len(executables)

    if totalJobs > 0:

        for numTaskIt in range(0, totalJobs):

            exeKeylist = executables[numTaskIt].keys()
            exeKeylist.sort(key=numericalSort)

            jobTask = []
            jobTaskIt = 0

            for name in exeKeylist:

                jobTask.append(Job(namespace=configData["namespace"], name=name, version="1.0"))

                for fileInputIt in range(0,len(files[numTaskIt][name])):
                    jobTask[jobTaskIt].uses(files[numTaskIt][name][fileInputIt], link=Link.INPUT)

                    if (configData["tasks"][numTaskIt].has_key("fileInputPath")):

                        config = configData["tasks"][numTaskIt]["prefixConfig"]
                        filename = files[numTaskIt][name][fileInputIt]
                        filenameString = str(filename)
                        position = filenameString.find(config)

                        fileToSearch = PATH + "/" + name +"/" + filenameString[position:-1]

                        with open(fileToSearch, 'r') as f:
                            data = f.readlines()

                            for line in data:

                                if(line.find("FILENAME = ",0,11) > -1):
                                    # transforming in a list
                                    fileInputList = ast.literal_eval(line[11:-1])
                                    for fileInput in fileInputList:

                                        for fileInputItem in files[numTaskIt][fileInput]:
                                            jobTask[jobTaskIt].uses(fileInputItem, link=Link.INPUT)

                dax.addJob(jobTask[jobTaskIt])
                jobTaskIt += 1


            jobs.append(jobTask)
            jobsIt += 1

    #################################################
    # DEPENDENCY
    # dax.addDependency(Dependency(parent=hello, child=world)) hello is the var for the job hello
    #################################################

    #pprint.pprint(jobs)
    #pprint.pprint(executables)

    totalJobs = len(jobs)
    for j in range(1,totalJobs):
        #print j
        if configData["tasks"][j].has_key("dependency"):
            #print "\nTASK "+configData["tasks"][j]["taskName"]

            for x,i in enumerate(configData["tasks"]):
                #print "Task "+str(x)
                #print "Data Task" + str(i)+"\n"

                for dep in configData["tasks"][j]["dependency"]:
                    #print "Pref " + i["prefixFolder"]
                    #print "Dep "+dep


                    if i["prefixFolder"] == dep:
                        #print i["prefixFolder"]
                        children = jobs[j]
                        parents = jobs[x]
                        #pprint.pprint(parents)
                        #pprint.pprint(children)
                        for child in children:
                            for parent in parents:
                                dax.addDependency(Dependency(parent=parent, child=child))



# Write the DAX to stdout
dax.writeXML(sys.stdout)
