#!/usr/bin/python
"""
Gera o tempo de execução das atividades réplicas considerando o tempo mais cedo e o tempo mais tarde obtido da lista de réplicas
"""
import psycopg2
import sys
import pprint

import numpy as np
from datetime import datetime
import time

def main():
    conn_string = "host='localhost' dbname='my_exp' user='postgres' password='enw1989'"
    # print the connection string we will use to connect
    print "Connecting to database\n	->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    query = "select workflow, execution, job, elapsed_time, resource, execution_time, terminated_time from stats order by workflow, execution, submit_time"
    cursor.execute(query)

    # retrieve the records from the database
    rows = cursor.fetchall()
    data = {}
    for row in rows:
        if row[0] not in data:
            data[row[0]] = {}
        if row[1] not in data[row[0]]:
            data[row[0]][row[1]] = []

        data[row[0]][row[1]].append(row)

    stats = {}
    # pprint.pprint(data)

    for workflow, executions in data.iteritems():
        # print workflow
        if workflow not in stats:
            stats[workflow] = {}

        for execution, rows in executions.iteritems():
            # print "\n" + execution

            doc = {}
            for row in rows:
                task = row[2].split("_")[0]
                # print task
                if task not in doc:
                    doc[task] = {}
                    doc[task]["start"] = None
                    doc[task]["end"] = None

                if doc[task]["start"] > row[5] or doc[task]["start"] is None:
                    doc[task]["start"] = row[5]

                if doc[task]["end"] < row[6] or doc[task]["end"] is None:
                    doc[task]["end"] = row[6]
            # print "\n\n",
            for task, times in sorted(doc.iteritems()):
                # print task
                # print times
                if task not in stats[workflow]:
                    stats[workflow][task] = {}

                if execution not in stats[workflow][task]:
                    stats[workflow][task][execution] = {}

                stats[workflow][task][execution] = times
                starttime = datetime.strptime(times["start"], '%Y-%m-%d %H:%M:%S')
                endtime = datetime.strptime(times["end"], '%Y-%m-%d %H:%M:%S')

                stats[workflow][task][execution]["duration"] = endtime - starttime

    # s1 = "2017-10-25 2:51:43"
    # s2 = "2017-10-25 2:57:15"
    # starttime = datetime.strptime(s1, '%Y-%m-%d %H:%M:%S')
    # endtime = datetime.strptime(s2, '%Y-%m-%d %H:%M:%S')
    # print (endtime - starttime).total_seconds() # 0:05:32, 332 "20161025T022606+0000"

    # pprint.pprint(stats)
    # mean + std

    for workflow, tasks in sorted(stats.iteritems()):
        # print "\n" + workflow

        for task, executions in sorted(tasks.iteritems()):
            # if task == "averageratioevent":
                # print "\n"+workflow, task,
            items = []
            for execution, times in executions.iteritems():
                # print "\n" + execution + " - ", (times["duration"]).total_seconds()
                # if task == "averageratioevent":
                    # print (times["duration"]).total_seconds(),
                # print times
                items.append((times["duration"]).total_seconds())

            a = np.array(items)
            m = np.mean(a)
            std = np.std(a)
            print workflow + "," + task + "," + str(m) + "," +str(round(std,3))+""


# a = np.array([[1, 2], [3, 4]])
# np.mean(a, axis=1)
# array([ 1.5,  3.5])
#
# np.std([1,3,4,6])
# 1.8027756377319946

    # date_object1 = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
    # print date_object1
    # date_object2 = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')
    # print date_object2
    # print date_object1 > date_object2
    # print row[5] < row[6]






if __name__ == "__main__":
	main()
