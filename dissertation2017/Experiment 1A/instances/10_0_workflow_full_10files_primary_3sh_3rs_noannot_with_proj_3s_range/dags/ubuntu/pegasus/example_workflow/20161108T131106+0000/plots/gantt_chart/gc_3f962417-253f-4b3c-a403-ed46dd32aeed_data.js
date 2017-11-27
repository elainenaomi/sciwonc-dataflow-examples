
var data = [{
"name":"create_dir_example_workflow_0_local" , "jobS":4 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":4 , "cD":5.0 , "gS":'' , "gD":'' , "eS":9 , "eD":0.0 , "kS":9 , "kD":0.0 , "postS":9 , "postD":5.0 , "state":3 , "transformation": "pegasus::dirmanager"  , "color": "#8dd3c7"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_0_0" , "jobS":20 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":20 , "cD":5.0 , "gS":'' , "gD":'' , "eS":20 , "eD":5.0 , "kS":20 , "kD":2.205 , "postS":25 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_2_1" , "jobS":20 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":20 , "cD":5.0 , "gS":'' , "gD":'' , "eS":25 , "eD":0.0 , "kS":22 , "kD":2.532 , "postS":25 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_6_0" , "jobS":20 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":20 , "cD":5.0 , "gS":'' , "gD":'' , "eS":25 , "eD":0.0 , "kS":22 , "kD":2.504 , "postS":25 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_5_1" , "jobS":20 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":20 , "cD":10.0 , "gS":'' , "gD":'' , "eS":25 , "eD":5.0 , "kS":22 , "kD":4.537 , "postS":30 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_5_0" , "jobS":20 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":20 , "cD":10.0 , "gS":'' , "gD":'' , "eS":25 , "eD":5.0 , "kS":22 , "kD":4.457 , "postS":30 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_2_0" , "jobS":25 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":25 , "cD":5.0 , "gS":'' , "gD":'' , "eS":25 , "eD":5.0 , "kS":25 , "kD":4.385 , "postS":30 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_2_1" , "jobS":25 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":25 , "cD":5.0 , "gS":'' , "gD":'' , "eS":25 , "eD":5.0 , "kS":25 , "kD":2.309 , "postS":30 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_1_0" , "jobS":25 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":25 , "cD":5.0 , "gS":'' , "gD":'' , "eS":30 , "eD":0.0 , "kS":27 , "kD":2.358 , "postS":30 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_3_1" , "jobS":25 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":25 , "cD":10.0 , "gS":'' , "gD":'' , "eS":30 , "eD":5.0 , "kS":27 , "kD":4.348 , "postS":35 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_5_0" , "jobS":25 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":25 , "cD":10.0 , "gS":'' , "gD":'' , "eS":30 , "eD":5.0 , "kS":27 , "kD":4.383 , "postS":35 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_3_0" , "jobS":30 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":30 , "cD":10.0 , "gS":'' , "gD":'' , "eS":35 , "eD":5.0 , "kS":31 , "kD":4.464 , "postS":40 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_5_1" , "jobS":30 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":30 , "cD":10.0 , "gS":'' , "gD":'' , "eS":35 , "eD":5.0 , "kS":31 , "kD":4.585 , "postS":40 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_4_0" , "jobS":30 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":30 , "cD":10.0 , "gS":'' , "gD":'' , "eS":35 , "eD":5.0 , "kS":32 , "kD":4.534 , "postS":40 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_7_0" , "jobS":30 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":30 , "cD":5.0 , "gS":'' , "gD":'' , "eS":35 , "eD":0.0 , "kS":31 , "kD":2.603 , "postS":35 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_4_1" , "jobS":30 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":30 , "cD":10.0 , "gS":'' , "gD":'' , "eS":35 , "eD":5.0 , "kS":32 , "kD":4.502 , "postS":40 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_local_local_1_0" , "jobS":35 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":35 , "cD":5.0 , "gS":'' , "gD":'' , "eS":40 , "eD":0.0 , "kS":36 , "kD":2.636 , "postS":40 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_4_1" , "jobS":35 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":35 , "cD":10.0 , "gS":'' , "gD":'' , "eS":40 , "eD":5.0 , "kS":36 , "kD":4.903 , "postS":45 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_4_0" , "jobS":35 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":35 , "cD":10.0 , "gS":'' , "gD":'' , "eS":40 , "eD":5.0 , "kS":36 , "kD":4.792 , "postS":45 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_2_0" , "jobS":35 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":35 , "cD":10.0 , "gS":'' , "gD":'' , "eS":40 , "eD":5.0 , "kS":36 , "kD":4.736 , "postS":45 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_3_1" , "jobS":35 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":35 , "cD":10.0 , "gS":'' , "gD":'' , "eS":40 , "eD":5.0 , "kS":36 , "kD":4.868 , "postS":45 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_3_0" , "jobS":40 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":40 , "cD":10.0 , "gS":'' , "gD":'' , "eS":45 , "eD":5.0 , "kS":41 , "kD":4.27 , "postS":50 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"stage_in_remote_local_6_0" , "jobS":40 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":40 , "cD":5.0 , "gS":'' , "gD":'' , "eS":45 , "eD":0.0 , "kS":41 , "kD":2.383 , "postS":45 , "postD":5.0 , "state":3 , "transformation": "pegasus::transfer"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"init_0_ID0000001" , "jobS":40 , "jobD":20.0 , "preS":'' , "preD":'' , "cS":40 , "cD":15.0 , "gS":'' , "gD":'' , "eS":55 , "eD":0.0 , "kS":42 , "kD":0.64 , "postS":55 , "postD":5.0 , "state":3 , "transformation": "example_workflow::init_0:1.0"  , "color": "#bebada"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"init_0_ID0000001_retry_1" , "jobS":65 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":65 , "cD":5.0 , "gS":'' , "gD":'' , "eS":70 , "eD":0.0 , "kS":54 , "kD":0.638 , "postS":70 , "postD":5.0 , "state":3 , "transformation": "example_workflow::init_0:1.0"  , "color": "#bebada"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_3_0" , "jobS":80 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":80 , "cD":5.0 , "gS":'' , "gD":'' , "eS":80 , "eD":5.0 , "kS":80 , "kD":2.158 , "postS":85 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"generalinfo_0_ID0000002" , "jobS":80 , "jobD":260.0 , "preS":'' , "preD":'' , "cS":80 , "cD":255.0 , "gS":'' , "gD":'' , "eS":85 , "eD":250.0 , "kS":69 , "kD":251.964 , "postS":335 , "postD":5.0 , "state":3 , "transformation": "example_workflow::generalinfo_0:1.0"  , "color": "#b3de69"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_4_0" , "jobS":345 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":345 , "cD":5.0 , "gS":'' , "gD":'' , "eS":345 , "eD":5.0 , "kS":345 , "kD":4.205 , "postS":350 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"statscpumemory_0_ID0000003" , "jobS":345 , "jobD":551.0 , "preS":'' , "preD":'' , "cS":345 , "cD":546.0 , "gS":'' , "gD":'' , "eS":350 , "eD":541.0 , "kS":334 , "kD":544.077 , "postS":891 , "postD":5.0 , "state":3 , "transformation": "example_workflow::statscpumemory_0:1.0"  , "color": "#fccde5"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"medianmemory_0_ID0000005" , "jobS":345 , "jobD":556.0 , "preS":'' , "preD":'' , "cS":345 , "cD":551.0 , "gS":'' , "gD":'' , "eS":355 , "eD":541.0 , "kS":353 , "kD":538.892 , "postS":896 , "postD":5.0 , "state":3 , "transformation": "example_workflow::medianmemory_0:1.0"  , "color": "#d9d9d9"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"mediancpu_0_ID0000004" , "jobS":345 , "jobD":561.0 , "preS":'' , "preD":'' , "cS":345 , "cD":556.0 , "gS":'' , "gD":'' , "eS":355 , "eD":546.0 , "kS":348 , "kD":544.437 , "postS":901 , "postD":5.0 , "state":3 , "transformation": "example_workflow::mediancpu_0:1.0"  , "color": "#bc80bd"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_5_0" , "jobS":906 , "jobD":17.0 , "preS":'' , "preD":'' , "cS":906 , "cD":12.0 , "gS":'' , "gD":'' , "eS":912 , "eD":6.0 , "kS":906 , "kD":8.257 , "postS":918 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"taskevent_6_ID0000012" , "jobS":912 , "jobD":26.0 , "preS":'' , "preD":'' , "cS":912 , "cD":21.0 , "gS":'' , "gD":'' , "eS":918 , "eD":15.0 , "kS":901 , "kD":18.081 , "postS":933 , "postD":5.0 , "state":3 , "transformation": "example_workflow::taskevent_6:1.0"  , "color": "#ccebc5"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"taskevent_0_ID0000006" , "jobS":912 , "jobD":287.0 , "preS":'' , "preD":'' , "cS":912 , "cD":282.0 , "gS":'' , "gD":'' , "eS":918 , "eD":276.0 , "kS":907 , "kD":278.882 , "postS":1194 , "postD":5.0 , "state":3 , "transformation": "example_workflow::taskevent_0:1.0"  , "color": "#fb8072"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"taskevent_3_ID0000009" , "jobS":912 , "jobD":96.0 , "preS":'' , "preD":'' , "cS":912 , "cD":91.0 , "gS":'' , "gD":'' , "eS":918 , "eD":85.0 , "kS":912 , "kD":86.946 , "postS":1003 , "postD":5.0 , "state":3 , "transformation": "example_workflow::taskevent_3:1.0"  , "color": "#8dd3c7"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"taskevent_1_ID0000007" , "jobS":912 , "jobD":287.0 , "preS":'' , "preD":'' , "cS":912 , "cD":282.0 , "gS":'' , "gD":'' , "eS":933 , "eD":261.0 , "kS":920 , "kD":258.403 , "postS":1194 , "postD":5.0 , "state":3 , "transformation": "example_workflow::taskevent_1:1.0"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"taskevent_5_ID0000011" , "jobS":912 , "jobD":156.0 , "preS":'' , "preD":'' , "cS":912 , "cD":151.0 , "gS":'' , "gD":'' , "eS":938 , "eD":125.0 , "kS":934 , "kD":129.025 , "postS":1063 , "postD":5.0 , "state":3 , "transformation": "example_workflow::taskevent_5:1.0"  , "color": "#bebada"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"taskevent_4_ID0000010" , "jobS":918 , "jobD":185.0 , "preS":'' , "preD":'' , "cS":918 , "cD":180.0 , "gS":'' , "gD":'' , "eS":938 , "eD":160.0 , "kS":935 , "kD":161.977 , "postS":1098 , "postD":5.0 , "state":3 , "transformation": "example_workflow::taskevent_4:1.0"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"taskevent_2_ID0000008" , "jobS":918 , "jobD":110.0 , "preS":'' , "preD":'' , "cS":918 , "cD":105.0 , "gS":'' , "gD":'' , "eS":938 , "eD":85.0 , "kS":930 , "kD":85.057 , "postS":1023 , "postD":5.0 , "state":3 , "transformation": "example_workflow::taskevent_2:1.0"  , "color": "#b3de69"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"taskevent_8_ID0000014" , "jobS":918 , "jobD":110.0 , "preS":'' , "preD":'' , "cS":918 , "cD":105.0 , "gS":'' , "gD":'' , "eS":938 , "eD":85.0 , "kS":921 , "kD":86.409 , "postS":1023 , "postD":5.0 , "state":3 , "transformation": "example_workflow::taskevent_8:1.0"  , "color": "#fccde5"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"taskevent_7_ID0000013" , "jobS":918 , "jobD":60.0 , "preS":'' , "preD":'' , "cS":918 , "cD":55.0 , "gS":'' , "gD":'' , "eS":938 , "eD":35.0 , "kS":925 , "kD":35.464 , "postS":973 , "postD":5.0 , "state":3 , "transformation": "example_workflow::taskevent_7:1.0"  , "color": "#d9d9d9"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_5_1" , "jobS":918 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":918 , "cD":10.0 , "gS":'' , "gD":'' , "eS":923 , "eD":5.0 , "kS":922 , "kD":4.13 , "postS":928 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_6_1" , "jobS":1108 , "jobD":26.0 , "preS":'' , "preD":'' , "cS":1108 , "cD":21.0 , "gS":'' , "gD":'' , "eS":1114 , "eD":15.0 , "kS":1109 , "kD":16.144 , "postS":1129 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_6_0" , "jobS":1207 , "jobD":20.0 , "preS":'' , "preD":'' , "cS":1207 , "cD":15.0 , "gS":'' , "gD":'' , "eS":1207 , "eD":15.0 , "kS":1207 , "kD":14.24 , "postS":1222 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"calculateratio_8_ID0000023" , "jobS":1207 , "jobD":396.0 , "preS":'' , "preD":'' , "cS":1207 , "cD":391.0 , "gS":'' , "gD":'' , "eS":1212 , "eD":386.0 , "kS":1196 , "kD":386.018 , "postS":1598 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_8:1.0"  , "color": "#bc80bd"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"calculateratio_6_ID0000021" , "jobS":1207 , "jobD":311.0 , "preS":'' , "preD":'' , "cS":1207 , "cD":306.0 , "gS":'' , "gD":'' , "eS":1212 , "eD":301.0 , "kS":1202 , "kD":301.886 , "postS":1513 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_6:1.0"  , "color": "#ccebc5"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"calculateratio_7_ID0000022" , "jobS":1207 , "jobD":396.0 , "preS":'' , "preD":'' , "cS":1207 , "cD":391.0 , "gS":'' , "gD":'' , "eS":1233 , "eD":365.0 , "kS":1228 , "kD":369.443 , "postS":1598 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_7:1.0"  , "color": "#fb8072"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"calculateratio_5_ID0000020" , "jobS":1207 , "jobD":431.0 , "preS":'' , "preD":'' , "cS":1207 , "cD":426.0 , "gS":'' , "gD":'' , "eS":1233 , "eD":400.0 , "kS":1228 , "kD":404.064 , "postS":1633 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_5:1.0"  , "color": "#8dd3c7"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"calculateratio_1_ID0000016" , "jobS":1212 , "jobD":366.0 , "preS":'' , "preD":'' , "cS":1212 , "cD":361.0 , "gS":'' , "gD":'' , "eS":1233 , "eD":340.0 , "kS":1229 , "kD":344.116 , "postS":1573 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_1:1.0"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"calculateratio_4_ID0000019" , "jobS":1212 , "jobD":421.0 , "preS":'' , "preD":'' , "cS":1212 , "cD":416.0 , "gS":'' , "gD":'' , "eS":1233 , "eD":395.0 , "kS":1224 , "kD":397.281 , "postS":1628 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_4:1.0"  , "color": "#bebada"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"calculateratio_3_ID0000018" , "jobS":1212 , "jobD":471.0 , "preS":'' , "preD":'' , "cS":1212 , "cD":466.0 , "gS":'' , "gD":'' , "eS":1233 , "eD":445.0 , "kS":1215 , "kD":445.57 , "postS":1678 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_3:1.0"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"calculateratio_2_ID0000017" , "jobS":1212 , "jobD":411.0 , "preS":'' , "preD":'' , "cS":1212 , "cD":406.0 , "gS":'' , "gD":'' , "eS":1233 , "eD":385.0 , "kS":1219 , "kD":385.128 , "postS":1618 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_2:1.0"  , "color": "#b3de69"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"calculateratio_0_ID0000015" , "jobS":1212 , "jobD":386.0 , "preS":'' , "preD":'' , "cS":1212 , "cD":381.0 , "gS":'' , "gD":'' , "eS":1233 , "eD":360.0 , "kS":1216 , "kD":360.2 , "postS":1593 , "postD":5.0 , "state":3 , "transformation": "example_workflow::calculateratio_0:1.0"  , "color": "#fccde5"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_7_0" , "jobS":1643 , "jobD":20.0 , "preS":'' , "preD":'' , "cS":1643 , "cD":15.0 , "gS":'' , "gD":'' , "eS":1648 , "eD":10.0 , "kS":1643 , "kD":14.147 , "postS":1658 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_7_1" , "jobS":1688 , "jobD":25.0 , "preS":'' , "preD":'' , "cS":1688 , "cD":20.0 , "gS":'' , "gD":'' , "eS":1688 , "eD":20.0 , "kS":1688 , "kD":16.228 , "postS":1708 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"averageratioevent_1_ID0000025" , "jobS":1688 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":1688 , "cD":10.0 , "gS":'' , "gD":'' , "eS":1693 , "eD":5.0 , "kS":1675 , "kD":8.634 , "postS":1698 , "postD":5.0 , "state":3 , "transformation": "example_workflow::averageratioevent_1:1.0"  , "color": "#d9d9d9"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"averageratioevent_3_ID0000027" , "jobS":1688 , "jobD":20.0 , "preS":'' , "preD":'' , "cS":1688 , "cD":15.0 , "gS":'' , "gD":'' , "eS":1698 , "eD":5.0 , "kS":1685 , "kD":0.678 , "postS":1703 , "postD":5.0 , "state":3 , "transformation": "example_workflow::averageratioevent_3:1.0"  , "color": "#bc80bd"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"averageratioevent_0_ID0000024" , "jobS":1688 , "jobD":35.0 , "preS":'' , "preD":'' , "cS":1688 , "cD":30.0 , "gS":'' , "gD":'' , "eS":1703 , "eD":15.0 , "kS":1687 , "kD":14.832 , "postS":1718 , "postD":5.0 , "state":3 , "transformation": "example_workflow::averageratioevent_0:1.0"  , "color": "#ccebc5"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"averageratioevent_2_ID0000026" , "jobS":1688 , "jobD":75.0 , "preS":'' , "preD":'' , "cS":1688 , "cD":70.0 , "gS":'' , "gD":'' , "eS":1713 , "eD":45.0 , "kS":1698 , "kD":45.852 , "postS":1758 , "postD":5.0 , "state":3 , "transformation": "example_workflow::averageratioevent_2:1.0"  , "color": "#fb8072"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_8_0" , "jobS":1713 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":1713 , "cD":10.0 , "gS":'' , "gD":'' , "eS":1718 , "eD":5.0 , "kS":1714 , "kD":8.131 , "postS":1723 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"analysisevent_0_ID0000028" , "jobS":1768 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":1768 , "cD":5.0 , "gS":'' , "gD":'' , "eS":1773 , "eD":0.0 , "kS":1758 , "kD":0.657 , "postS":1773 , "postD":5.0 , "state":3 , "transformation": "example_workflow::analysisevent_0:1.0"  , "color": "#8dd3c7"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_8_1" , "jobS":1768 , "jobD":21.0 , "preS":'' , "preD":'' , "cS":1768 , "cD":16.0 , "gS":'' , "gD":'' , "eS":1778 , "eD":6.0 , "kS":1774 , "kD":8.135 , "postS":1784 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"terminate_0_ID0000029" , "jobS":1784 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":1784 , "cD":5.0 , "gS":'' , "gD":'' , "eS":1789 , "eD":0.0 , "kS":1773 , "kD":0.652 , "postS":1789 , "postD":5.0 , "state":3 , "transformation": "example_workflow::terminate_0:1.0"  , "color": "#4daf4a"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_9_0" , "jobS":1784 , "jobD":15.0 , "preS":'' , "preD":'' , "cS":1784 , "cD":10.0 , "gS":'' , "gD":'' , "eS":1794 , "eD":0.0 , "kS":1789 , "kD":4.197 , "postS":1794 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"clean_up_local_level_10_0" , "jobS":1799 , "jobD":10.0 , "preS":'' , "preD":'' , "cS":1799 , "cD":5.0 , "gS":'' , "gD":'' , "eS":1804 , "eD":0.0 , "kS":1799 , "kD":2.142 , "postS":1804 , "postD":5.0 , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
{
"name":"cleanup_example_workflow_0_local" , "jobS":1814 , "jobD":5.0 , "preS":'' , "preD":'' , "cS":1814 , "cD":5.0 , "gS":'' , "gD":'' , "eS":1819 , "eD":0.0 , "kS":1819 , "kD":0.0 , "postS":'' , "postD":'' , "state":3 , "transformation": "pegasus::cleanup"  , "color": "#80b1d3"  , "sub_wf":0 , "sub_wf_name":''},
];