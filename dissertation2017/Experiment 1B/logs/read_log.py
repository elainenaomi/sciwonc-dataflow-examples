# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import pprint
import datetime
# import statistics


# import numpy as np
# import scipy as sp
# import scipy.stats
# import math

def initWorkflowExecutionInfo(filename, stats_workflow_jobs):
    # f = filename.split("/")
    f = filename.split("\\")
    workflow = f[1]
    execution = f[2]

    if workflow not in stats_workflow_jobs:
        stats_workflow_jobs[workflow] = {}

    if execution not in stats_workflow_jobs[workflow]:
        stats_workflow_jobs[workflow][execution] = {}

    return workflow,execution


############################################################
# open job statistics file
############################################################
def getJobList(filename,stats_workflow_jobs):
    workflow,execution = initWorkflowExecutionInfo(filename, stats_workflow_jobs)

    with open(filename, 'r') as f:
        data = f.readlines()
        enableRead = False

        for line in data:
            if(line.find("Try Site",22,44) > -1):
                enableRead = True

            if enableRead == True:
                job_info = line.split()
                job = job_info[0]
                pool = job_info[2]
                time = job_info[3]
                resource = job_info[14]
                if pool == "condorpool":
                    stats_workflow_jobs[workflow][execution][job] = {}
                    stats_workflow_jobs[workflow][execution][job]["elapsed_time"] = time
                    stats_workflow_jobs[workflow][execution][job]["resource"] = resource

    return

############################################################
# open log file
############################################################
def getJobInfoLog(filename, workflow, execution, stats_workflow_jobs):
    YEAR = datetime.date.today().strftime("%Y")
    job_ids = []
    job_map_id = {}
    with open(filename, 'r') as f:
        last_line = None
        last_terminate_job_log_id = None
        enableTerminateStats = False

        for line in f:
            if line.find("DAG Node: ") > -1:
                job = line.split()[2]
                if job in stats_workflow_jobs[workflow][execution]:
                    info = last_line.split()
                    job_log_id = info[1]
                    date = info[2].split("/")
                    submit_time = YEAR +"-"+ date[0]+ "-"+ date[1] + " "+ info[3]
                    stats_workflow_jobs[workflow][execution][job]["job_log_id"] = job_log_id
                    stats_workflow_jobs[workflow][execution][job]["submit_time"] = submit_time
                    job_ids.append(job_log_id)

                    if job not in job_map_id:
                        job_map_id[job_log_id] = job

            # any(substring in string for substring in substring_list)
            elif any(substring in line for substring in job_ids):
                info = line.split()
                job_log_id = info[1]
                job = job_map_id[job_log_id]
                date = info[2].split("/")
                time = YEAR +"-"+ date[0]+ "-"+ date[1] + " "+ info[3]

                if info[5] == "terminated.":
                    stats_workflow_jobs[workflow][execution][job]["terminated_time"] = time
                    last_terminate_job_log_id = job_log_id
                    enableTerminateStats = True
                    count = 0
                elif info[5] == "executing":
                    stats_workflow_jobs[workflow][execution][job]["executing_time"] = time
                    stats_workflow_jobs[workflow][execution][job]["executing_host"] = info[8]

            elif enableTerminateStats == True:
                if count < 13:
                    # print line
                    job = job_map_id[last_terminate_job_log_id]

                    if line.find("Total Bytes Sent By Job") > -1:
                        bytes_sent = line.split()[0]
                        stats_workflow_jobs[workflow][execution][job]["total bytes sent"] = bytes_sent
                    if line.find("Total Bytes Received By Job") > -1:
                        bytes_rec = line.split()[0]
                        stats_workflow_jobs[workflow][execution][job]["total bytes received"] = bytes_rec
                    if line.find("Cpus") > -1:
                        cpus = line.split()
                        stats_workflow_jobs[workflow][execution][job]["cpu request"] = cpus[2]
                        stats_workflow_jobs[workflow][execution][job]["cpu allocated"] = cpus[3]
                    if line.find("Disk (KB)") > -1:
                        disk = line.split()
                        stats_workflow_jobs[workflow][execution][job]["disk(KB) usage"] = disk[3]
                        stats_workflow_jobs[workflow][execution][job]["disk(KB) request"] = disk[4]
                        stats_workflow_jobs[workflow][execution][job]["disk(KB) allocated"] = disk[5]
                    if line.find("Memory (MB)") > -1:
                        mem = line.split()
                        stats_workflow_jobs[workflow][execution][job]["memory(MB) usage"] = mem[3]
                        stats_workflow_jobs[workflow][execution][job]["memory(MB) request"] = mem[4]
                        stats_workflow_jobs[workflow][execution][job]["memory(MB) allocated"] = mem[5]

                    count += 1
                else:
                    enableTerminateStats = False
            last_line = line

    return
