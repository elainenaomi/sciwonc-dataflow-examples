HOST = "wfSciwoncWiki:enw1989@172.31.29.101:27001,172.31.29.102:27001,172.31.29.103:27001,172.31.29.104:27001,172.31.29.105:27001,172.31.29.106:27001,172.31.29.107:27001,172.31.29.108:27001,172.31.29.109:27001/?authSource=admin:27017"
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
VALUE = [(1111965526, 1114557525),(1114557526, 1117149525),(1117149526, 1119741525),(1119741526, 1122333525),(1122333526, 1124925525),(1124925526, 1127517525),(1127517526, 1130105925),(1130105926, 1132697925),(1132697926, 1135289925),(1135289926, 1137881925),(1137881926, 1140477525),(1140477526, 1143069525)]

INPUT_FILE = "user_info.csv"
OUTPUT_FILE = "top_sessions_4.csv"