HOST = "172.31.28.140:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "stats_cpumemory"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["CPU request", "memory request"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"


INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "stats_cpumemory_0.dat"