############################################################

PATH = "."
DIR_STATS = "statistics"
stats_workflow_jobs = {}
# {w10 : {job1: {...}}}

for path, subdirs, files in sorted(os.walk(PATH)):
    for filename in files:
        # searching for log file
        if ("example_workflow-0.log" in filename):
            log_filepath = os.path.join(path, filename)
            workflow,execution = initWorkflowExecutionInfo(log_filepath, stats_workflow_jobs)
            stats_workflow_jobs[workflow][execution]["logfile"] = log_filepath

        # searching for job file statistics
        if DIR_STATS in path:
            if ("jobs.txt" in filename):
                f = os.path.join(path, filename)
                getJobList(f,stats_workflow_jobs)

for workflow, executions in stats_workflow_jobs.iteritems():
    for execution, jobs in executions.iteritems():
        getJobInfoLog(jobs["logfile"], workflow, execution, stats_workflow_jobs)


# pprint.pprint(stats_workflow_jobs)
import json
with open('stats.json', 'w') as outfile:
    json.dump(stats_workflow_jobs, outfile, sort_keys = True, indent = 4)

csv_lines = []
for workflow, executions in stats_workflow_jobs.iteritems():
    for execution, jobs in executions.iteritems():
        print "\n\n" + execution+"\n"
        for job, data in jobs.iteritems():
            print job
            # print data
            if "logfile" not in job:
                dict_data = {}
                dict_data["workflow"] = workflow
                dict_data["execution"] = execution
                dict_data["job"] = job
                dict_data["elapsed_time"] = data["elapsed_time"]
                dict_data["resource"] = data['resource']
                dict_data["job_log_id"] = data['job_log_id']
                dict_data["submit_time"] = data['submit_time']
                dict_data["execution_time"] = data['executing_time']
                dict_data["executing_host"] = data['executing_host']
                dict_data["terminated_time"] = data['terminated_time']
                dict_data["total bytes sent"] = data['total bytes sent']
                dict_data["total bytes received"] = data['total bytes received']
                dict_data["cpu request"] = data['cpu request']
                dict_data["cpu allocated"] = data['cpu allocated']
                dict_data["disk(KB) usage"] = data['disk(KB) usage']
                dict_data["disk(KB) request"] = data['disk(KB) request']
                dict_data["disk(KB) allocated"] = data['disk(KB) allocated']
                dict_data["memory(MB) usage"] = data['memory(MB) usage']
                dict_data["memory(MB) request"] = data['memory(MB) request']
                dict_data["memory(MB) allocated"] = data['memory(MB) allocated']

                csv_lines.append(dict_data)

import csv

with open('stats.csv', 'w') as csvfile:
    fieldnames = ["workflow", "execution", "job", "elapsed_time", "resource", "job_log_id", "submit_time", "execution_time", "executing_host", "terminated_time", "total bytes sent", "total bytes received", "cpu request", "cpu allocated", "disk(KB) usage", "disk(KB) request", "disk(KB) allocated", "memory(MB) usage", "memory(MB) request", "memory(MB) allocated"]

    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')

    # writer.writeheader()
    for line in csv_lines:
        writer.writerow(line)
