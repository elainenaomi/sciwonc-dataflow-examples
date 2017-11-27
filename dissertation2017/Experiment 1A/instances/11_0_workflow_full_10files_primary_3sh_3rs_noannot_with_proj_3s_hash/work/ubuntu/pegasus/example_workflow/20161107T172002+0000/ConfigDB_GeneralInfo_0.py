HOST = "ip-172-31-29-102.us-west-2.compute.internal:27017,ip-172-31-29-103.us-west-2.compute.internal:27017,ip-172-31-29-104.us-west-2.compute.internal:27017,ip-172-31-29-105.us-west-2.compute.internal:27017,ip-172-31-29-101.us-west-2.compute.internal:27017,ip-172-31-29-106.us-west-2.compute.internal:27017,ip-172-31-29-107.us-west-2.compute.internal:27017,ip-172-31-29-108.us-west-2.compute.internal:27017,ip-172-31-29-109.us-west-2.compute.internal:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googleh"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "general_info"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["time", "job ID", "task index"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "task_events_0.dat"
OUTPUT_FILE = "general_info_0.dat"
