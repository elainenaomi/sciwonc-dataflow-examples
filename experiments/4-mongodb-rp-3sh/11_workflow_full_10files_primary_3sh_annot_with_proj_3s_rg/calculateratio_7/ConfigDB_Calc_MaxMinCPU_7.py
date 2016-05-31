HOST = "mongos-3sh-ex4q:27017,mongos-3sh-lenv:27017,mongos-3sh-ql7j:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "maxmin_cpu"
COLLECTION_OUTPUT = "ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["max cpu","min cpu"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"

OUTPUT_FILE = "ratio_cpu_memory.csv"
