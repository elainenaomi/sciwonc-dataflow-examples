#!/usr/bin/env python
from pymongo import MongoClient
import pymongo

HOST = "wfSciwoncGW:enw1989@172.31.28.140:27001/?authSource=admin"

c = MongoClient('mongodb://'+HOST)

dbname = "googlew"

task = "task_events"
ratio = "ratio"

db = c[dbname]
task_col = db[task]
ratio_col = db[ratio]

task_col.drop_index([("CPU request", pymongo.ASCENDING)])
task_col.drop_index([("memory request", pymongo.ASCENDING)])
task_col.drop_index([("event type", pymongo.ASCENDING)])
ratio_col.drop_index([("event type", pymongo.ASCENDING)])
