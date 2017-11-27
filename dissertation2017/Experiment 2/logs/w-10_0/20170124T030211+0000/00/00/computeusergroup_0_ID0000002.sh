#!/bin/bash
set -e
pegasus_lite_version_major="4"
pegasus_lite_version_minor="7"
pegasus_lite_version_patch="0"
pegasus_lite_enforce_strict_wp_check="true"
pegasus_lite_version_allow_wp_auto_download="true"

. pegasus-lite-common.sh

pegasus_lite_init

# cleanup in case of failures
trap pegasus_lite_signal_int INT
trap pegasus_lite_signal_term TERM
trap pegasus_lite_exit EXIT

echo -e "\n################################ Setting up workdir ################################"  1>&2
# work dir
export pegasus_lite_work_dir=$PWD
pegasus_lite_setup_work_dir

echo -e "\n###################### figuring out the worker package to use ######################"  1>&2
# figure out the worker package to use
pegasus_lite_worker_package

echo -e "\n##################### setting the xbit for executables staged #####################"  1>&2
# set the xbit for any executables staged
/bin/chmod +x wikiflow-computeusergroup_0-1.0 

echo -e "\n############################# executing the user tasks #############################"  1>&2
# execute the tasks
set +e
pegasus-kickstart -n wikiflow::computeusergroup_0:1.0 -N ID0000002 -R condorpool  -s ConfigDB_SessionCompute_1.py=ConfigDB_SessionCompute_1.py -s ConfigDB_SessionCompute_7.py=ConfigDB_SessionCompute_7.py -s ConfigDB_SessionCompute_4.py=ConfigDB_SessionCompute_4.py -s ConfigDB_SessionCompute_0.py=ConfigDB_SessionCompute_0.py -s ConfigDB_SessionCompute_2.py=ConfigDB_SessionCompute_2.py -s ConfigDB_SessionCompute_6.py=ConfigDB_SessionCompute_6.py -s ConfigDB_SessionCompute_3.py=ConfigDB_SessionCompute_3.py -s ConfigDB_SessionCompute_5.py=ConfigDB_SessionCompute_5.py -s ConfigDB_SessionCompute_8.py=ConfigDB_SessionCompute_8.py -L example_workflow -T 2017-01-24T03:02:11+00:00 ./wikiflow-computeusergroup_0-1.0 
job_ec=$?
set -e
