HOST = "172.31.28.89"
PORT = "5432"
USER = "postgres"
PASSWORD = "enw1989"
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "stats_cpumemory"
COLLECTION_OUTPUT = "ratio"

PREFIX_COLUMN = "g_"

ATTRIBUTES = ["standard deviation cpu", "average cpu","standard deviation memory", "average memory","standard deviation ratio", "average ratio"]
SORT = ["filepath", "numline"]
OPERATION_TYPE = "ALL"
