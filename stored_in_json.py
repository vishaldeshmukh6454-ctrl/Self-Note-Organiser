import json

def write_data(data,file_name):
    """This function writes data to json file"""
    try:
        with open(f'{file_name}.json', 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(e)
