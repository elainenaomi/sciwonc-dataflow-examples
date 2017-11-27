#!/usr/bin/env python
"""
This activity will calculate the ratio between CPU request and Memory request by (job ID, task index, event type).
These fields are optional and could be null.
"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import math
import sys

##################################################################
import ConfigDB_Calc_StatsCPUMemory_0
client_statscpumemory = DataStoreClient("postgres", ConfigDB_Calc_StatsCPUMemory_0)
data_statscpumemory = client_statscpumemory.getData()

if data_statscpumemory:
    while True:
        doc = data_statscpumemory.next()
        if doc is None:
            break;

        sd_cpu = float(doc['standard deviation cpu']) if doc['standard deviation cpu'] else None
        avg_cpu = float(doc['average cpu']) if doc['average cpu'] else None
        sd_memory = float(doc['standard deviation memory']) if doc['standard deviation memory'] else None
        avg_memory = float(doc['average memory']) if doc['average memory'] else None
        sd_ratio = float(doc['standard deviation ratio']) if doc['standard deviation ratio'] else None
        avg_ratio = float(doc['average ratio']) if doc['average ratio'] else None

##################################################################
import ConfigDB_Calc_TEInfo_0
client_taskinfo = DataStoreClient("postgres", ConfigDB_Calc_TEInfo_0)

# according to config
eventList = client_taskinfo.getData() # return an array of docs (like a csv reader)
eventInfo = {}

if(eventList):
    for index in eventList:

        event_type = index[ConfigDB_Calc_TEInfo_0.COLUMN]
        while True:
            doc = index['data'].next()
            if doc is None:
                break;
            info = {}
            info["standard deviation cpu"] = float(doc["standard deviation cpu"]) if doc["standard deviation cpu"] else None
            info["average cpu"] = float(doc["average cpu"]) if doc["average cpu"] else None
            info["standard deviation memory"] = float(doc["standard deviation memory"]) if doc["standard deviation memory"] else None
            info["average memory"] = float(doc["average memory"]) if doc["average memory"] else None
            info["standard deviation ratio"] = float(doc["standard deviation ratio"]) if doc["standard deviation ratio"] else None
            info["average ratio"] = float(doc["average ratio"]) if doc["average ratio"] else None
            eventInfo[event_type] = info


##################################################################

import ConfigDB_Calc_TaskEvent_0
client_task = DataStoreClient("postgres", ConfigDB_Calc_TaskEvent_0)
data_task = client_task.getData() # return an array of docs (like a csv reader)

output = []
count = 1

if(data_task):
    # processing
    while True:
        doc = data_task.next()

        if doc is None:
            print "================="
            print "finish"
            print output
            print len(output)
            print count
            if len(output) > 0:
                print "done"
                client_task.saveData(output, numline=count)
            break;

        if doc['event type'] in ["2","3","4","6"]:

            if doc['CPU request'] and doc['memory request']:
                #print doc
                cpu = 0 if (not doc['CPU request']) else float(doc['CPU request'])
                memory = 0 if not doc['memory request'] else float(doc['memory request'])

                ratio = cpu/memory if (memory != 0) else 0

                event_type = doc['event type']
                event_avg_cpu = eventInfo[event_type]["average cpu"]
                event_sd_cpu = eventInfo[event_type]["standard deviation cpu"]
                event_avg_memory = eventInfo[event_type]["average memory"]
                event_sd_memory = eventInfo[event_type]["standard deviation memory"]
                event_avg_ratio = eventInfo[event_type]["average ratio"]
                event_sd_ratio = eventInfo[event_type]["standard deviation ratio"]

                newline = {}
                newline['job ID'] = doc['job ID']
                newline['task index'] = doc['task index']
                newline['event type'] = doc['event type']
                newline['time'] = doc['time']
                newline['ratio cpu memory'] = ratio
                newline['sds from all avg cpu'] = (cpu - avg_cpu)/sd_cpu if sd_cpu else None
                newline['sds from all avg memory'] = (memory - avg_memory)/sd_memory if sd_memory else None
                newline['sds from all avg ratio'] = (ratio - avg_ratio)/sd_ratio if sd_ratio else None
                newline['sds from event avg cpu'] = (cpu - event_avg_cpu)/event_sd_cpu if event_sd_cpu else None
                newline['sds from event avg memory'] = (memory - event_avg_memory)/event_sd_memory if event_sd_memory else None
                newline['sds from event avg ratio'] = (ratio - event_avg_ratio)/event_sd_ratio if event_sd_ratio else None
                output.append(newline)


                if len(output) >= 3000:
                    print "================="
                    print "inside"
                    print count
                    client_task.saveData(output, numline=count)
                    count += 3000
                    output = []
