#!/usr/bin/env python
"""
This activity will calculate the average_cpu of CPU request in whole data.
These fields are optional and could be null.
"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_StatsCPUMemory_0
import math

# connector and config
client = DataStoreClient("mongodb", ConfigDB_StatsCPUMemory_0)

# according to config
data = client.getData() # return an array of docs (like a csv reader)
output = []
sum_cpu = 0
sum_memory = 0
sum_ratio = 0
total_valid_tasks = 0

total_tasks = 0
total_variance_cpu = 0
total_variance_memory = 0
total_variance_ratio = 0

if(data):

    # processing
    while True:
        doc = data.next()

        if doc is None:
            break;

        total_tasks += 1

        if doc['CPU request'] and doc['memory request']:
            sum_cpu = sum_cpu + float(doc['CPU request'])
            sum_memory = sum_memory + float(doc['memory request'])
            ratio = float(doc['CPU request'])/float(doc['memory request']) if float(doc['memory request']) > 0 else 0
            sum_ratio = sum_ratio + ratio
            total_valid_tasks += 1

    # average
	average_cpu = sum_cpu / total_valid_tasks if total_valid_tasks > 0 else None
	average_memory = sum_memory / total_valid_tasks if total_valid_tasks > 0 else None
	average_ratio = sum_ratio / total_valid_tasks if total_valid_tasks > 0 else None

    # variance
    if average_cpu and average_memory and average_ratio:
        data = client.getData() # return an array of docs (like a csv reader)

        # processing
        while True:
            doc = data.next()

            if doc is None:
                break;

            if doc['CPU request'] and doc['memory request']:
                total_variance_cpu = total_variance_cpu + (float(doc['CPU request']) - average_cpu) ** 2
                total_variance_memory = total_variance_memory + (float(doc['memory request']) - average_memory) ** 2
                ratio = float(doc['CPU request'])/float(doc['memory request']) if float(doc['memory request']) > 0 else 0
                total_variance_ratio = total_variance_ratio + (ratio - average_ratio) ** 2


    newline = {}
    newline['sum cpu'] = sum_cpu
    newline['sum variance cpu'] = total_variance_cpu
    newline['average cpu'] = average_cpu if average_cpu > 0 else None
    newline['standard deviation cpu'] = math.sqrt(total_variance_cpu/total_valid_tasks)
    newline['variance cpu'] = total_variance_cpu/total_valid_tasks

    newline['sum memory'] = sum_memory
    newline['sum variance memory'] = total_variance_memory
    newline['average memory'] = average_memory if average_memory > 0 else None
    newline['standard deviation memory'] = math.sqrt(total_variance_memory/total_valid_tasks)
    newline['variance memory'] = total_variance_memory/total_valid_tasks

    newline['sum ratio'] = sum_ratio
    newline['sum variance ratio'] = total_variance_ratio
    newline['average ratio'] = average_ratio if average_ratio > 0 else None
    newline['standard deviation ratio'] = math.sqrt(total_variance_ratio/total_valid_tasks)
    newline['variance ratio'] = total_variance_ratio/total_valid_tasks


    newline['total valid tasks'] = total_valid_tasks
    newline['total tasks'] = total_tasks

    output.append(newline)


    # save
    client.saveData(output)
