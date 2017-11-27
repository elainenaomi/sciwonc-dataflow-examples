HOST = "wfSciwoncGW:enw1989@172.31.25.253:27001,172.31.25.251:27001,172.31.2.76:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googlew"
READ_PREFERENCE = "secondary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "stats_cpumemory"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["CPU request", "memory request"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"


INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "stats_cpumemory_0.dat"
