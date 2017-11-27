HOST = "172.31.28.89"
PORT = "5432"
USER = "postgres"
PASSWORD = "enw1989"
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "general_info"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["time", "job ID", "task index"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "task_events_0.dat"
OUTPUT_FILE = "general_info_0.dat"
