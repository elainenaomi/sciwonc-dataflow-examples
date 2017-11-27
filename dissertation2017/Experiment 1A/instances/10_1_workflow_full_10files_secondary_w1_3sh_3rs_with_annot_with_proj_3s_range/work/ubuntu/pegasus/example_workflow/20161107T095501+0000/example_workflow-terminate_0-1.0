#!/usr/bin/env python
from pymongo import MongoClient
import pymongo

HOST = "ip-172-31-29-102.us-west-2.compute.internal:27017,ip-172-31-29-103.us-west-2.compute.internal:27017,ip-172-31-29-104.us-west-2.compute.internal:27017,ip-172-31-29-105.us-west-2.compute.internal:27017,ip-172-31-29-101.us-west-2.compute.internal:27017,ip-172-31-29-106.us-west-2.compute.internal:27017,ip-172-31-29-107.us-west-2.compute.internal:27017,ip-172-31-29-108.us-west-2.compute.internal:27017,ip-172-31-29-109.us-west-2.compute.internal:27017"

c = MongoClient('mongodb://'+HOST)

dbname = "googler"

task = "task_events"

db = c[dbname]
task_col = db[task]

task_col.drop_index([("CPU request", pymongo.ASCENDING)])
task_col.drop_index([("memory request", pymongo.ASCENDING)])
