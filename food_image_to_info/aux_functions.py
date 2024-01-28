import os
import json


## list all files in a directory
def list_files(directory):
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            yield full_path


## import json file as dictionary
def import_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data