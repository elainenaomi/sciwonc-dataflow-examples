#!/usr/bin/env python
from pymongo import MongoClient
import pymongo

HOST = "ec2-54-244-59-9.us-west-2.compute.amazonaws.com:27017"
c = MongoClient('mongodb://'+HOST)

dbname = "googlew"

task = "task_events"
ginfo = "general_info"
statscpumemory = "stats_cpumemory"
mediancpu = "median_cpu"
medianmemory = "median_memory"
tinfo = "task_events_info"
ratio = "ratio"
avgratio = "average_ratioevent"
analysis = "analysis_ratio"

db = c[dbname]
task_col = db[task]
ginfo_col = db[ginfo]
statscpumemory_col = db[statscpumemory]
mediancpu_col = db[mediancpu]
medianmemory_col = db[medianmemory]
tinfo_col = db[tinfo]
ratio_col = db[ratio]
avgratio_col = db[avgratio]
analysis_col = db[analysis]

# write a file

output = []

######################################
task_events_count = task_col.count()

newLine = "Task Events:\t" + str(task_events_count) + "\t"

if task_events_count == 2892970:
    newLine = newLine + "Ok"
else:
    newLine = newLine + "Error"

output.append(newLine+"\n")

######################################
ginfo_count = ginfo_col.count()

newLine = "General Info Count:\t" + str(task_events_count) + "\t"
if ginfo_count == 1:
    newLine = newLine + "Ok"
else:
    newLine = newLine + "Error"

output.append(newLine+"\n")


cursor = ginfo_col.find()

for doc in cursor:
    if doc['interval seconds'] == 1934322.504095 and doc['min timestamp'] == 561854551050.0 and doc['max timestamp'] == 2496177055145.0 and doc['total items'] ==  2892970:
        newLine = "General Info:\tStats\tOk"
    else:
        newLine = "General Info:\tStats\tError"
output.append(newLine+"\n")

######################################
statscpumemory_count = statscpumemory_col.count()

newLine = "Stats CPU Memory Info Count:\t" + str(statscpumemory_count) + "\t"
if statscpumemory_count == 1:
    newLine = newLine + "Ok"
else:
    newLine = newLine + "Error"

output.append(newLine+"\n")


cursor = statscpumemory_col.find()

for doc in cursor:

	if \
        round(doc["sum cpu"],2) == round(99321.2426834434,2)   and \
        round(doc["sum ratio"],2) == round(5453800.668569512,2)   and \
        round(doc["variance cpu"],2) == round(0.0007348989990335962,2)   and \
        round(doc["average ratio"],2) == round(1.8851908829229171,2)   and \
        round(doc["sum variance cpu"],2) == round(2126.040757234223,2)   and \
        round(doc["standard deviation ratio"],2) == round(2.641234096618789,2)   and \
        round(doc["sum variance ratio"],2) == round(20181698.79771226,2)   and \
        round(doc["total tasks"],2) == round(2892970,2)   and \
        round(doc["average cpu"],2) == round(0.03433192970664867,2)   and \
        round(doc["standard deviation cpu"],2) == round(0.027109020621069957,2)   and \
        round(doc["sum memory"],2) == round(79295.72718423756,2)   and \
        round(doc["variance ratio"],2) == round(6.976117553141671,2)   and \
        round(doc["variance memory"],2) == round(0.0006540568268376541,2)   and \
        round(doc["sum variance memory"],2) == round(1892.1667783365283,2)   and \
        round(doc["average memory"],2) == round(0.027409799335712973,2)   and \
        round(doc["total valid tasks"],2) == round(2892970,2)   and \
        round(doc["standard deviation memory"],2) == round(0.02557453473355193,2):
            newLine = "Stats CPU Memory Info:\tStats\tOk"
        else:
            newLine = "Stats CPU Memory Info:\tStats\tError"

output.append(newLine+"\n")


######################################
count = mediancpu_col.count()

newLine = "Median CPU Count:\t" + str(count) + "\t"
if count == 1:
    newLine = newLine + "Ok"
else:
    newLine = newLine + "Error"

output.append(newLine+"\n")

cursor = mediancpu_col.find()

for doc in cursor:
    if doc["median cpu"] == 0.0614:
        newLine = "Median CPU Info:\tStats\tOk"
    else:
        newLine = "Median CPU Info:\tStats\tError"

output.append(newLine+"\n")

######################################
count = medianmemory_col.count()

