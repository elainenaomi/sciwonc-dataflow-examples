HOST = "mongos-1sh-5niv:27017,mongos-1sh-82z7:27017,mongos-1sh-qktb:27017"
PORT = "27017"
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "median_cpu"
COLLECTION_OUTPUT = "ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ['median cpu']
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "task_google.csv"
OUTPUT_FILE = "ratio_cpu_memory.csv"
