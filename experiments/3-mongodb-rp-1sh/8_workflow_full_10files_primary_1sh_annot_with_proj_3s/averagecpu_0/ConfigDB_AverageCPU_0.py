HOST = "mongos-1sh-5niv:27017,mongos-1sh-82z7:27017,mongos-1sh-qktb:27017"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "google"
READ_PREFERENCE = "primary"
COLLECTION_INPUT = "task_events"
COLLECTION_OUTPUT = "average_cpu"
PREFIX_COLUMN = "g_"

ATTRIBUTES = ["CPU request"]
SORT = ["_id.filepath", "_id.numline"]
OPERATION_TYPE = "ALL"


INPUT_FILE = "task_events.dat"
OUTPUT_FILE = "average_cpu.dat"
