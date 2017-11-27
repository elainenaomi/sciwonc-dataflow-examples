HOST = "wfSciwoncWiki:enw1989@172.31.2.76:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "wiki"

READ_PREFERENCE = "secondary"
WRITE_CONCERN = "majority"

COLLECTION_INPUT = "sessions"
COLLECTION_OUTPUT = "contributors"
PREFIX_COLUMN = "w_"

OUTPUT_FILE = "contributors.dat"

OPERATION_TYPE = "DISTINCT"
COLUMN = "contributor_username"

TOTAL_NODES = 1
TEMPLATE_NAME = "ConfigDB_SessionCompute.py"
