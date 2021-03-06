HOST = "wfSciwoncWiki:enw1989@172.31.29.101:27001,172.31.29.102:27001,172.31.29.103:27001,172.31.29.104:27001,172.31.29.105:27001,172.31.29.106:27001,172.31.29.107:27001,172.31.29.108:27001,172.31.29.109:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "wiki"
READ_PREFERENCE = "secondary"

COLLECTION_INPUT = "user_sessions"
COLLECTION_OUTPUT = "top_sessions"
PREFIX_COLUMN = "w_"

ATTRIBUTES = ["duration", "start time", "end time", "contributor_username", "edition_counts"]
SORT = ["duration", "end time"]
OPERATION_TYPE = "GROUP_BY_FIXED_WINDOW"
COLUMN = "end time"
VALUE = [(1080861526, 1083453525),(1083453526, 1086045525),(1086045526, 1088637525),(1088637526, 1091229525),(1091229526, 1093821525),(1093821526, 1096413525),(1096413526, 1099001925),(1099001926, 1101593925),(1101593926, 1104185925),(1104185926, 1106777925),(1106777926, 1109373525),(1109373526, 1111965525)]

INPUT_FILE = "user_info.csv"
OUTPUT_FILE = "top_sessions_3.csv"
