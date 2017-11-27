HOST = "172.31.28.89"
PORT = "5432"
USER = "postgres"
PASSWORD = "enw1989"
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events_info"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "standard deviation memory", "standard deviation cpu","standard deviation ratio", "average memory", "average cpu","average ratio"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "GROUP_BY_COLUMN"
COLUMN = "event type"
VALUE = ["0","1","2","3","4","5","6","7","8"]

INPUT_FILE = "task_events_info_0.dat"
