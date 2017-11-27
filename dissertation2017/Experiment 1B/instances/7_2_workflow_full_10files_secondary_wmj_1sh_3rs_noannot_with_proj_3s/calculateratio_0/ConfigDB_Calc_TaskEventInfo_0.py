HOST = "wfSciwoncGW:enw1989@172.31.2.76:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googlew"
READ_PREFERENCE = "secondary"
WRITE_CONCERN = "majority"
COLLECTION_INPUT = "task_events_info"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "standard deviation memory", "standard deviation cpu","standard deviation ratio", "average memory", "average cpu","average ratio"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "GROUP_BY_COLUMN"
COLUMN = "event type"
VALUE = ["0","1","2","3","4","5","6","7","8"]

INPUT_FILE = "task_events_info_0.dat"
