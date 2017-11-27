HOST = "172.31.28.140:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "task_events_info"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "CPU request", "memory request"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "GROUP_BY_COLUMN"
COLUMN = "event type"
VALUE = ["3","4","5"]

INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "task_events_info_1.dat"
