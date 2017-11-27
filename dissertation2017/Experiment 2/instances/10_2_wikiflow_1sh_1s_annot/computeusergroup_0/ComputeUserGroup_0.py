#!/usr/bin/env python
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigDB_UserGroup_0

import re
import json

# connector and config
client = DataStoreClient("mongodb", ConfigDB_UserGroup_0)

# according to config
data = client.getData() # return an array of docs (like a csv reader)

output = []
contributors = []
if(data):
    # processing
    while True:
        doc = data.next()

        if doc is None:
            break;
        print doc
        if doc["_id"]:        
            contributor_username =  doc["_id"]
            contributors.append(contributor_username)
            output.append({"contributor_username": contributor_username})

    if output:
        clientOutput = DataStoreClient("mongodb", ConfigDB_UserGroup_0)
        clientOutput.saveData(output)

MAX_GROUPS = 10000

total_groups = min(MAX_GROUPS,len(output))

total_nodes = ConfigDB_UserGroup_0.TOTAL_NODES
template_filename = ConfigDB_UserGroup_0.TEMPLATE_NAME
total_groups_per_node = total_groups // total_nodes
remain_groups = total_groups % total_nodes

print "\n"
print "MAX : ", MAX_GROUPS
print "output size: ", len(output)
print "groups: ",total_groups
print "nodes: ",total_nodes
print "groups per node: ", total_groups_per_node
print "remain groups: ",remain_groups
print "\n"

initial = 0

for iterator_group in range(0, total_nodes):

    additional_groups = 1 if remain_groups > 0 else 0 
    remain_groups -= 1

    # save the total of groups in a array
    # split according to the total of nodes
    # generate the file
    f = """HOST = "wfSciwoncWiki:enw1989@172.31.29.101:27001,172.31.29.102:27001,172.31.29.103:27001,172.31.29.104:27001,172.31.29.105:27001,172.31.29.106:27001,172.31.29.107:27001,172.31.29.108:27001,172.31.29.109:27001/?authSource=admin"
PORT = ""
USER = ""
PASSWORD = ""
DATABASE = "wiki"
READ_PREFERENCE = "secondary"
WRITE_CONCERN = "majority"

COLLECTION_INPUT = "sessions"
COLLECTION_OUTPUT = "user_sessions"
PREFIX_COLUMN = "w_"

ATTRIBUTES = ["timestamp", "contributor_username"]
SORT = ["timestamp"]
OPERATION_TYPE = "GROUP_BY_COLUMN"
COLUMN = "contributor_username"
VALUE = """
    
    print "\n Iterating"
    print initial
    
    size_group = total_groups_per_node + additional_groups
    print initial+size_group
    groups = [ json.dumps(group) for group in contributors[initial: (initial+size_group)] ]
    initial += size_group

    # str_groups = str(groups).replace("'\"", "\"").replace("\"'", "\"")
    str_groups = str(groups)
    str_groups = re.sub(r'(?<!\\)\'"', r'"', str_groups)
    str_groups = re.sub(r'"\'', r'"', str_groups)
    str_groups = re.sub(r'\\\\"',r'\\"',str_groups)
    str_groups = re.sub(r'\\\'',r"'",str_groups)
    str_groups = re.sub(r'\\"(?=,)', r'\\\\"', str_groups)
    str_groups = re.sub(r'(?<=\[)"', r'u"', str_groups)
    str_groups = re.sub(r'", "', r'", u"', str_groups)
    str_groups = re.sub(r'\\\\u(?!ser)', r'\\u', str_groups)
    str_groups = re.sub(r'(?!\w)\\\\\\\\(?=\w")', r'\\\\', str_groups)


    f += str_groups
    f +="""

INPUT_FILE = "session"
OUTPUT_FILE = "user_"""

    f += str(iterator_group) + '"'

    filename = template_filename.replace(".py","_"+str(iterator_group)+".py")
    with open(filename, 'w') as writer:
        writer.write(f)
