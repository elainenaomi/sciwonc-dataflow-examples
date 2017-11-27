HOST = "wfSciwoncGW:enw1989@172.31.2.76:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googlew"
READ_PREFERENCE = "primary"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "median_memory"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["memory request"]
SORT = ["memory request"]
OPERATION_TYPE = "ALL"


INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "median_memory.dat"
