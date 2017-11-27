#!/usr/bin/env python
"""
This activity wants to answer:
- which time interval was analysed?
- how many items has this interval?
"""
# Connection with SciWonc-Dataflow module
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_GeneralInfo_0

# connector and config
client = DataStoreClient("postgres", ConfigDB_GeneralInfo_0)

# according to config
data = client.getData() # return an array of docs (like a csv reader)
output = []

count = 0
min_time = None
max_time = None

if(data):

    # processing
    while True:
        doc = data.next()

        if doc is None:
            break;

        current_time = float(doc['time'])

        if current_time:
            if min_time is None or min_time > current_time:
                min_time = current_time

            if max_time is None or max_time < current_time:
                max_time = current_time

            count += 1

    if count > 0:
        newline = {}
        newline['interval seconds'] = (max_time - min_time)/1000000
        newline['total items'] = count
        newline['min timestamp'] = min_time
        newline['max timestamp'] = max_time

        output.append(newline)

        client.saveData(output)
