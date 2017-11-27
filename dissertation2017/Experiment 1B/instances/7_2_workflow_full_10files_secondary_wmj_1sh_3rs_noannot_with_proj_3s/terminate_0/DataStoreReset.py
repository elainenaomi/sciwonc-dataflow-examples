#!/usr/bin/env python
from pymongo import MongoClient
import pymongo

HOST = "wfSciwoncGW:enw1989@172.31.2.76:27001/?authSource=admin"

c = MongoClient('mongodb://'+HOST)

dbname = "googlew"

task = "task_events"

db = c[dbname]
task_col = db[task]

task_col.drop_index([("CPU request", pymongo.ASCENDING)])
task_col.drop_index([("memory request", pymongo.ASCENDING)])
