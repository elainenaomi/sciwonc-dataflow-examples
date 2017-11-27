HOST = "172.31.28.89"
PORT = "5432"
USER = "postgres"
PASSWORD = "enw1989"
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "ratio"
COLLECTION_OUTPUT = "average_ratioevent"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "sds from all avg ratio"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "GROUP_BY_COLUMN"
COLUMN = "event type"
VALUE = ["4"]

INPUT_FILE = "ratio_cpu_memory.csv"
OUTPUT_FILE = "mean_ratio_cpu_memory_1.csv"
