#!/usr/bin/env python
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_Longest_7
import pprint
import datetime

# connector and config
client = DataStoreClient("mongodb", ConfigDB_Longest_7)
config = ConfigDB_Longest_7

# according to config
dataList = client.getData() # return an array of docs (like a csv reader)
output = []
print "\n"

# """Formats a string containing the user, count, and session."""
if(dataList):
    print "Total of windows:", len(dataList)
    for i in dataList:
        column = i[config.COLUMN]
        print "\nNew column: ", column

        new_doc = {}

        while True:
            doc = i['data'].next()

            if doc is None:
                break;

            if "longest session" not in new_doc or new_doc["longest session"] < doc["duration"]:
                new_doc["longest session"] = doc["duration"]
                new_doc["top user"] = doc["contributor_username"]
                new_doc["edition counts"] = doc["edition_counts"]
                new_doc["window"] = column
                new_doc["h_window"] = datetime.datetime.fromtimestamp(column).strftime('%Y-%m-%d %H:%M:%S')
                new_doc["start time"] = doc["start time"]
                new_doc["end time"] = doc["end time"]

        if "longest session" in new_doc:
            print "New doc: ", new_doc, '\n'
            output.append(new_doc)

    # pprint.pprint(output)
    clientOutput = DataStoreClient("mongodb", ConfigDB_Longest_7)
    clientOutput.saveData(output)

# 'user1 : [0.0, 3600.002) : 3 : [0.0, 2592000.0)',
# 'user2 : [0.0, 3603.602) : 4 : [0.0, 2592000.0)',
# 'user2 : [7200.0, 10800.0) : 1 : [0.0, 2592000.0)',
# 'user3 : [3024.0, 6624.0) : 1 : [0.0, 2592000.0)',

# { "end time" : 6624, "edition_counts" : 1, "start time" : 3024 }
# { "end time" : 10804, "edition_counts" : 1, "start time" : 7204 } ** salvei errado no db
# { "end time" : 3600.002, "edition_counts" : 3, "start time" : 0 }
# { "end time" : 3603.602, "edition_counts" : 4, "start time" : 0 }
