HOST = "172.31.28.89"
PORT = "5432"
USER = "postgres"
PASSWORD = "enw1989"
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "ratio"
PREFIX_COLUMN = "g_"

FIRST_ITEM = {'numline':192866,'filepath':'part-00006-of-00500.csv.gz'}
LAST_ITEM = {'numline':289297,'filepath':'part-00009-of-00500.csv.gz'}
ATTRIBUTES = ["job ID", "task index", "event type","time", "memory request","CPU request"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "UNIT"

INPUT_FILE = "task_google.csv"
OUTPUT_FILE = "ratio_cpu_memory_2.csv"
