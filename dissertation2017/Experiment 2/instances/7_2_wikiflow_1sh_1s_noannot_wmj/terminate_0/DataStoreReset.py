#!/usr/bin/env python
from pymongo import MongoClient
import pymongo

HOST = "wfSciwoncWiki:enw1989@172.31.2.76:27001/?authSource=admin"

c = MongoClient('mongodb://'+HOST)

dbname = "wiki"

sessions = "sessions"
user_sessions = "user_sessions"


db = c[dbname]
sessions_col = db[sessions]
user_sessions_col = db[user_sessions]


sessions_col.drop_index([("contributor_username", pymongo.ASCENDING)])
sessions_col.drop_index([("timestamp", pymongo.ASCENDING)])
user_sessions_col.drop_index([("timestamp", pymongo.ASCENDING)])
