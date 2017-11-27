HOST = "wfSciwoncGW:enw1989@172.31.2.76:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googlew"
READ_PREFERENCE = "secondary"
WRITE_CONCERN = "majority"
COLLECTION_INPUT = "average_ratioevent"
COLLECTION_OUTPUT = "analysis_ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "total cpu task","total memory task", "total balanced task"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "mean_ratio_cpu_memory.csv"
OUTPUT_FILE = "analysis_ratio_cpu_memory_0.csv"
