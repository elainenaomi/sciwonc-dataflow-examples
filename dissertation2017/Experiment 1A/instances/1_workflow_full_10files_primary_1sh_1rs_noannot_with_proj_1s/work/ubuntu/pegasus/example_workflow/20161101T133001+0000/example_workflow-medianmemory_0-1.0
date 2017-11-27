#!/usr/bin/env python

# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_MedianMemory_0

# connector and config
client = DataStoreClient("postgres", ConfigDB_MedianMemory_0)

data = client.getData()
output = []


if(data):
    #docs = []
    n = 0

    # processing
    while True:
        doc = data.next()
        #docs.append(doc)
        print doc
        if doc is None:
            break;
        n = n + 1

    print "Total docs"
    print n

    data = client.getData()
    pos = 0
    cpuPrev = 0
    cpuCur = 0

    while True:
        doc = data.next()
        cpuCur = float(doc['memory request'])

        if pos == (n-1):
            if n % 2 == 0:
                median = (cpuCur + cpuPrev)/2
            else:
                median = cpuCur/2

            break

        if doc is None:
            break;

        pos = pos + 1
        cpuPrev = float(doc['memory request'])

    print 'median:',median


    newline = {}
    newline['median memory'] = median

    output.append(newline)

    client.saveData(output)
