#!/usr/bin/env python
"""
This activity will calculate the average of ratios between CPU request and Memory request by each event type.
These fields are optional and could be null.

--> categorizar por evento (reduce)
     -> quantas tarefa CPU-bound
     -> quantas  tarefa Memory-Bound
     -> media da relacao CPU/Memory
     -> desvio padrao ratio

For example, the maximum observed memory capacity across all machines is used to rescale all memory requests and usage values

"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import math, sys
import ConfigDB_AverageRatioEvent_0
# connector and config
client = DataStoreClient("postgres", ConfigDB_AverageRatioEvent_0)

config = ConfigDB_AverageRatioEvent_0

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
