HOST = "172.31.28.140:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events_info"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "standard deviation memory", "standard deviation cpu","standard deviation ratio", "average memory", "average cpu","average ratio"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "GROUP_BY_COLUMN"
COLUMN = "event type"
VALUE = ["0","1","2","3","4","5","6","7","8"]

INPUT_FILE = "task_events_info_0.dat"
