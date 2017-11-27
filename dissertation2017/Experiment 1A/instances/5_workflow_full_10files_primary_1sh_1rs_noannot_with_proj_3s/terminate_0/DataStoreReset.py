#!/usr/bin/env python
from pymongo import MongoClient
import pymongo

HOST = "172.31.28.140:27017"

c = MongoClient('mongodb://'+HOST)

dbname = "google"

task = "task_events"

db = c[dbname]
task_col = db[task]

task_col.drop_index([("CPU request", pymongo.ASCENDING)])
task_col.drop_index([("memory request", pymongo.ASCENDING)])