newLine = "Median Memory Count:\t" + str(count) + "\t"
if count == 1:
    newLine = newLine + "Ok"
else:
    newLine = newLine + "Error"

output.append(newLine+"\n")

cursor = medianmemory_col.find()

for doc in cursor:
    if doc["median memory"] == 0.02386:
        newLine = "Median Memory Info:\tStats\tOk"
    else:
        newLine = "Median Memory Info:\tStats\tError"

output.append(newLine+"\n")

######################################

count = tinfo_col.count()

newLine = "Task Event Count:\t" + str(count) + "\t"
if count == 9:
    newLine = newLine + "Ok"
else:
    newLine = newLine + "Error"

output.append(newLine+"\n")

cursor = tinfo_col.find()

for doc in cursor:

    if doc['event type'] == "0":
        if \
            round(doc["sum cpu"],2) == round(33633.10060121667,2) and \
            round(doc["sum ratio"],2) == round(1802089.1624027935,2) and \
            round(doc["sds from avg cpu"],2) == round(0.018126711338001093,2) and \
            round(doc["variance cpu"],2) == round(0.0007234390834477359,2) and \
            round(doc["average cpu"],2) == round(0.03482332709810272,2) and \
            round(doc["total tasks"],2) == round(965821,2) and \
            round(doc["standard deviation ratio"],2) == round(2.629807956261423,2) and \
            round(doc["variance memory"],2) == round(0.0006009846225456817,2) and \
            round(doc["average ratio"],2) == round(1.8658624759689357,2) and \
            round(doc["standard deviation cpu"],2) == round(0.02689682292479422,2) and \
            round(doc["sum memory"],2) == round(26151.92796249314,2) and \
            round(doc["standard deviation memory"],2) == round(0.02451498771253377,2) and \
            round(doc["sds from avg memory"],2) == round(-0.012997018127261048,2) and \
            round(doc["total valid tasks"],2) == round(965821,2) and \
            round(doc["average memory"],2) == round(0.02707740664418473,2) and \
            round(doc["percentagem from total"],2) == round(299.5347999266945,2) and \
            round(doc["variance ratio"],2) == round(6.915889886815883,2) and \
            round(doc["sds from avg ratio"],2) == round(-0.007317945417532256,2):
                newLine = "Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Event "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if doc['event type'] == "1":
        if \
            round(doc["sum cpu"],2) == round(30555.448235223972,2) and \
            round(doc["sum ratio"],2) == round(1723700.5983060386,2) and \
            round(doc["sds from avg cpu"],2) == round(-0.04672211541707625,2) and \
            round(doc["variance cpu"],2) == round(0.000736664879204348,2) and \
            round(doc["average cpu"],2) == round(0.03306533891634714,2) and \
            round(doc["total tasks"],2) == round(924093,2) and \
            round(doc["standard deviation ratio"],2) == round(2.6840428478214626,2) and \
            round(doc["variance memory"],2) == round(0.0006529499516169935,2) and \
            round(doc["average ratio"],2) == round(1.8652890978570758,2) and \
            round(doc["standard deviation cpu"],2) == round(0.027141571052618677,2) and \
            round(doc["sum memory"],2) == round(25136.374621630795,2) and \
            round(doc["standard deviation memory"],2) == round(0.025552885387309855,2) and \
            round(doc["sds from avg memory"],2) == round(-0.008159228541852397,2) and \
            round(doc["total valid tasks"],2) == round(924093,2) and \
            round(doc["average memory"],2) == round(0.02720113086197038,2) and \
            round(doc["percentagem from total"],2) == round(313.0604820077633,2) and \
            round(doc["variance ratio"],2) == round(7.204086008941546,2) and \
            round(doc["sds from avg ratio"],2) == round(-0.007535032616502615,2):
                newLine = "Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Event "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if doc['event type'] == "2":
        if \
            round(doc["sum cpu"],2) == round(4920.120424400018,2) and \
            round(doc["sum ratio"],2) == round(203751.51073738385,2) and \
            round(doc["sds from avg cpu"],2) == round(0.09353374988528587,2) and \
            round(doc["variance cpu"],2) == round(0.0006855492365195038,2) and \
            round(doc["average cpu"],2) == round(0.03686753806105488,2) and \
            round(doc["total tasks"],2) == round(133454,2) and \
            round(doc["standard deviation ratio"],2) == round(4.361427599387985,2) and \
            round(doc["variance memory"],2) == round(0.0005419691576323096,2) and \
            round(doc["average ratio"],2) == round(1.5267546176014497,2) and \
            round(doc["standard deviation cpu"],2) == round(0.026182995178541047,2) and \
            round(doc["sum memory"],2) == round(4116.44618897074,2) and \
            round(doc["standard deviation memory"],2) == round(0.023280231047657356,2) and \
            round(doc["sds from avg memory"],2) == round(0.13433800466101967,2) and \
            round(doc["total valid tasks"],2) == round(133454,2) and \
            round(doc["average memory"],2) == round(0.030845431301952282,2) and \
            round(doc["percentagem from total"],2) == round(2167.7656720667796,2) and \
            round(doc["variance ratio"],2) == round(19.022050704703247,2) and \
            round(doc["sds from avg ratio"],2) == round(-0.1357078745046963,2):
                newLine = "Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Event "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if doc['event type'] == "3":
        if \
            round(doc["sum cpu"],2) == round(1816.3366382018626,2) and \
            round(doc["sum ratio"],2) == round(84267.1339540883,2) and \
            round(doc["sds from avg cpu"],2) == round(-0.3300538475348598,2) and \
            round(doc["variance cpu"],2) == round(0.0007916594279041643,2) and \
            round(doc["average cpu"],2) == round(0.025384493147762675,2) and \
            round(doc["total tasks"],2) == round(71553,2) and \
            round(doc["standard deviation ratio"],2) == round(1.5515381014722032,2) and \
            round(doc["variance memory"],2) == round(0.000755413830760473,2) and \
            round(doc["average ratio"],2) == round(1.1776883422650106,2) and \
            round(doc["standard deviation cpu"],2) == round(0.028136443057077493,2) and \
            round(doc["sum memory"],2) == round(1910.7759991862274,2) and \
            round(doc["standard deviation memory"],2) == round(0.027484792718164584,2) and \
            round(doc["sds from avg memory"],2) == round(-0.027584248295410823,2) and \
            round(doc["total valid tasks"],2) == round(71553,2) and \
            round(doc["average memory"],2) == round(0.02670434501958307,2) and \
            round(doc["percentagem from total"],2) == round(4043.114893854905,2) and \
            round(doc["variance ratio"],2) == round(2.4072704803199687,2) and \
            round(doc["sds from avg ratio"],2) == round(-0.2678681687335573,2):
                newLine = "Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Event "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if doc['event type'] == "4":
        if \
            round(doc["sum cpu"],2) == round(13290.871623892393,2) and \
            round(doc["sum ratio"],2) == round(844391.3224762151,2) and \
            round(doc["sds from avg cpu"],2) == round(-0.1494441493958755,2) and \
            round(doc["variance cpu"],2) == round(0.0007838896062906944,2) and \
            round(doc["average cpu"],2) == round(0.03028064517897762,2) and \
            round(doc["total tasks"],2) == round(438923,2) and \
            round(doc["standard deviation ratio"],2) == round(2.433745183191664,2) and \
            round(doc["variance memory"],2) == round(0.0007719618269364068,2) and \
            round(doc["average ratio"],2) == round(1.923780076405691,2) and \
            round(doc["standard deviation cpu"],2) == round(0.02799802861436309,2) and \
            round(doc["sum memory"],2) == round(12125.415444747849,2) and \
            round(doc["standard deviation memory"],2) == round(0.027784201031096915,2) and \
            round(doc["sds from avg memory"],2) == round(0.008429574236627164,2) and \
            round(doc["total valid tasks"],2) == round(438923,2) and \
            round(doc["average memory"],2) == round(0.02762538177481665,2) and \
            round(doc["percentagem from total"],2) == round(659.10649476104,2) and \
            round(doc["variance ratio"],2) == round(5.923115616708627,2) and \
            round(doc["sds from avg ratio"],2) == round(0.014610289005497188,2):
                newLine = "Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Event "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if doc['event type'] == "5":
        if \
            round(doc["sum cpu"],2) == round(10663.06460830491,2) and \
            round(doc["sum ratio"],2) == round(561062.8211971126,2) and \
            round(doc["sds from avg cpu"],2) == round(0.12043620613237489,2) and \
            round(doc["variance cpu"],2) == round(0.0006242763568776912,2) and \
            round(doc["average cpu"],2) == round(0.03759683730221465,2) and \
            round(doc["total tasks"],2) == round(283616,2) and \
            round(doc["standard deviation ratio"],2) == round(2.1678297120424634,2) and \
            round(doc["variance memory"],2) == round(0.0008252846374609808,2) and \
            round(doc["average ratio"],2) == round(1.9782481284451954,2) and \
            round(doc["standard deviation cpu"],2) == round(0.02498552294585189,2) and \
            round(doc["sum memory"],2) == round(8423.57429574846,2) and \
            round(doc["standard deviation memory"],2) == round(0.0287277677075853,2) and \
            round(doc["sds from avg memory"],2) == round(0.0895747336484838,2) and \
            round(doc["total valid tasks"],2) == round(283616,2) and \
            round(doc["average memory"],2) == round(0.029700631472654785,2) and \
            round(doc["percentagem from total"],2) == round(1020.0306047613675,2) and \
            round(doc["variance ratio"],2) == round(4.69948566041411,2) and \
            round(doc["sds from avg ratio"],2) == round(0.035232486829322215,2):
                newLine = "Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Event "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")
    if doc['event type'] == "6":
        if \
            round(doc["sum cpu"],2) == round(0,2) and \
            round(doc["sum ratio"],2) == round(0,2) and \
            round(doc["sds from avg cpu"],2) == round(-1.2664393224137669,2) and \
            doc["variance cpu"] == None and \
            round(doc["average cpu"],2) == round(0,2) and \
            round(doc["total tasks"],2) == round(0,2) and \
            doc["standard deviation ratio"] == None and \
            doc["variance memory"] == None and \
            round(doc["average ratio"],2) == round(0,2) and \
            doc["standard deviation cpu"] == None and \
            round(doc["sum memory"],2) == round(0,2) and \
            doc["standard deviation memory"] == None and \
            round(doc["sds from avg memory"],2) == round(-1.0717614072467683,2) and \
            round(doc["total valid tasks"],2) == round(0,2) and \
            round(doc["average memory"],2) == round(0,2) and \
            doc["percentagem from total"] == None and \
            doc["variance ratio"] == None and \
            round(doc["sds from avg ratio"],2) == round(-0.7137538036996681,2):
                newLine = "Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Event "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")


    if doc['event type'] == "7":
        if \
            round(doc["sum cpu"],2) == round(9.09282399999999,2) and \
            round(doc["sum ratio"],2) == round(552.696728552374,2) and \
            round(doc["sds from avg cpu"],2) == round(0.617925355046136,2) and \
            round(doc["variance cpu"],2) == round(0.00030433619202221946,2) and \
            round(doc["average cpu"],2) == round(0.05108328089887634,2) and \
            round(doc["total tasks"],2) == round(178,2) and \
            round(doc["standard deviation ratio"],2) == round(0.7092106358581964,2) and \
            round(doc["variance memory"],2) == round(0.000013245274855352863,2) and \
            round(doc["average ratio"],2) == round(3.1050378008560338,2) and \
            round(doc["standard deviation cpu"],2) == round(0.017445234077598945,2) and \
            round(doc["sum memory"],2) == round(2.8115789999999983,2) and \
            round(doc["standard deviation memory"],2) == round(0.003639405838231409,2) and \
            round(doc["sds from avg memory"],2) == round(-0.4541397064020204,2) and \
            round(doc["total valid tasks"],2) == round(178,2) and \
            round(doc["average memory"],2) == round(0.015795387640449427,2) and \
            round(doc["percentagem from total"],2) == round(1625264.0449438202,2) and \
            round(doc["variance ratio"],2) == round(0.5029797260143872,2) and \
            round(doc["sds from avg ratio"],2) == round(0.4618473309483321,2):
                newLine = "Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Event "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if doc['event type'] == "8":
        if \
            round(doc["sum cpu"],2) == round(4433.207727996908,2) and \
            round(doc["sum ratio"],2) == round(233985.42277147647,2) and \
            round(doc["sds from avg cpu"],2) == round(0.9043853853930378,2) and \
            round(doc["variance cpu"],2) == round(0.0001780149751221565,2) and \
            round(doc["average cpu"],2) == round(0.05884893176866283,2) and \
            round(doc["total tasks"],2) == round(75332,2) and \
            round(doc["standard deviation ratio"],2) == round(0.6522459265999301,2) and \
            round(doc["variance memory"],2) == round(0.000005192139433844148,2) and \
            round(doc["average ratio"],2) == round(3.106056161677328,2) and \
            round(doc["standard deviation cpu"],2) == round(0.013342225268753203,2) and \
            round(doc["sum memory"],2) == round(1428.401093998356,2) and \
            round(doc["standard deviation memory"],2) == round(0.002278626655212334,2) and \
            round(doc["sds from avg memory"],2) == round(-0.3303437327213998,2) and \
            round(doc["total valid tasks"],2) == round(75332,2) and \
            round(doc["average memory"],2) == round(0.01896141206921834,2) and \
            round(doc["percentagem from total"],2) == round(3840.2936335156373,2) and \
            round(doc["variance ratio"],2) == round(0.42542474876620134,2) and \
            round(doc["sds from avg ratio"],2) == round(0.46223289344830054,2):
                newLine = "Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Event "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

