import json

def write_data_to_file(data, file_name):
    """
    Write data to a file in JSON format.
    Args:
        data (dict): The data to write to the file.
        file_name (str): The name of the file to write the data to.
    """
    with open(file_name, 'w') as f:
        json.dump(data, f)

def read_data_from_file(file_name):
    """
    Read data from a JSON file.
    Args:
        file_name (str): The name of the file to read the data from.
    Returns:
        dict: The data read from the file.
    """
    with open(file_name, 'r') as f:
        return json.load(f)
