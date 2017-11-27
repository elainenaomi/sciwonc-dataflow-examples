HOST = "wfSciwoncGW:enw1989@172.31.25.253:27001,172.31.25.251:27001,172.31.2.76:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googlew"
READ_PREFERENCE = "secondary"
COLLECTION_INPUT = "stats_cpumemory"

PREFIX_COLUMN = ""

ATTRIBUTES = ["standard deviation cpu", "average cpu","standard deviation memory", "average memory","standard deviation ratio", "average ratio"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"