######################################
count = ratio_col.count()

newLine = "Ratio Count:\t" + str(count) + "\t"
if count == 643930:
    newLine = newLine + "Ok"
else:
    newLine = newLine + "Error"

output.append(newLine+"\n")

######################################
count = avgratio_col.count()

newLine = "Average Ratio Event Count:\t" + str(count) + "\t"
if count == 4:
    newLine = newLine + "Ok"
else:
    newLine = newLine + "Error"

output.append(newLine+"\n")


cursor = avgratio_col.find()

for doc in cursor:
    if doc["event type"] == "2":
        if \
            doc["total cpu task"] == 12084 and \
            doc["event type"] == "2" and \
            doc["total balanced task"] == 102022 and \
            doc["total memory task"] == 19348:
                newLine = "Average Ratio Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Average Ratio Event  "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if doc["event type"] == "3":
        if \
            doc["total cpu task"] == 4104 and \
            doc["event type"] == "3" and \
            doc["total balanced task"] == 58466 and \
            doc["total memory task"] == 8983:
                newLine = "Average Ratio Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Average Ratio Event  "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if doc["event type"] == "4":
        if \
            doc["total cpu task"] == 70448 and \
            doc["event type"] == "4" and \
            doc["total balanced task"] == 290306 and \
            doc["total memory task"] == 78169:
                newLine = "Average Ratio Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Average Ratio Event  "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if doc["event type"] == "6":
        if \
            doc["total cpu task"] == 0 and \
            doc["event type"] == "6" and \
            doc["total balanced task"] == 0 and \
            doc["total memory task"] == 0:
                newLine = "Average Ratio Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Average Ratio Event  "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

