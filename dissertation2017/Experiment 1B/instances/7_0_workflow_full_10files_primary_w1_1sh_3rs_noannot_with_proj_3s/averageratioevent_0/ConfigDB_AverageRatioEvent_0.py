HOST = "wfSciwoncGW:enw1989@172.31.2.76:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googlew"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "ratio"
COLLECTION_OUTPUT = "average_ratioevent"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "sds from all avg ratio"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "GROUP_BY_COLUMN"
COLUMN = "event type"
VALUE = ["2","3","4","6"]

INPUT_FILE = "ratio_cpu_memory.csv"
OUTPUT_FILE = "mean_ratio_cpu_memory_0.csv"
