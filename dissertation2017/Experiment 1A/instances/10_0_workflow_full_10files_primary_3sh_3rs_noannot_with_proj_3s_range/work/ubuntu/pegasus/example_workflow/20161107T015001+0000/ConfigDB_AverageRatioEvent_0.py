HOST = "ip-172-31-29-102.us-west-2.compute.internal:27017,ip-172-31-29-103.us-west-2.compute.internal:27017,ip-172-31-29-104.us-west-2.compute.internal:27017,ip-172-31-29-105.us-west-2.compute.internal:27017,ip-172-31-29-101.us-west-2.compute.internal:27017,ip-172-31-29-106.us-west-2.compute.internal:27017,ip-172-31-29-107.us-west-2.compute.internal:27017,ip-172-31-29-108.us-west-2.compute.internal:27017,ip-172-31-29-109.us-west-2.compute.internal:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googler"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "ratio"
COLLECTION_OUTPUT = "average_ratioevent"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "sds from all avg ratio"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "GROUP_BY_COLUMN"
COLUMN = "event type"
VALUE = ["2"]

INPUT_FILE = "ratio_cpu_memory.csv"
OUTPUT_FILE = "mean_ratio_cpu_memory_0.csv"