######################################
count = analysis_col.count()

newLine = "Analysis Count:\t" + str(count) + "\t"
if count == 5:
    newLine = newLine + "Ok"
else:
    newLine = newLine + "Error"

output.append(newLine+"\n")

cursor = analysis_col.find()

for doc in cursor:
    if "event type" in doc and doc["event type"] == "2":
        if \
            doc["total task type"] == 102022 and \
            doc["event type"] == "2" and \
            doc["task type"] == "balanced":
                newLine = "Analysis Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Analysis Event  "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if "event type" in doc and doc["event type"] == "3":
        if \
            doc["total task type"] == 58466 and \
            doc["event type"] == "3" and \
            doc["task type"] == "balanced":
                newLine = "Analysis Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Analysis Event  "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if "event type" in doc and doc["event type"] == "4":
        if \
            doc["total task type"] == 290306 and \
            doc["event type"] == "4" and \
            doc["task type"] == "balanced":
                newLine = "Analysis Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Analysis Event  "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if "event type" in doc and doc["event type"] == "6":
        if \
            doc["total task type"] == 0 and \
            doc["event type"] == "6" and \
            doc["task type"] == "balanced":
                newLine = "Analysis Event "+doc['event type']+ " Info:\tStats\tOk"
        else:
                newLine = "Analysis Event  "+doc['event type']+ " Info:\tStats\tError"

        output.append(newLine+"\n")

    if "general type" in doc and doc["general type"]== "all":
        if \
            doc["task type"] == "balanced" and \
            doc["general type"] == "all" and \
            doc["total task type"] == 450794:
                newLine = "Analysis General Type Info:\tStats\tOk"
        else:
                newLine = "Analysis  General Type Info:\tStats\tError"

        output.append(newLine+"\n")




######################################

import os
from datetime import datetime

workflow_folder_name = os.getcwd().split('/')[-2]

strtime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename_stats = strtime + "_" + workflow_folder_name + ".txt"

fi = open(filename_stats, "w")
fi.writelines(output)
fi.close()
