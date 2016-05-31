#!/usr/bin/env python
"""
This activity will calculate the average of ratios between CPU request and Memory request by each event type.
These fields are optional and could be null.
"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_AverageCPU_0

# connector and config
client = DataStoreClient("mongodb", ConfigDB_AverageCPU_0)

# according to config
data = client.getData() # return an array of docs (like a csv reader)
output = []
sum_ratio = 0
total_valid_tasks = 0

total_tasks = 0
total_variance = 0

if(data):

    # processing
    while True:
        doc = data.next()

        if doc is None:
            break;

        print doc
        total_tasks += 1

        if(doc['CPU request']):
            sum_ratio = sum_ratio + float(doc['CPU request'])
            total_valid_tasks += 1


	average = sum_ratio / total_valid_tasks if total_valid_tasks > 0 else None

    print average

    if average:
        data = client.getData() # return an array of docs (like a csv reader)

        # processing
        while True:
            doc = data.next()

            if doc is None:
                break;

            print doc
            if(doc['CPU request']):
                total_variance = total_variance + (float(doc['CPU request']) - average) ** 2


    newline = {}
    newline['sum cpu'] = sum_ratio
    newline['sum variance'] = total_variance
    newline['total valid tasks'] = total_valid_tasks
    newline['total tasks'] = total_tasks
    newline['average cpu'] = average if average > 0 else None
    newline['variance cpu'] = total_variance/total_valid_tasks

    output.append(newline)


    # save
    client.saveData(output)
