HOST = "mongos-3sh-ex4q:27017,mongos-3sh-lenv:27017,mongos-3sh-ql7j:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "ratio"
PREFIX_COLUMN = "g_"

FIRST_ITEM = {'numline':257154,'filepath':'part-00008-of-00500.csv.gz'}
LAST_ITEM = {'numline':289297,'filepath':'part-00009-of-00500.csv.gz'}
ATTRIBUTES = ["job ID", "task index", "event type","time", "memory request","CPU request"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "UNIT"

INPUT_FILE = "task_google.csv"
OUTPUT_FILE = "ratio_cpu_memory_8.csv"
