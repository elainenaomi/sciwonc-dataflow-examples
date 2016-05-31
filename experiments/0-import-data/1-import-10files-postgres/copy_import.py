#!/usr/bin/env python

# template
# copiar o original
# alterar os parametros
# alterar o nome dos configs dentro das atividades


# design pattern
# - template define a lista de comandos a serem executados
# BYFILE -> lista de arquivos e total de recursos (condor_q?)
# BYUNIT ->	descobre o total de registros e divide
# BYGROUP -> divide de acordo com uma lista
# BYSLIDINGWINDOW -> divide de X em X
# ALL -> nao divide


import os
import shutil
import json
from pprint import pprint

with open('import_filename.json') as dataFile:
	importData = json.load(dataFile)
	totalSlots = importData["totalSlots"]
	totalFilesInput = len(importData["files"])

print importData["configTaskName"];
print importData["taskName"];
print totalFilesInput


if(importData["typeOperation"] == "BY_FILE"):
	totalTasks = min (totalSlots, totalFilesInput)
	totalFileByTask = totalFilesInput / totalSlots
	totalAdditionalFile =  totalFilesInput % totalSlots

	print "\n BY_FILE"
	print totalTasks
	print totalFileByTask
	print totalAdditionalFile



	additionalFilePerTask = totalAdditionalFile / totalTasks
	remainderFilePerTask =  totalAdditionalFile % totalTasks
	print additionalFilePerTask
	print remainderFilePerTask


initialFile = 0

for x in range(0, totalTasks):

	directory = importData['prefixFolder']+str(x)

	if not os.path.exists(directory):
	    os.makedirs(directory)


	outputImport = []
	fileToSearch = importData["taskName"]

	with open(fileToSearch, 'r') as f:
		data = f.readlines()

	for line in data:
		newLine = line
		for config in importData["configTaskName"]:
			oldConfig = config.replace(".py","")
			newConfig = config.replace(".py","_"+str(x)) # without .py
			newLine = newLine.replace(oldConfig, newConfig)
		outputImport.append(newLine)


	newImportFile = fileToSearch.replace(".py","_"+str(x)+".py")
	fi = open(directory +"/"+newImportFile, "w")
	fi.writelines(outputImport)
	fi.close()


	for config in importData["configTaskName"]:

		if totalAdditionalFile > 0:

			if (remainderFilePerTask > 0):
				totalFiles = totalFileByTask + additionalFilePerTask + 1
				totalAdditionalFile = totalAdditionalFile - additionalFilePerTask - 1
				remainderFilePerTask = remainderFilePerTask - 1
			else:
				totalFiles = totalFileByTask + additionalFilePerTask
				totalAdditionalFile = totalAdditionalFile - additionalFilePerTask
		else:
			totalFiles = totalFileByTask

		outputConfig = []
		fileToSearch = config

		with open(fileToSearch, 'r') as f:
			data = f.readlines()


		for line in data:
			newLine = line
			# if filename, replace with my custom content
			# FILENAME = ["part-00000-of-00500.csv.gz"]

			if(newLine.find("FILENAME = ",0,11) > -1):
				newLine = "FILENAME = "+str(importData["files"][initialFile:(initialFile+totalFiles)]).replace('u','') + "\n"

			outputConfig.append(newLine)


		newImportFile = fileToSearch.replace(".py","_"+str(x)+".py")
		fi = open(directory +"/"+newImportFile, "w")
		fi.writelines(outputConfig)
		fi.close()

	initialFile += totalFiles
