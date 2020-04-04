import json

output_file = 'out.json'

def write(data):
    with open(output_file, 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read(filename):
    with open(output_file, 'r+', encoding='utf-8') as f:    
        old_data = json.load(f)
    return old_data

def update(new_data):
    data = read(output_file)
    data["data"] += new_data["data"]
    return data

def set_output_file(filename):
    global output_file
    output_file = filename