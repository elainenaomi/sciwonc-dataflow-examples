HOST = "postgres-10f" 
PORT = "5432"
USER = "postgres"
PASSWORD = ""
DATABASE = "google"
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
