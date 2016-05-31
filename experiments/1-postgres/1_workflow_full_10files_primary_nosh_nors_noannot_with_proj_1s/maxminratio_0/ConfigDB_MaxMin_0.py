HOST = "postgres-10f" 
PORT = "27017"
USER = "postgres"
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "average_ratio"
COLLECTION_OUTPUT = "analysis_ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["event type", "mean ratio cpu memory"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "ALL"

INPUT_FILE = "mean_ratio_cpu_memory.csv"
OUTPUT_FILE = "analysis_ratio_cpu_memory_0.csv"
