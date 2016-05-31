HOST = "postgres-10f"
PORT = "5432"
USER = "postgres"
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "ratio"
COLLECTION_OUTPUT = "average_ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "ratio cpu memory"]
SORT = ["filepath","numline"]
OPERATION_TYPE = "GROUP_BY_COLUMN"
COLUMN = "event type"
VALUE = ["6","7","8"]

INPUT_FILE = "ratio_cpu_memory.csv"
OUTPUT_FILE = "mean_ratio_cpu_memory_2.csv"
