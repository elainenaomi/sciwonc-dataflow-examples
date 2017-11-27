#!/usr/bin/env python
"""
Categorize per event
-- how many tasks are CPU intensive
-- how many tasks are Memory intensive
-- how many tasks use CPU and Memory normal

"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import math, sys
import ConfigDB_AverageRatioEvent_1
# connector and config
client = DataStoreClient("mongodb", ConfigDB_AverageRatioEvent_1)

config = ConfigDB_AverageRatioEvent_1

# according to config
dataList = client.getData() # return an array of docs (like a csv reader)
output = []

if(dataList):
    for i in dataList:
        event_type = i[config.COLUMN]


        total_cpu_task = 0
        total_memory_task = 0
        total_balanced_task = 0

        if event_type:
            while True:
                doc = i['data'].next()

                if doc is None:
                    break;

                if(doc['sds from all avg ratio']):
                    sds = float(doc['sds from all avg ratio'])
                    print sds
                    if (sds <= -0.5):
                        total_memory_task += 1
                    elif(sds >= 0.5):
                        total_cpu_task += 1
                    else:
                        total_balanced_task += 1

            newline = {}
            newline['event type'] = event_type
            newline['total cpu task'] = total_cpu_task
            newline['total memory task'] = total_memory_task
            newline['total balanced task'] = total_balanced_task

            output.append(newline)

    # save
    client.saveData(output)
