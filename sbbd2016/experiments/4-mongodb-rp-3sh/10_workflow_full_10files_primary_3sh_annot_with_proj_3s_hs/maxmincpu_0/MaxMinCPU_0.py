#!/usr/bin/env python
"""
This activity will calculate the mean of ratios between CPU request and Memory request by each event type.
These fields are optional and could be null.
"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_MaxMinCPU_0

# connector and config
client = DataStoreClient("mongodb", ConfigDB_MaxMinCPU_0)

# according to config
data = client.getData() # return an array of docs (like a csv reader)
output = []

max_cpu = None
min_cpu = None


if(data):

    # processing
    while True:
        doc = data.next()

        if doc is None:
            break;

        if(doc['CPU request']):
            if max_cpu:
                if max_cpu < float(doc['CPU request']):
                    max_cpu = float(doc['CPU request'])
            else:
                max_cpu = float(doc['CPU request'])

            if min_cpu:
                if min_cpu > float(doc['CPU request']):
                    min_cpu = float(doc['CPU request'])
            else:
                min_cpu = float(doc['CPU request'])

    newline = {}
    newline['max cpu'] = max_cpu
    newline['min cpu'] = min_cpu

    output.append(newline)

    client.saveData(output)
