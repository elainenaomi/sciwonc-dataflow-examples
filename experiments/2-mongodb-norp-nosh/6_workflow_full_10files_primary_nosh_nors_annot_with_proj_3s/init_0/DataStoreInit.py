#!/usr/bin/env python

from pymongo import MongoClient
import pymongo

HOST = "mongo-nosh-norep-10f:27017"

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
c[dbname].create_collection(avg_cpu)


c[dbname].drop_collection(mm_cpu)
c[dbname].create_collection(mm_cpu)

c[dbname].drop_collection(med_cpu)
c[dbname].create_collection(med_cpu)


c[dbname].drop_collection(ratio)
c[dbname].create_collection(ratio)

c[dbname].drop_collection(avg)
c[dbname].create_collection(avg)

c[dbname].drop_collection(analysis)
c[dbname].create_collection(analysis)



db = c[dbname]
task_col = db[task]
ratio_col = db[ratio]
avg_col = db[avg]
analysis_col = db[analysis]



task_col.create_index([("CPU request", pymongo.ASCENDING)])
task_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
#task_col.create_index([("_id", pymongo.HASHED)])


ratio_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
#ratio_col.create_index([("_id", pymongo.HASHED)])

avg_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
#avg_col.create_index([("_id", pymongo.HASHED)])

analysis_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
#analysis_col.create_index([("_id", pymongo.HASHED)])



avg_cpu_col = db[avg_cpu]
med_cpu_col = db[med_cpu]
mm_cpu_col = db[mm_cpu]

avg_cpu_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
med_cpu_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
mm_cpu_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
