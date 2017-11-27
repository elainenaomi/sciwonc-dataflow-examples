#!/usr/bin/env python

from pymongo import MongoClient
import pymongo

HOST = "wfSciwoncWiki:enw1989@172.31.2.76:27001/?authSource=admin"

c = MongoClient('mongodb://'+HOST)

dbname = "wiki"

sessions = "sessions"

contributors = "contributors"
user_sessions = "user_sessions"
top_sessions = "top_sessions"



c[dbname].drop_collection(contributors)
c[dbname].create_collection(contributors)

c[dbname].drop_collection(user_sessions)
c[dbname].create_collection(user_sessions)

c[dbname].drop_collection(top_sessions)
c[dbname].create_collection(top_sessions)


db = c[dbname]
sessions_col = db[sessions]
contributors_col = db[contributors]
user_sessions_col = db[user_sessions]
top_sessions_col = db[top_sessions]


sessions_col.create_index([("contributor_username", pymongo.ASCENDING)])
sessions_col.create_index([("timestamp", pymongo.ASCENDING)])
user_sessions_col.create_index([("timestamp", pymongo.ASCENDING)])

#sessions_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])

contributors_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
user_sessions_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
top_sessions_col.create_index([("_id.filepath", pymongo.ASCENDING),("_id.numline", pymongo.ASCENDING)])
