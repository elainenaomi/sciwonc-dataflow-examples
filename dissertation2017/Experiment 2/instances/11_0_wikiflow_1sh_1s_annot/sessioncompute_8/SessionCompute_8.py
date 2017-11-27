#!/usr/bin/env python
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_SessionCompute_8
import pprint

# connector and config
client = DataStoreClient("mongodb", ConfigDB_SessionCompute_8)
config = ConfigDB_SessionCompute_8

# according to config
dataList = client.getData() # return an array of docs (like a csv reader)
output = []

ONE_HOUR_IN_SECONDS = 3600

if(dataList):
    for i in dataList:
        contributor_username = i[config.COLUMN]

        current_user = contributor_username
        start_time = None
        end_time = None
        duration = None
        last_start_timestamp =  None
        count = 1

        if contributor_username:
            print "\n\n"
            print contributor_username.encode('utf-8')


            while True:
                doc = i['data'].next()
                if doc is None:
                    break;

                print doc["timestamp"]

                if start_time is None:
                    start_time = float(doc["timestamp"])

                if end_time is None:
                    end_time = start_time + ONE_HOUR_IN_SECONDS
                else:
                    if float(doc["timestamp"]) <= end_time:
                        end_time = float(doc["timestamp"]) + ONE_HOUR_IN_SECONDS
                        count += 1
                    else:
                        new_doc = {}
                        new_doc["start time"] = start_time
                        new_doc["end time"] = end_time
                        new_doc["duration"] = (end_time - start_time)
                        new_doc["edition_counts"] = count
                        new_doc["contributor_username"] = contributor_username
                        output.append(new_doc)

                        start_time = float(doc["timestamp"])
                        end_time = start_time + ONE_HOUR_IN_SECONDS
                        count = 1

            if start_time:
                new_doc = {}
                new_doc["start time"] = start_time
                new_doc["end time"] = end_time
                new_doc["duration"] = (end_time - start_time)
                new_doc["edition_counts"] = count
                new_doc["contributor_username"] = contributor_username
                output.append(new_doc)

    pprint.pprint(output)
    clientOutput = DataStoreClient("mongodb", ConfigDB_SessionCompute_8)
    clientOutput.saveData(output)

# import datetime
# print(
#     datetime.datetime.fromtimestamp(
#         int("1176585742")
#     ).strftime('%Y-%m-%d %H:%M:%S')
# )

# {
# start time:
# end time:
# duration:
# user:
# }

# import time
# timestamp2 = time.mktime(d.timetuple()) # DO NOT USE IT WITH UTC DATE
# datetime.fromtimestamp(timestamp2)
# datetime.datetime(2011, 1, 1, 0, 0)
