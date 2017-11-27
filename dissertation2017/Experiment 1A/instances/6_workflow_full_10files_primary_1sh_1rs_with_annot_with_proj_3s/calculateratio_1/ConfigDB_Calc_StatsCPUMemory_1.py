HOST = "172.31.28.140:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "stats_cpumemory"
COLLECTION_OUTPUT = "ratio"

PREFIX_COLUMN = "g_"

ATTRIBUTES = ["standard deviation cpu", "average cpu","standard deviation memory", "average memory","standard deviation ratio", "average ratio"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"
