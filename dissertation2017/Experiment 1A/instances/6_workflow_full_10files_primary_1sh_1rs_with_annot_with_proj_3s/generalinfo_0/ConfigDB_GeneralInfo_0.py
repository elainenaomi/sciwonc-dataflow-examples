HOST = "172.31.28.140:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "general_info"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["time", "job ID", "task index"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "task_events_0.dat"
OUTPUT_FILE = "general_info_0.dat"
