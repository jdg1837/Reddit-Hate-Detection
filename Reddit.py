import file_io
import requests
import time
import json

def url_request(url):
    try:
        return requests.get(url)
    except Exception:
        time.sleep(1)
        return url_request(url)

def request_data(sub, size, fields, epoch, initial, users):
    url = 'https://api.pushshift.io/reddit/search/comment/?subreddit='+str(sub)+'&size='+str(size)+'&fields='+str(fields)+'&before='+str(epoch)
    #print(url)
    r = url_request(url)
    data = json.loads(r.text)
    obj_num = len(data["data"])

    if obj_num == 0:
        return epoch, -1

    for datum in data["data"]:
        u = datum["author"]
        if u == '[deleted]':
            continue
        if u not in users:
            users.append(u)

    epoch = data["data"][obj_num-1]["created_utc"]

    if not initial:
        data = file_io.update(data)
    
    file_io.write(data)
    
    return epoch, obj_num