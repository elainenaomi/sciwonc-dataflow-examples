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
import ConfigDB_Calc_StatsCPUMemory_5
client_statscpumemory = DataStoreClient("mongodb", ConfigDB_Calc_StatsCPUMemory_5)
data_statscpumemory = client_statscpumemory.getData()

if data_statscpumemory:
    while True:
        doc = data_statscpumemory.next()
        if doc is None:
            break;

        sd_cpu = doc['standard deviation cpu']
        avg_cpu = doc['average cpu']
        sd_memory = doc['standard deviation memory']
        avg_memory = doc['average memory']
        sd_ratio = doc['standard deviation ratio']
        avg_ratio = doc['average ratio']

##################################################################
import ConfigDB_Calc_TEInfo_5
client_taskinfo = DataStoreClient("mongodb", ConfigDB_Calc_TEInfo_5)

# according to config
eventList = client_taskinfo.getData() # return an array of docs (like a csv reader)
eventInfo = {}

if(eventList):
    for index in eventList:

        event_type = index[ConfigDB_Calc_TEInfo_5.COLUMN]
        while True:
            doc = index['data'].next()
            if doc is None:
                break;
            info = {}
            info["standard deviation cpu"] = doc["standard deviation cpu"]
            info["average cpu"] = doc["average cpu"]
            info["standard deviation memory"] = doc["standard deviation memory"]
            info["average memory"] = doc["average memory"]
            info["standard deviation ratio"] = doc["standard deviation ratio"]
            info["average ratio"] = doc["average ratio"]
            eventInfo[event_type] = info


##################################################################

import ConfigDB_Calc_TaskEvent_5
client_task = DataStoreClient("mongodb", ConfigDB_Calc_TaskEvent_5)
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
