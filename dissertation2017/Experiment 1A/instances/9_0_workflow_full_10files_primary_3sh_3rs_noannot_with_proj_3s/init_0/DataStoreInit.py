#!/usr/bin/env python

from pymongo import MongoClient
import pymongo

HOST = "ip-172-31-29-102.us-west-2.compute.internal:27017,ip-172-31-29-103.us-west-2.compute.internal:27017,ip-172-31-29-104.us-west-2.compute.internal:27017,ip-172-31-29-105.us-west-2.compute.internal:27017,ip-172-31-29-101.us-west-2.compute.internal:27017,ip-172-31-29-106.us-west-2.compute.internal:27017,ip-172-31-29-107.us-west-2.compute.internal:27017,ip-172-31-29-108.us-west-2.compute.internal:27017,ip-172-31-29-109.us-west-2.compute.internal:27017"

c = MongoClient('mongodb://'+HOST)

dbname = "google"

task = "task_events"
ginfo = "general_info"
statscpumemory = "stats_cpumemory"
maxmincpumemory = "maxmin_cpumemory"
mediancpu = "median_cpu"
medianmemory = "median_memory"
tinfo = "task_events_info"
ratio = "ratio"
avgratio = "average_ratioevent"
analysis = "analysis_ratio"


db = c[dbname]

task_col = db[task]

c[dbname].drop_collection(ginfo)
c[dbname].create_collection(ginfo)

c[dbname].drop_collection(statscpumemory)
c[dbname].create_collection(statscpumemory)

c[dbname].drop_collection(maxmincpumemory)
c[dbname].create_collection(maxmincpumemory)

c[dbname].drop_collection(mediancpu)
c[dbname].create_collection(mediancpu)
c[dbname].drop_collection(medianmemory)
c[dbname].create_collection(medianmemory)

c[dbname].drop_collection(tinfo)
c[dbname].create_collection(tinfo)

c[dbname].drop_collection(ratio)
c[dbname].create_collection(ratio)

c[dbname].drop_collection(avgratio)
c[dbname].create_collection(avgratio)

c[dbname].drop_collection(analysis)
c[dbname].create_collection(analysis)

db = c[dbname]
task_col = db[task]

ginfo_col = db[ginfo]
statscpumemory_col = db[statscpumemory]
maxmincpumemory_col = db[maxmincpumemory]
mediancpu_col = db[mediancpu]
medianmemory_col = db[medianmemory]
tinfo_col = db[tinfo]
ratio_col = db[ratio]
avgratio_col = db[avgratio]
analysis_col = db[analysis]

task_col.create_index([("CPU request", pymongo.ASCENDING)])
task_col.create_index([("memory request", pymongo.ASCENDING)])
task_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])

ginfo_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
statscpumemory_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
maxmincpumemory_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
mediancpu_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
medianmemory_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
tinfo_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
ratio_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
avgratio_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
analysis_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
