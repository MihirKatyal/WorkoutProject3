import json 

def write_data_to_file(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f)

def read_data_from_file(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)