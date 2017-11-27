HOST = "ip-172-31-29-102.us-west-2.compute.internal:27017,ip-172-31-29-103.us-west-2.compute.internal:27017,ip-172-31-29-104.us-west-2.compute.internal:27017,ip-172-31-29-105.us-west-2.compute.internal:27017,ip-172-31-29-101.us-west-2.compute.internal:27017,ip-172-31-29-106.us-west-2.compute.internal:27017,ip-172-31-29-107.us-west-2.compute.internal:27017,ip-172-31-29-108.us-west-2.compute.internal:27017,ip-172-31-29-109.us-west-2.compute.internal:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "googler"
READ_PREFERENCE = "secondary"
COLLECTION_INPUT = "stats_cpumemory"

PREFIX_COLUMN = ""

ATTRIBUTES = ["standard deviation cpu", "average cpu","standard deviation memory", "average memory","standard deviation ratio", "average ratio"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"
