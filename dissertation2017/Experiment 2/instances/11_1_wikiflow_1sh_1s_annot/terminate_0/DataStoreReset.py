#!/usr/bin/env python
from pymongo import MongoClient
import pymongo

HOST = "wfSciwoncWiki:enw1989@172.31.29.101:27001,172.31.29.102:27001,172.31.29.103:27001,172.31.29.104:27001,172.31.29.105:27001,172.31.29.106:27001,172.31.29.107:27001,172.31.29.108:27001,172.31.29.109:27001/?authSource=admin"
READ_PREFERENCE = "secondary"

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
