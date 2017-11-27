HOST = "172.31.28.140:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "average_ratioevent"
COLLECTION_OUTPUT = "analysis_ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "total cpu task","total memory task", "total balanced task"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "mean_ratio_cpu_memory.csv"
OUTPUT_FILE = "analysis_ratio_cpu_memory_0.csv"
