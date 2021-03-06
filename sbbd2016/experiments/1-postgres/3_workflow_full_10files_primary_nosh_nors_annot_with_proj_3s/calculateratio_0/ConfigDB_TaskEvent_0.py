HOST = "postgres-10f" 
PORT = "5432"
USER = "postgres"
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "ratio"
PREFIX_COLUMN = "g_"

FIRST_ITEM = {'numline':1,'filepath':'part-00000-of-00500.csv.gz'}
LAST_ITEM = {'numline':96433,'filepath':'part-00003-of-00500.csv.gz'}
ATTRIBUTES = ["job ID", "task index", "event type","time", "memory request","CPU request"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "UNIT"

INPUT_FILE = "task_google.csv"
OUTPUT_FILE = "ratio_cpu_memory_0.csv"
