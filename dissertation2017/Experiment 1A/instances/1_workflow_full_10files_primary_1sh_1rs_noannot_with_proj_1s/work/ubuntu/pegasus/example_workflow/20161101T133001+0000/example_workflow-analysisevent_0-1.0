#!/usr/bin/env python
"""
definir qual tipo de tarefa tem mais por evento e no geral
"""

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_Analysis_AverageEvent_0

# connector and config
client = DataStoreClient("postgres", ConfigDB_Analysis_AverageEvent_0)

# according to config
data = client.getData() # return an array of docs (like a csv reader)
output = []

info = {"cpu":0, "memory":0, "balanced":0}

if(data):
    # processing
    while True:
        doc = data.next()

        if doc is None:
            break;

        event_type = doc['event type']

        task_types = {}
        task_types["cpu"] = float(doc['total cpu task'])
        task_types["memory"] = float(doc['total memory task'])
        task_types["balanced"] = float(doc['total balanced task'])

        max_type = max(task_types, key=task_types.get)
        max_value = task_types[max_type]

        newline = {}
        newline['event type'] = event_type
        newline['task type'] = max_type
        newline['total task type'] = max_value

        output.append(newline)

        info[max_type] += max_value

    max_type = max(info, key=info.get)
    max_value = info[max_type]

    newline = {}
    newline['event type'] = "all"
    newline['task type'] = max_type
    newline['total task type'] = max_value

    output.append(newline)

    # save
    client.saveData(output)
