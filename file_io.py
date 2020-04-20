import json

output_file = 'out.json'

def write(data):
    with open(output_file, 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read(filename):
    with open(filename, 'r+', encoding='utf-8') as f:    
        old_data = json.load(f)
    return old_data

def update(new_data):
    data = read(output_file)
    data["data"] += new_data["data"]
    return data

def extract_data(sub,src):
    src_file = src + '/' + sub + '_' + src + '.json'
    old_data = read(src_file)
    epoch = old_data["data"][-1]["created_utc"]
    count = len(old_data["data"])
    write(old_data)
    return epoch, count

def set_output_file(filename):
    global output_file
    output_file = filename

def read_parameters(filename):
    with open(filename, 'r+', encoding='utf-8') as f:    
        data = json.load(f)
    return data["method"],data["subs"],int(data["start"]),int(data["end"]),data["fields"],int(data["k"]),data["src"],data["dst"],bool(data["extend"])

def write_to_txt(data,filename):
    with open(filename, 'w',encoding='utf-8') as f:
        for datum in data:
            f.write(datum)