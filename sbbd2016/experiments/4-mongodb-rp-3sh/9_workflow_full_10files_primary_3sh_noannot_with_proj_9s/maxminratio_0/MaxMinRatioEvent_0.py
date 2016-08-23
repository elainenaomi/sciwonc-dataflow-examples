#!/usr/bin/env python
"""
This activity will calculate the mean of ratios between CPU request and Memory request by each event type.
These fields are optional and could be null.
"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_MaxMin_0

# connector and config
client = DataStoreClient("mongodb", ConfigDB_MaxMin_0)

# according to config
data = client.getData() # return an array of docs (like a csv reader)
output = []

max_event = None
max_ratio = None
min_event = None
min_ratio = None


if(data):
    # processing
    while True:
        doc = data.next()

        if doc is None:
            break;

        print doc

        ratio = doc['mean ratio cpu memory']
        event = doc['event type']

        if(ratio):
            if(max_event is None) or (max_ratio <= ratio):
                max_ratio = ratio
                max_event = event

            if(min_event is None) or (min_ratio >= ratio):
                min_ratio = ratio
                min_event = event


    newline = {}
    newline['event type max'] = max_event
    newline['ratio max'] = max_ratio
    newline['event type min'] = min_event
    newline['ratio min'] = min_ratio
    print newline
    output.append(newline)

    # save
    client.saveData(output)
