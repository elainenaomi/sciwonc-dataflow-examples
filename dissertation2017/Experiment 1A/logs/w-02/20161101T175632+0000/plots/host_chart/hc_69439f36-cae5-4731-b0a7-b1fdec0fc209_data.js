
var hc_data = [ 
{ "name":"ip-172-31-28-254.us-west-2.compute.internal" , "jobs": [
	{
	"name":"medianmemory_0_ID0000005" , "jobS":649 , "jobD":526.0 , "preS":'' , "preD":'' , "cS":649 , "cD":526.0 , "gS":'' , "gD":'' , "eS":674 , "eD":501.0 , "kS":668 , "kD":500.984 , "postS":1175 , "postD":5.0 , "state":3 , "transformation": "example_workflow::medianmemory_0:1.0"  , "color": "#d9d9d9"  , "sub_wf":0 , "sub_wf_name":''
	},
]}, 
{ "name":"ip-172-31-28-252.us-west-2.compute.internal" , "jobs": [
	{
	"name":"mediancpu_0_ID0000004" , "jobS":649 , "jobD":526.0 , "preS":'' , "preD":'' , "cS":649 , "cD":526.0 , "gS":'' , "gD":'' , "eS":674 , "eD":501.0 , "kS":667 , "kD":499.805 , "postS":1175 , "postD":5.0 , "state":3 , "transformation": "example_workflow::mediancpu_0:1.0"  , "color": "#bc80bd"  , "sub_wf":0 , "sub_wf_name":''
	},
]}, 
{ "name":"Unknown" , "jobs": [
	{
	"name":"create_dir_example_workflow_0_local" , "jobS":5 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":5 , "cD":5.0 , "gS":'' , "gD":'' , "eS":10 , "eD":0.0 , "kS":10 , "kD":0.0 , "postS":10 , "postD":5.0 , "state":3 , "transformation": "pegasus::dirmanager"  , "color": "#8dd3c7"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"cleanup_example_workflow_0_local" , "jobS":4561 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":4561 , "cD":5.0 , "gS":'' , "gD":'' , "eS":4566 , "eD":0.0 , "kS":4566 , "kD":0.0 , "postS":'' , "postD":'' , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},
]}, 
{ "name":"ip-172-31-29-197.us-west-1.compute.internal" , "jobs": [
	{
	"name":"stage_in_local_local_0_0" , "jobS":20 , "jobD":6.0 , "preS":'' , "preD":'' , "cS":20 , "cD":6.0 , "gS":'' , "gD":'' , "eS":20 , "eD":6.0 , "kS":20 , "kD":2.215 , "postS":26 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_local_local_6_0" , "jobS":20 , "jobD":6.0 , "preS":'' , "preD":'' , "cS":20 , "cD":6.0 , "gS":'' , "gD":'' , "eS":26 , "eD":0.0 , "kS":22 , "kD":2.386 , "postS":26 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_2_1" , "jobS":20 , "jobD":6.0 , "preS":'' , "preD":'' , "cS":20 , "cD":6.0 , "gS":'' , "gD":'' , "eS":26 , "eD":0.0 , "kS":22 , "kD":2.495 , "postS":26 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_5_0" , "jobS":20 , "jobD":6.0 , "preS":'' , "preD":'' , "cS":20 , "cD":6.0 , "gS":'' , "gD":'' , "eS":26 , "eD":0.0 , "kS":22 , "kD":2.428 , "postS":26 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_local_local_2_0" , "jobS":20 , "jobD":11.0 , "preS":'' , "preD":'' , "cS":20 , "cD":11.0 , "gS":'' , "gD":'' , "eS":26 , "eD":5.0 , "kS":22 , "kD":4.509 , "postS":31 , "postD":6.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_local_local_2_1" , "jobS":26 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":26 , "cD":5.0 , "gS":'' , "gD":'' , "eS":26 , "eD":5.0 , "kS":25 , "kD":2.512 , "postS":31 , "postD":6.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_1_0" , "jobS":26 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":26 , "cD":5.0 , "gS":'' , "gD":'' , "eS":26 , "eD":5.0 , "kS":25 , "kD":2.504 , "postS":31 , "postD":6.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_local_local_5_0" , "jobS":26 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":26 , "cD":5.0 , "gS":'' , "gD":'' , "eS":26 , "eD":5.0 , "kS":26 , "kD":2.404 , "postS":31 , "postD":6.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_local_local_3_0" , "jobS":26 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":26 , "cD":5.0 , "gS":'' , "gD":'' , "eS":31 , "eD":0.0 , "kS":27 , "kD":2.338 , "postS":31 , "postD":6.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_7_0" , "jobS":26 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":26 , "cD":5.0 , "gS":'' , "gD":'' , "eS":31 , "eD":0.0 , "kS":27 , "kD":2.288 , "postS":31 , "postD":6.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_local_local_4_0" , "jobS":31 , "jobD":11.0 , "preS":'' , "preD":'' , "cS":31 , "cD":11.0 , "gS":'' , "gD":'' , "eS":37 , "eD":5.0 , "kS":36 , "kD":2.735 , "postS":42 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_local_local_1_0" , "jobS":31 , "jobD":11.0 , "preS":'' , "preD":'' , "cS":31 , "cD":11.0 , "gS":'' , "gD":'' , "eS":37 , "eD":5.0 , "kS":36 , "kD":2.886 , "postS":42 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_local_local_7_0" , "jobS":31 , "jobD":11.0 , "preS":'' , "preD":'' , "cS":31 , "cD":11.0 , "gS":'' , "gD":'' , "eS":37 , "eD":5.0 , "kS":36 , "kD":2.785 , "postS":42 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_4_1" , "jobS":31 , "jobD":11.0 , "preS":'' , "preD":'' , "cS":31 , "cD":11.0 , "gS":'' , "gD":'' , "eS":37 , "eD":5.0 , "kS":36 , "kD":2.765 , "postS":42 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_4_0" , "jobS":31 , "jobD":11.0 , "preS":'' , "preD":'' , "cS":31 , "cD":11.0 , "gS":'' , "gD":'' , "eS":37 , "eD":5.0 , "kS":36 , "kD":4.754 , "postS":42 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_0_0" , "jobS":37 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":37 , "cD":5.0 , "gS":'' , "gD":'' , "eS":42 , "eD":0.0 , "kS":39 , "kD":2.596 , "postS":42 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_2_0" , "jobS":37 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":37 , "cD":10.0 , "gS":'' , "gD":'' , "eS":42 , "eD":5.0 , "kS":39 , "kD":4.66 , "postS":47 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_3_1" , "jobS":37 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":37 , "cD":5.0 , "gS":'' , "gD":'' , "eS":42 , "eD":0.0 , "kS":39 , "kD":2.599 , "postS":42 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_3_0" , "jobS":37 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":37 , "cD":10.0 , "gS":'' , "gD":'' , "eS":42 , "eD":5.0 , "kS":39 , "kD":4.517 , "postS":47 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"stage_in_remote_local_6_0" , "jobS":37 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":37 , "cD":5.0 , "gS":'' , "gD":'' , "eS":42 , "eD":0.0 , "kS":39 , "kD":2.788 , "postS":42 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"clean_up_local_level_3_0" , "jobS":258 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":258 , "cD":5.0 , "gS":'' , "gD":'' , "eS":258 , "eD":5.0 , "kS":258 , "kD":4.185 , "postS":263 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"clean_up_local_level_4_0" , "jobS":649 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":649 , "cD":5.0 , "gS":'' , "gD":'' , "eS":649 , "eD":5.0 , "kS":649 , "kD":4.212 , "postS":654 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"clean_up_local_level_5_1" , "jobS":1185 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":1185 , "cD":5.0 , "gS":'' , "gD":'' , "eS":1190 , "eD":0.0 , "kS":1185 , "kD":4.199 , "postS":1190 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"clean_up_local_level_5_0" , "jobS":1751 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":1751 , "cD":10.0 , "gS":'' , "gD":'' , "eS":1751 , "eD":10.0 , "kS":1751 , "kD":8.189 , "postS":1761 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"clean_up_local_level_6_0" , "jobS":2492 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":2492 , "cD":10.0 , "gS":'' , "gD":'' , "eS":2492 , "eD":10.0 , "kS":2492 , "kD":8.179 , "postS":2502 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"clean_up_local_level_7_0" , "jobS":4394 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":4394 , "cD":10.0 , "gS":'' , "gD":'' , "eS":4394 , "eD":10.0 , "kS":4394 , "kD":8.165 , "postS":4404 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"clean_up_local_level_8_0" , "jobS":4515 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":4515 , "cD":5.0 , "gS":'' , "gD":'' , "eS":4515 , "eD":5.0 , "kS":4515 , "kD":4.205 , "postS":4520 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"clean_up_local_level_9_0" , "jobS":4530 , "jobD":11.0 , "preS":'' , "preD":'' , "cS":4530 , "cD":11.0 , "gS":'' , "gD":'' , "eS":4541 , "eD":0.0 , "kS":4536 , "kD":4.174 , "postS":4541 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"clean_up_local_level_10_0" , "jobS":4546 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":4546 , "cD":5.0 , "gS":'' , "gD":'' , "eS":4551 , "eD":0.0 , "kS":4546 , "kD":4.132 , "postS":4551 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''
	},
]}, 
{ "name":"ip-172-31-28-253.us-west-2.compute.internal" , "jobs": [
	{
	"name":"init_0_ID0000001" , "jobS":52 , "jobD":196.0 , "preS":'' , "preD":'' , "cS":52 , "cD":196.0 , "gS":'' , "gD":'' , "eS":62 , "eD":186.0 , "kS":62 , "kD":182.083 , "postS":248 , "postD":5.0 , "state":3 , "transformation": "example_workflow::init_0:1.0"  , "color": "#bebada"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"generalinfo_0_ID0000002" , "jobS":258 , "jobD":381.0 , "preS":'' , "preD":'' , "cS":258 , "cD":381.0 , "gS":'' , "gD":'' , "eS":263 , "eD":376.0 , "kS":259 , "kD":377.581 , "postS":639 , "postD":5.0 , "state":3 , "transformation": "example_workflow::generalinfo_0:1.0"  , "color": "#b3de69"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"statscpumemory_0_ID0000003" , "jobS":649 , "jobD":1091.0 , "preS":'' , "preD":'' , "cS":649 , "cD":1091.0 , "gS":'' , "gD":'' , "eS":654 , "eD":1086.0 , "kS":650 , "kD":1086.666 , "postS":1740 , "postD":5.0 , "state":3 , "transformation": "example_workflow::statscpumemory_0:1.0"  , "color": "#fccde5"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"taskevent_0_ID0000006" , "jobS":1751 , "jobD":730.0 , "preS":'' , "preD":'' , "cS":1751 , "cD":730.0 , "gS":'' , "gD":'' , "eS":1766 , "eD":715.0 , "kS":1766 , "kD":711.665 , "postS":2481 , "postD":6.0 , "state":3 , "transformation": "example_workflow::taskevent_0:1.0"  , "color": "#ccebc5"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"calculateratio_0_ID0000007" , "jobS":2492 , "jobD":1892.0 , "preS":'' , "preD":'' , "cS":2492 , "cD":1892.0 , "gS":'' , "gD":'' , "eS":2497 , "eD":1887.0 , "kS":2493 , "kD":1886.337 , "postS":4384 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_0:1.0"  , "color": "#fb8072"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"averageratioevent_0_ID0000008" , "jobS":4394 , "jobD":111.0 , "preS":'' , "preD":'' , "cS":4394 , "cD":111.0 , "gS":'' , "gD":'' , "eS":4435 , "eD":70.0 , "kS":4432 , "kD":71.62 , "postS":4505 , "postD":5.0 , "state":3 , "transformation": "example_workflow::averageratioevent_0:1.0"  , "color": "#8dd3c7"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"analysisevent_0_ID0000009" , "jobS":4515 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":4515 , "cD":5.0 , "gS":'' , "gD":'' , "eS":4520 , "eD":0.0 , "kS":4516 , "kD":0.111 , "postS":4520 , "postD":5.0 , "state":3 , "transformation": "example_workflow::analysisevent_0:1.0"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''
	},

	{
	"name":"terminate_0_ID0000010" , "jobS":4530 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":4530 , "cD":5.0 , "gS":'' , "gD":'' , "eS":4535 , "eD":0.0 , "kS":4532 , "kD":0.112 , "postS":4535 , "postD":6.0 , "state":3 , "transformation": "example_workflow::terminate_0:1.0"  , "color": "#bebada"  , "sub_wf":0 , "sub_wf_name":''
	},
]},];