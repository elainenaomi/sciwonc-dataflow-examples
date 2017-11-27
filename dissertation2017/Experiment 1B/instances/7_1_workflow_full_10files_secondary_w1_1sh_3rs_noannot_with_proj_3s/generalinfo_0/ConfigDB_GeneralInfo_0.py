HOST = "wfSciwoncGW:enw1989@172.31.2.76:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googlew"
READ_PREFERENCE = "secondary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "general_info"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["time", "job ID", "task index"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "task_events_0.dat"
OUTPUT_FILE = "general_info_0.dat"
