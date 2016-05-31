HOST = "postgres-10f" 
PORT = "5432"
USER = "postgres"
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "average_cpu"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["CPU request"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "ALL"


INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "average_cpu.dat"
