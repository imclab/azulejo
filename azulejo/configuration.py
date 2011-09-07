# This file is part of azulejo
#
# Author: Pedro
#
# This code takes care of setting up or loading configurations.
# Do not edit this file directly. This is only used for bootstrap, once executed,
# this script will write configurations to ~/.azulejorc.js. If you want to
# personalize shortcuts and geometries, edit that file instead.
#

import json
import os.path

def read_file(path):
    """Returns file content as string."""
    file_handler = open(path, 'r')
    content = file_handler.read()
    file_handler.close()
    return content

def get_initial_config_content():
    """Returns the initial config values as string."""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    initial_config_path = os.path.join(this_dir, 'initial_config.json')
    return read_file(initial_config_path)

def create_inicial_config_file(conf_filename):
    """Create a file with config values."""
    fw = open(conf_filename, 'w')
    raw_json = get_initial_config_content()
    fw.write(raw_json)
    fw.close()

conf_filename = os.path.expanduser('~/.azulejorc.js')

if not os.path.isfile(conf_filename):
    print "Starting azulejo by creating file: '%s'" %(conf_filename)
    create_inicial_config_file(conf_filename)

print "Reading config file: '%s'" %(conf_filename)
json_string = read_file(conf_filename)

conf_data = json.loads(json_string)
