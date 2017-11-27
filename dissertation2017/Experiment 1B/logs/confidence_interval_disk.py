    #!/usr/bin/python

import os
import statistics
import pprint
import numpy as np
import scipy as sp
import scipy.stats
import math

#####################################################
def hms_to_seconds(t):
    h, m, s = [int(i) for i in t.split(':')]
    return 3600*h + 60*m + s

#####################################################

def saveDatFile(stats, type):
    #pprint.pprint(stats)

    directory = "plots"
    if not os.path.exists(directory):
        os.makedirs(directory)

    output = open(directory+"/"+type+".dat", 'w')

    for line in stats:
        output.write(' '.join(map(str, line))+"\n")

    output.close()

    return


#####################################################

def getGeneralStats(data,stats):
    workflow = data[1]
    execution_id = data[6]

    if workflow not in stats:
        stats[workflow] = {}

    if execution_id not in stats[workflow]:
        stats[workflow][execution_id] = {}

    return stats

#####################################################
def getActivity(line):

    if "example_workflow::" in line:

        activity_complete = line[18:]
        activity = activity_complete.split("_")
        return activity[0]

    return None

#####################################################
def getBreakdown(workflow, execution_id, filename, stats):

    enableRead = False

    with open(filename, 'r') as f:
        data = f.readlines()

        for line in data:

            if enableRead:
                if "Transformation" not in line:
                    stats_line = line.split() #print stats_line[7]

                    activity = getActivity(stats_line[0])
                    if activity:
                        if activity not in stats[workflow][execution_id]:
                            stats[workflow][execution_id][activity] = [float(stats_line[7])]
                        else:
                            stats[workflow][execution_id][activity].append(float(stats_line[7]))


            if "# All (All)" in line:
                enableRead = True

    return stats

def getSummary(workflow, execution_id, filename, stats):

    #print workflow

    with open(filename, 'r') as f:
        data = f.readlines()

        for line in data:
            if(line.find("Workflow wall time",0,18) > -1):
                timeline = line.split(":")
                workflow_total_time = timeline[1].strip()

                if " hr" not in workflow_total_time:
                    workflow_total_time = "0:"+workflow_total_time

                workflow_total_time = workflow_total_time.replace(" hrs, ",":")
                workflow_total_time = workflow_total_time.replace(" hr, ",":")
                workflow_total_time = workflow_total_time.replace(" mins, ",":")
                workflow_total_time = workflow_total_time.replace(" min, ",":")
                workflow_total_time = workflow_total_time.replace(" mins",":00")
                workflow_total_time = workflow_total_time.replace(" min",":00")
                workflow_total_time = workflow_total_time.replace(" secs","")
                workflow_total_time = workflow_total_time.replace(" sec","")

                #workflow_total_time = hms_to_seconds(workflow_total_time) #seconds
                #print workflow_total_time
                if workflow_total_time:
                    if "workflow wall time" not in stats[workflow][execution_id]:
                        stats[workflow][execution_id]["workflow wall time"] = [workflow_total_time]
                    else:
                        stats[workflow][execution_id]["workflow wall time"].append(workflow_total_time)

    return

#####################################################

def convert_second_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

#####################################################

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    #m, se = np.mean(a), scipy.stats.sem(a)
    #h = se * sp.stats.t.ppf((1+confidence)/2., n-1)
    #return m, m-h, m+h
    m = np.mean(a)
    m_min, m_max = sp.stats.t.interval(0.95, len(a)-1, loc=np.mean(a), scale=sp.stats.sem(a))

    if math.isnan(m_min):
        m_min = m
    if math.isnan(m_max):
        m_max = m

    return m, m_min, m_max

def colorType(workflow):

    if workflow in ["w-01","w-02","w-03"]:
        return 1

    if workflow in ["w-04","w-05","w-06"]:
        return 2

    if workflow in ["w-07","w-08"]:
        return 3

    if workflow in ["w-09","w-10","w-11"]:
        return 4

    return

#####################################################

