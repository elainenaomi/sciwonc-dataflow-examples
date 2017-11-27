HOST = "ip-172-31-29-102.us-west-2.compute.internal:27017,ip-172-31-29-103.us-west-2.compute.internal:27017,ip-172-31-29-104.us-west-2.compute.internal:27017,ip-172-31-29-105.us-west-2.compute.internal:27017,ip-172-31-29-101.us-west-2.compute.internal:27017,ip-172-31-29-106.us-west-2.compute.internal:27017,ip-172-31-29-107.us-west-2.compute.internal:27017,ip-172-31-29-108.us-west-2.compute.internal:27017,ip-172-31-29-109.us-west-2.compute.internal:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googleh"
READ_PREFERENCE = "secondary"
READ_PREFERENCE = "secondary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "median_cpu"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["CPU request"]
SORT = ["CPU request"]
OPERATION_TYPE = "ALL"


INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "median_cpu.dat"
