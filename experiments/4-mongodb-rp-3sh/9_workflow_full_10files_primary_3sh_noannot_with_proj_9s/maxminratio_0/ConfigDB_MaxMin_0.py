HOST = "mongos-3sh-ex4q:27017,mongos-3sh-lenv:27017,mongos-3sh-ql7j:27017"
PORT = "27017"
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "average_ratio"
COLLECTION_OUTPUT = "analysis_ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "mean ratio cpu memory"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "mean_ratio_cpu_memory.csv"
OUTPUT_FILE = "analysis_ratio_cpu_memory_0.csv"