def saveMakespanDat(stats,type, attribute):
    workflow_total_time = []
    raw_values = []

    for workflow, values in sorted(stats.iteritems()):
        all_values = []

        raw = []
        raw.append(str.upper(workflow))

        for execution_id, attr in values.iteritems():
            for item in  attr[attribute]:
                item = hms_to_seconds(item)
                all_values.append(item)
                raw.append(item)

        raw_values.append(raw)
        #pprint.pprint(all_values)

        mean, min_v, max_v = mean_confidence_interval(all_values)

        # min_v = convert_second_to_hms(min_v)
        # mean = convert_second_to_hms(mean)
        # max_v =  convert_second_to_hms(max_v)

        info = []
        info.append(str.upper(workflow))
        info.append(mean)
        info.append(min_v)
        info.append(max_v)
        info.append(colorType(workflow))


        workflow_total_time.append(info)

    #pprint.pprint(info)

    # for i in range(0,len(raw_values)-1):
    #
    #     for j in range(i+1,len(raw_values)):
    #         print raw_values[i]
    #         print raw_values[j]
    #
    #         s1 = raw_values[i][1:6]
    #         s2 = raw_values[j][1:6]
    #
    #         print raw_values[i][0],
    #         print raw_values[j][0]
    #
    #         compareTwoSamples(s1, s2)
    #         print "\n"


    saveDatFile(workflow_total_time, type)
    saveDatFile(raw_values, "raw_"+type)
    return

#####################################################
def costDB(workflow, runtime_hours):

    if workflow in ["w-01","w-02","w-03"]:
        total_disk_gb = 12
        value_disk_gb = 0.17
        total_value_disk_gb = total_disk_gb * value_disk_gb

        total_vm = 1
        value_vm_hour = 0.055
        total_value_vm_runtime = total_vm * value_vm_hour * runtime_hours

        return (total_value_disk_gb + total_value_vm_runtime)

    if workflow in ["w-04","w-05","w-06"]:
        total_disk_gb = 47
        value_disk_gb = 0.17
        total_value_disk_gb = total_disk_gb * value_disk_gb

        total_vm = 1
        value_vm_hour = 0.055
        total_value_vm_runtime = total_vm * value_vm_hour * runtime_hours

        return (total_value_disk_gb + total_value_vm_runtime)

    if workflow in ["w-07_0","w-07_1", "w-07_2", "w-08_0", "w-08_1","w-08_2"]:

        total_disk_gb = 35
        value_disk_gb = 0.17
        total_value_disk_gb_1 = total_disk_gb * value_disk_gb

        total_vm = 6
        value_vm_hour = 0.055
        total_value_vm_runtime_1 = total_vm * value_vm_hour * runtime_hours

        total_disk_gb = 12
        value_disk_gb = 0.17
        total_value_disk_gb_2 = total_disk_gb * value_disk_gb

        total_vm = 3
        value_vm_hour = 0.03
        total_value_vm_runtime_2 = total_vm * value_vm_hour * runtime_hours

        return (total_value_disk_gb_1 + total_value_vm_runtime_1 + total_value_disk_gb_2 + total_value_vm_runtime_2)

    if workflow in ["w-09_0","w-09_1","w-09_2","w-10_0","w-10_1","w-10_2","w-11_0","w-11_1","w-11_2"]:

        total_disk_gb = 40
        value_disk_gb = 0.17
        total_value_disk_gb_1 = total_disk_gb * value_disk_gb

        total_vm = 6
        value_vm_hour = 0.055
        total_value_vm_runtime_1 = total_vm * value_vm_hour * runtime_hours

        total_disk_gb = 37
        value_disk_gb = 0.17
        total_value_disk_gb_2 = total_disk_gb * value_disk_gb

        total_vm = 9
        value_vm_hour = 0.03
        total_value_vm_runtime_2 = total_vm * value_vm_hour * runtime_hours

        return (total_value_disk_gb_1 + total_value_vm_runtime_1 + total_value_disk_gb_2 + total_value_vm_runtime_2)


    return

def totalSlave(workflow):
    if workflow in ["w-01","w-04"]: return 1
    if workflow in ["w-02","w-03","w-05","w-06","w-07","w-08"]: return 3
    if workflow in ["w-09","w-10","w-11"]: return 9

def costSlave(total_slaves, runtime_hours):
    total_value_disk_gb = 10 * 0.17
    value_vm_hour = 0.055

    return total_slaves * value_vm_hour * runtime_hours + total_value_disk_gb * total_slaves

#####################################################

def saveMakespanCostDat(stats,type, attribute):
    workflow_total_cost = []
    raw_values = []

    for workflow, values in sorted(stats.iteritems()):
        print "\n"+workflow

        all_values = []

        raw = []
        raw.append(str.upper(workflow))

        for execution_id, attr in values.iteritems():
            for item in  attr[attribute]:
                item_seconds = hms_to_seconds(item)
                runtime_hours = (item_seconds*1.0)/60/60

                runtime_hours = math.ceil(runtime_hours)

                total_db_cost = costDB(workflow,runtime_hours)
                total_slaves = totalSlave(workflow);
                total_cost_slaves = costSlave(total_slaves, runtime_hours)

                print "DB: "+str(total_db_cost)
                print "SLAVE: "+str(total_cost_slaves)
                print total_slaves
                print runtime_hours

                total_cost_execution = total_cost_slaves + total_db_cost
                print total_cost_execution

                all_values.append(total_cost_execution)
                raw.append(total_cost_execution)

        raw_values.append(raw)

        #pprint.pprint(all_values)

        mean, min_v, max_v = mean_confidence_interval(all_values)

        info = []
        info.append(str.upper(workflow))
        info.append(mean)
        info.append(min_v)
        info.append(max_v)
        info.append(colorType(workflow))

        workflow_total_cost.append(info)

    #pprint.pprint(info)


    saveDatFile(workflow_total_cost, type)
    saveDatFile(raw_values, "raw_"+type)
    return

