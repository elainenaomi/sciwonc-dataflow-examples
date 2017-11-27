HOST = "ip-172-31-29-102.us-west-2.compute.internal:27017,ip-172-31-29-103.us-west-2.compute.internal:27017,ip-172-31-29-104.us-west-2.compute.internal:27017,ip-172-31-29-105.us-west-2.compute.internal:27017,ip-172-31-29-101.us-west-2.compute.internal:27017,ip-172-31-29-106.us-west-2.compute.internal:27017,ip-172-31-29-107.us-west-2.compute.internal:27017,ip-172-31-29-108.us-west-2.compute.internal:27017,ip-172-31-29-109.us-west-2.compute.internal:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googler"
READ_PREFERENCE = "primary"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "median_memory"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["memory request"]
SORT = ["memory request"]
OPERATION_TYPE = "ALL"


INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "median_memory.dat"
