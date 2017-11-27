#!/usr/bin/env python
"""
Computes per event type:
  - how many tasks are per event?
  - which is the average and standard deviation of CPU request per event?
  - which is the average and standard deviation of Memory request per event?
"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import sys
##################################################################
import ConfigDB_Task_StatsCPUMemory_4
client_averagecpu = DataStoreClient("mongodb", ConfigDB_Task_StatsCPUMemory_4)
data_averagecpu = client_averagecpu.getData()

if data_averagecpu:
    while True:
        doc = data_averagecpu.next()
        if doc is None:
            break;

        sd_cpu = doc['standard deviation cpu']
        avg_cpu = doc['average cpu']
        sd_memory = doc['standard deviation memory']
        avg_memory = doc['average memory']
        sd_ratio = doc['standard deviation ratio']
        avg_ratio = doc['average ratio']


##################################################################
import ConfigDB_Task_GeneralInfo_4
client_geninfo = DataStoreClient("mongodb", ConfigDB_Task_GeneralInfo_4)
data_geninfo = client_geninfo.getData()

if data_geninfo:
    while True:
        doc = data_geninfo.next()
        if doc is None:
            break;
        print doc
        total_items = doc['total items']

##################################################################


import ConfigDB_TaskEvent_4
import math

# connector and config
config = ConfigDB_TaskEvent_4
client = DataStoreClient("mongodb", config)

# according to config
eventList = client.getData() # return an array of docs (like a csv reader)

info = {}

if(eventList):
    for index in eventList:

        # sum_ratio = 0
        total_valid_tasks = 0
        total_tasks = 0
        event_type = index[config.COLUMN]
        sum_memory = 0
        sum_cpu = 0
        sum_ratio = 0

        while True:
            doc = index['data'].next()

            if doc is None:
                break;

            total_tasks += 1

            if(doc['memory request']):
                sum_memory = sum_memory + float(doc['memory request'])

            if(doc['CPU request']):
                sum_cpu = sum_cpu + float(doc['CPU request'])

            if(doc['CPU request']) and (doc['memory request']):
                ratio = float(doc['CPU request'])/ float(doc['memory request']) if float(doc['memory request']) > 0 else 0
                sum_ratio = sum_ratio + ratio
                total_valid_tasks += 1

        # average
        average_memory = sum_memory / total_valid_tasks if total_valid_tasks > 0 else 0
        average_cpu = sum_cpu / total_valid_tasks if total_valid_tasks > 0 else 0
        average_ratio = sum_ratio / total_valid_tasks if total_valid_tasks > 0 else 0

        event_info = {}
        event_info['event type'] = event_type
        event_info['sum memory'] = sum_memory
        event_info['sum cpu'] = sum_cpu
        event_info['sum ratio'] = sum_ratio

        event_info['total valid tasks'] = total_valid_tasks
        event_info['total tasks'] = total_tasks

        event_info['average memory'] = average_memory
        event_info['average cpu'] = average_cpu
        event_info['average ratio'] = average_ratio
        info[event_type] = event_info



# according to config
eventList = client.getData() # return an array of docs (like a csv reader)
output = []

if(eventList):
    for index in eventList:

        event_type = index[config.COLUMN]
        total_variance_memory = 0
        total_variance_cpu = 0
        total_variance_ratio = 0

        average_memory = info[event_type]['average memory']
        average_cpu = info[event_type]['average cpu']
        average_ratio = info[event_type]['average ratio']

        while True:
            doc = index['data'].next()
            if doc is None:
                break;

            if(doc['memory request'] and doc['CPU request']):
                total_variance_memory = total_variance_memory + (float(doc['memory request']) - average_memory) ** 2
                total_variance_cpu = total_variance_cpu + (float(doc['CPU request']) - average_cpu) ** 2
                ratio = float(doc['CPU request']) / float(doc['memory request']) if float(doc['memory request']) > 0 else 0
                total_variance_ratio = total_variance_ratio + (ratio - average_ratio) ** 2

        total_valid_tasks = info[event_type]['total valid tasks']  if total_valid_tasks is not None else 0

        newline = {}
        newline['event type'] = event_type
        newline['sum memory'] = info[event_type]['sum memory']
        newline['sum cpu'] = info[event_type]['sum cpu']
        newline['sum ratio'] = info[event_type]['sum ratio']

        newline['total valid tasks'] = info[event_type]['total valid tasks']
        newline['total tasks'] = info[event_type]['total tasks']

        newline['average memory'] = average_memory
        newline['average cpu'] = average_cpu
        newline['average ratio'] = average_ratio

        newline['variance memory'] = total_variance_memory/total_valid_tasks  if total_valid_tasks > 0 else None
        newline['variance cpu'] = total_variance_cpu/total_valid_tasks  if total_valid_tasks > 0 else None
        newline['variance ratio'] = total_variance_ratio/total_valid_tasks  if total_valid_tasks > 0 else None

        newline['standard deviation memory'] = math.sqrt(total_variance_memory/total_valid_tasks)  if total_valid_tasks > 0 else None
        newline['standard deviation cpu'] = math.sqrt(total_variance_cpu/total_valid_tasks)  if total_valid_tasks > 0 else None
        newline['standard deviation ratio'] = math.sqrt(total_variance_ratio/total_valid_tasks)  if total_valid_tasks > 0 else None


        newline['percentagem from total'] = total_items * 100.0 / total_valid_tasks if total_valid_tasks > 0 else None


        newline['sds from avg cpu'] = (average_cpu - avg_cpu)/sd_cpu  if sd_cpu is not None else None
        newline['sds from avg memory'] = (average_memory - avg_memory)/sd_memory if sd_memory is not None else None
        newline['sds from avg ratio'] = (average_ratio - avg_ratio)/sd_ratio if sd_ratio is not None else None

        output.append(newline)

    # save
    client.saveData(output)
