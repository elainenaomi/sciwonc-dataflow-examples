#!/usr/bin/env python

# script para gerar os bancos de dados

import sys, getopt
import os
import os.path
import csv
import gzip


# It will connect to DataStoreClient
from sciwonc.dataflow.DataStoreClient import DataStoreClient
import ConfigCSVGZ_ImportTask_2
import ConfigDB_ImportTask_2

# connector and config
clientCSV = DataStoreClient("csv.gz", ConfigCSVGZ_ImportTask_2)
data = clientCSV.getData() # return an array of docs (like a csv reader)





def main():


	line = 1
	docs = []

	if(data):
		for c in data:
			output = c.getData()
			print output['filename']
			#print output['data']

			clientOutput = DataStoreClient("mongodb", ConfigDB_ImportTask_2)
			clientOutput.saveData(output["data"], output["filename"])


if __name__ == "__main__":
	main()
