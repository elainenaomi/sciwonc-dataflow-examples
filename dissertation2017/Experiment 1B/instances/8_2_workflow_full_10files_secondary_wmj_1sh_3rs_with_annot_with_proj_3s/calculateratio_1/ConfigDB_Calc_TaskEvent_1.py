HOST = "wfSciwoncGW:enw1989@172.31.25.253:27001,172.31.25.251:27001,172.31.2.76:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googlew"
READ_PREFERENCE = "secondary"
WRITE_CONCERN = "majority"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "ratio"
PREFIX_COLUMN = "g_"

FIRST_ITEM = {'numline':96434,'filepath':'part-00003-of-00500.csv.gz'}
LAST_ITEM = {'numline':192865,'filepath':'part-00006-of-00500.csv.gz'}
ATTRIBUTES = ["job ID", "task index", "event type","time", "memory request","CPU request"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "UNIT"

INPUT_FILE = "task_googlew.csv"
OUTPUT_FILE = "ratio_cpu_memory_1.csv"