#####################################################
def compareTwoSamples(s1, s2):
    diff_s1_s2 = []

    for i in range(0,5):
        diff_s1_s2.append(s1[i]-s2[i])


    mean, min_v, max_v = mean_confidence_interval(diff_s1_s2)

    print diff_s1_s2
    print mean,
    print min_v,
    print max_v

    if min_v > 0 and max_v > 0:
        print "sample 2 is more efficient because the s1 is higher"
    elif min_v < 0 and max_v < 0:
        print "sample 1 is more efficient because the s2 is higher"
    else:
        print "samples without significantly diffences and they are equivalents"

    return

#####################################################
def saveActivityDat(stats,type):
    print type

    activity_time = []
    raw_values = []

    for workflow, values in sorted(stats.iteritems()):
        all_values = []

        raw = []
        raw.append(str.upper(workflow))

        for item in values:
            all_values.append(item)
            raw.append(item)

        raw_values.append(raw)
        #pprint.pprint(all_values)

        mean, min_v, max_v = mean_confidence_interval(all_values)

        info = []
        info.append(str.upper(workflow))
        info.append(mean)
        info.append(min_v)
        info.append(max_v)
        info.append(colorType(workflow))

        activity_time.append(info)

    saveDatFile(activity_time, type)
    saveDatFile(raw_values, "raw_"+type)
    return

#####################################################




PATH = "."
DIR_STATS = "statistics"

# stats [db][workflow][activity] = [1,2,3]
stats_makespan = {}
stats_activities = {}

for path, subdirs, files in sorted(os.walk(PATH)):
    for filename in files:
        if DIR_STATS in path:
            if ("breakdown.txt" in filename):
                 f = os.path.join(path, filename)
                 data = f.split("/")
                 stats_activities = getGeneralStats(data,stats_activities)
                 getBreakdown(data[1],data[6],f,stats_activities)


            if ("summary.txt" in filename):
               f = os.path.join(path, filename)
               data = f.split("/")
               #print data[6] #execution id
               stats_makespan = getGeneralStats(data,stats_makespan)
               getSummary(data[1],data[6],f,stats_makespan)


#pprint.pprint(stats_activities)
#pprint.pprint(stats_makespan)

#raw_activity = []
#activity = []
#
# stats_grouped = {}
#
# for workflow, values in sorted(stats_activities.iteritems()):
#     print "\n\n"+workflow
#
#saveMakespanCostDat
#     #summary = []
#
#     # media por execution de cada atividade em um tipo de workflow + I.C.
#     for execution_id, executions in values.iteritems():
#         for activity, values in executions.iteritems():
#
#             if activity not in stats_grouped:
#                 stats_grouped[activity] = {}
#
#             if workflow not in stats_grouped[activity]:
#                 stats_grouped[activity][workflow] = []
#
#             m = np.mean(values)
#             stats_grouped[activity][workflow].append(m)
#
#             #
#             # raw = []
#             # raw.append(workflow)
#             # raw.append(activity)
#             # raw.append(execution_id)
#             #
#             # for v in values:
#             #     raw.append(v)
#             #
#             # print raw
#
#             # print activity,
#             # print values
#             # print m
#
#
# pprint.pprint(stats_grouped)
# for activity, values in stats_grouped.iteritems():
#     saveActivityDat(values,activity)

# saveActivityDat(stats_grouped['mediancpu'],"mediancpu")
# saveActivityDat(stats_grouped['maxmincpu'],"maxmincpu")
#
# saveActivityDat(stats_grouped['calculateratio'],"calculateratio")
# saveActivityDat(stats_grouped['maxminratio'],"maxminratio")

saveMakespanDat(stats_makespan, "makespan",'workflow wall time')
saveMakespanCostDat(stats_makespan,"makespan_cost", 'workflow wall time')

# group the tasks with same prefix


# label, first_value, second_value .gnu if the task has many copies, just added the values
