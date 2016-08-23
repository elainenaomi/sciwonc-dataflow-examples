#!/usr/bin/env python

from pymongo import MongoClient
import pymongo

HOST = "mongo-nosh-norep-10f:27017"
c = MongoClient(HOST)

dbname = "google"

task = "task_events"

db = c[dbname]


c[dbname].drop_collection(task)
c[dbname].create_collection(task)

#c.admin.command('enableSharding', dbname)

db = c[dbname]
task_col = db[task]


task_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
task_col.create_index([("_id", pymongo.ASCENDING)])
#c.admin.command('shardCollection', dbname+'.'+task, key={'_id': "hashed"})
#c.admin.command('shardCollection', dbname+'.'+task, key={'_id.filepath': "hashed"})
