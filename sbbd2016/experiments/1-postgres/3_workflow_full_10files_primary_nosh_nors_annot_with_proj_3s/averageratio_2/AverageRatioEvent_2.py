#!/usr/bin/env python
"""
This activity will calculate the average of ratios between CPU request and Memory request by each event type.
These fields are optional and could be null.
"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_Average_2

# connector and config
client = DataStoreClient("postgres", ConfigDB_Average_2)

config = ConfigDB_Average_2

# according to config
dataList = client.getData() # return an array of docs (like a csv reader)
output = []


if(dataList):
    for i in dataList:

        sum_ratio = 0
        total_valid_tasks = 0
        total_tasks = 0
        event_type = i[config.COLUMN]

        while True:
            doc = i['data'].next()

            if doc is None:
                break;

            total_tasks += 1

            if(doc['ratio cpu memory']):
                sum_ratio = sum_ratio + float(doc['ratio cpu memory'])
                total_valid_tasks += 1

        newline = {}
        newline['event type'] = event_type
        newline['sum ratio cpu memory'] = sum_ratio
        newline['total valid tasks'] = total_valid_tasks
        newline['total tasks'] = total_tasks
        if((sum_ratio > 0) and (total_valid_tasks > 0)):
            newline['mean ratio cpu memory'] = sum_ratio / total_valid_tasks
        else:
            newline['mean ratio cpu memory'] = None

        output.append(newline)

    # save
    client.saveData(output)
