HOST = "172.31.28.89"
PORT = "5432"
USER = "postgres"
PASSWORD = "enw1989"
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "stats_cpumemory"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["CPU request", "memory request"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "ALL"


INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "stats_cpumemory_0.dat"
