HOST = "wfSciwoncGW:enw1989@172.31.28.140:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googlew"
READ_PREFERENCE = "primary"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "median_cpu"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["CPU request"]
SORT = ["CPU request"]
OPERATION_TYPE = "ALL"


INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "median_cpu.dat"
