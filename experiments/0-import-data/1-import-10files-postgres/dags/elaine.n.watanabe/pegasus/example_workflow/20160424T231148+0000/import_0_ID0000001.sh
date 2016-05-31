#!/bin/bash
set -e
pegasus_lite_version_major="4"
pegasus_lite_version_minor="6"
pegasus_lite_version_patch="0"

. pegasus-lite-common.sh

pegasus_lite_init

# cleanup in case of failures
trap pegasus_lite_exit INT TERM EXIT

echo -e "\n################################ Setting up workdir ################################"  1>&2
# work dir
export pegasus_lite_work_dir=$PWD
pegasus_lite_setup_work_dir

echo -e "\n###################### figuring out the worker package to use ######################"  1>&2
# figure out the worker package to use
pegasus_lite_worker_package

echo -e "\n##################### setting the xbit for executables staged #####################"  1>&2
# set the xbit for any executables staged
/bin/chmod +x example_workflow-import_0-1.0 

echo -e "\n############################# executing the user tasks #############################"  1>&2
# execute the tasks
set +e
pegasus-kickstart -n example_workflow::import_0:1.0 -N ID0000001 -R condorpool  -L example_workflow -T 2016-04-24T23:11:45+00:00 ./example_workflow-import_0-1.0 
job_ec=$?
set -e

