HOST = "postgres-10f" 
PORT = "27017"
USER = "postgres"
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["job ID", "task index", "event type","time", "memory request","CPU request"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "task_google.csv"
OUTPUT_FILE = "ratio_cpu_memory.csv"
