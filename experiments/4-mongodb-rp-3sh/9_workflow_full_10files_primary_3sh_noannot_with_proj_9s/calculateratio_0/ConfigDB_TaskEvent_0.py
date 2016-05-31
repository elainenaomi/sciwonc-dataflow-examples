HOST = "mongos-3sh-ex4q:27017,mongos-3sh-lenv:27017,mongos-3sh-ql7j:27017"
PORT = "27017"
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["job ID", "task index", "event type","time", "memory request","CPU request"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "task_google.csv"
OUTPUT_FILE = "ratio_cpu_memory.csv"
