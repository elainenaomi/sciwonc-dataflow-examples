HOST = "wfSciwoncWiki:enw1989@172.31.29.101:27001,172.31.29.102:27001,172.31.29.103:27001,172.31.29.104:27001,172.31.29.105:27001,172.31.29.106:27001,172.31.29.107:27001,172.31.29.108:27001,172.31.29.109:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "wiki"
READ_PREFERENCE = "primary"

COLLECTION_INPUT = "user_sessions"
COLLECTION_OUTPUT = "top_sessions"
PREFIX_COLUMN = "w_"

ATTRIBUTES = ["duration", "start time", "end time", "contributor_username", "edition_counts"]
SORT = ["duration", "end time"]
OPERATION_TYPE = "GROUP_BY_FIXED_WINDOW"
COLUMN = "end time"
VALUE = [(1205277526, 1207869525),(1207869526, 1210461525),(1210461526, 1213053525),(1213053526, 1215645525),(1215645526, 1218237525),(1218237526, 1220829525),(1220829526, 1223421525),(1223421526, 1226009925),(1226009926, 1228601925),(1228601926, 1231193925),(1231193926, 1233785925),(1233785926, 1236381525)]

INPUT_FILE = "user_info.csv"
OUTPUT_FILE = "top_sessions_7.csv"
