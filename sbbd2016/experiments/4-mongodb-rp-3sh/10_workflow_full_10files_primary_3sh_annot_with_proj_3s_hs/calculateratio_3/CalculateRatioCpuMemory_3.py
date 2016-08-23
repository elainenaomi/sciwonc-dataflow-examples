#!/usr/bin/env python
"""
This activity will calculate the ratio between CPU request and Memory request by (job ID, task index, event type).
These fields are optional and could be null.
"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_TaskEvent_3
import ConfigDB_Calc_MaxMinCPU_3
import ConfigDB_Calc_AverageCPU_3
import ConfigDB_Calc_MedianCPU_3

import math

##################################################################

client_maxmincpu = DataStoreClient("mongodb", ConfigDB_Calc_MaxMinCPU_3)
data_maxmincpu = client_maxmincpu.getData()

if data_maxmincpu:
    while True:
        doc = data_maxmincpu.next()
        if doc is None:
            break;

        print doc
        max_cpu = doc['max cpu']
        min_cpu = doc['min cpu']



##################################################################

client_mediancpu = DataStoreClient("mongodb", ConfigDB_Calc_MedianCPU_3)
data_mediancpu = client_mediancpu.getData()

if data_mediancpu:
    while True:
        doc = data_mediancpu.next()
        if doc is None:
            break;

        print doc
        median_cpu = doc['median cpu']

##################################################################

client_avgcpu = DataStoreClient("mongodb", ConfigDB_Calc_AverageCPU_3)
data_avgcpu = client_avgcpu.getData()

if data_avgcpu:
    while True:
        doc = data_avgcpu.next()
        if doc is None:
            break;

        print doc
        avg_cpu = doc['average cpu']


##################################################################


# task_events
client_task = DataStoreClient("mongodb", ConfigDB_TaskEvent_3)
data_task = client_task.getData() # return an array of docs (like a csv reader)


if(data_task):
    # processing
    while True:
        doc = data_task.next()

        if doc is None:
            break;

        #print doc
        cpu = 0 if (not doc['CPU request']) else float(doc['CPU request'])
        memory = 0 if not doc['memory request'] else float(doc['memory request'])

        ratio = cpu/memory if (memory != 0) else None



        newline = {}
        newline['job ID'] = doc['job ID']
        newline['task index'] = doc['task index']
        newline['event type'] = doc['event type']
        newline['time'] = doc['time']
        newline['ratio cpu memory'] = ratio

        if max_cpu and min_cpu:
            if cpu == max_cpu:
                newline['max cpu'] = 'true'
            else:
                newline['max cpu'] = 'false'

            if cpu == min_cpu:
                newline['min cpu'] = 'true'
            else:
                newline['min cpu'] = 'false'

        if avg_cpu:
            if cpu == avg_cpu:
                newline['avg cpu'] = 'equal'
            elif cpu > avg_cpu:
                newline['avg cpu'] = 'greater'
            else:
                newline['avg cpu'] = 'less'

        if median_cpu:
            if cpu == median_cpu:
                newline['median cpu'] = 'equal'
            elif cpu > median_cpu:
                newline['median cpu'] = 'greater'
            else:
                newline['median cpu'] = 'less'

        client_task.saveData(newline)
