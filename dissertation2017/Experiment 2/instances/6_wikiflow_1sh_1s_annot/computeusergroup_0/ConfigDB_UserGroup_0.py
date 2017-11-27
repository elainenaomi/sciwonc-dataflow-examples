HOST = "wfSciwoncWiki:enw1989@172.31.28.140:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "wiki"
COLLECTION_INPUT = "sessions"
COLLECTION_OUTPUT = "contributors"
PREFIX_COLUMN = "w_"

OUTPUT_FILE = "contributors.dat"

OPERATION_TYPE = "DISTINCT"
COLUMN = "contributor_username"

TOTAL_NODES = 3
TEMPLATE_NAME = "ConfigDB_SessionCompute.py"
