HOST = "172.31.21.247"
PORT = "5432"
USER = "postgres"
PASSWORD = "enw1989"
DATABASE = "wiki"
COLLECTION_INPUT = "sessions"
COLLECTION_OUTPUT = "contributors"
PREFIX_COLUMN = "w_"

OUTPUT_FILE = "contributors.dat"
ATTRIBUTES = ["contributor_username"]
OPERATION_TYPE = "DISTINCT"
COLUMN = "contributor_username"

TOTAL_NODES = 1
TEMPLATE_NAME = "ConfigDB_SessionCompute.py"
