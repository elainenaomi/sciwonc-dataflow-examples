#!/usr/bin/env python

from pymongo import MongoClient
import pymongo

HOST = "mongos-3sh-ex4q:27017,mongos-3sh-lenv:27017,mongos-3sh-ql7j:27017"

c = MongoClient('mongodb://'+HOST)

dbname = "google"

task = "task_events"
avg_cpu = "average_cpu"
mm_cpu = "maxmin_cpu"
med_cpu = "median_cpu"
ratio = "ratio"
avg = "average_ratio"
analysis = "analysis_ratio"


db = c[dbname]

task_col = db[task]

c[dbname].drop_collection(avg_cpu)
c[dbname].drop_collection(mm_cpu)
c[dbname].drop_collection(med_cpu)
c[dbname].drop_collection(ratio)
c[dbname].drop_collection(avg)
c[dbname].drop_collection(analysis)


task_col.drop_index("CPU request_1") #remove by name

dbname = "config"
db_c = c[dbname]
coll = "collections"
coll_col = db_c[coll]
coll_col.remove({"_id":"google.ratio"})
