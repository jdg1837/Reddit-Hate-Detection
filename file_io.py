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

def read_parameters(filename):
    with open(filename, 'r+', encoding='utf-8') as f:    
        data = json.load(f)
    return data["subs"],int(data["start"]),int(data["end"]),data["fields"],int(data["k"]),int(data["count"])

def write_to_txt(data,filename):
    with open(filename, 'w',encoding='utf-8') as f:
        for datum in data:
            f.write('%s\n',datum)