#This file is part of azulejo
#
# Author: Pedro
#
#This code takes care of setting up or loading configurations.
#Do not edit this file directly. This is only used for bootstrap, once executed,
#this script will write configurations to ~/.azulejorc.js. If you want to
#personalize shortcuts and geometries, edit that file instead.
#

import json
import os.path


raw_json = """
[
{
"name" : "side-by-syde",
"keybind": "<Super>2",
"function" : "resize_windows",
"parameters":[
	[0,0,"w/2","h"],
	["w/2+1",0,"w/2","h"]
	]
},

{
"name":"four-pane",
"keybind": "<Super>4",
"function" : "resize_windows",
"parameters":[
	[0,0,"w/2","h/2"],
	["w/2+1",0,"w/2","h/2"],
	[0,"h/2+1","w/2","h/2"],
	["w/2+1","h/2+1","w/2","h/2"]
	]
},

{
"name":"one-big-two-small",
"keybind": "<Super>3",
"function" : "resize_windows",
"parameters":[
	[0,0,"w*0.5","h"],
	["w*0.5+1",0,"w*0.5","h/2"],
	["w*0.5+1","h/2+1","w*0.5","h/2"]
	]
},

{
"name":"window-to-te-left-side",
"description": "move window to the left part of the screen, cycle through possible geometries",
"keybind": "<Super>h",
"function" : "resize_single_window",
"parameters":[
	[0,0,"w*0.5","h"],
	[0,0,"w*0.3","h"],
	[0,0,"w*0.7","h"]
	]
},

{
"name":"window-to-the-right-side",
"description": "move window to the right part of the screen, cycle through possible geometries",
"keybind": "<Super>k",
"function" : "resize_single_window",
"parameters":[
	["w*0.5",0,"w*0.5","h"],
	["w*0.7",0,"w*0.3","h"],
	["w*0.3",0,"w*0.7","h"]
	]
},

{
"name":"rotate-windows-positions",
"description": "rotates windows' positions, rotation queue will be the size of last arrangement or, if smaller, the number of visible windows ",
"keybind": "<Super>r",
"function" : "rotate_windows",
"parameters":[]
}

]
"""

conf_filename = os.path.expanduser('.azulejorc.js')
if not os.path.isfile(conf_filename):
	fw = open(conf_filename, 'w')
	fw.write(raw_json)
	fw.close

fr = open(conf_filename, 'r')
json_string = fr.read()
fr.close()
conf_data = json.loads(json_string)

