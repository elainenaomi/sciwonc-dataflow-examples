HOST = "postgres-10f" 
PORT = "27017"
USER = "postgres"
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "maxmin_cpu"
COLLECTION_OUTPUT = "ratio"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["max cpu","min cpu"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "ALL"
