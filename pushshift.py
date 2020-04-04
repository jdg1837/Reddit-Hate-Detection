import requests
import json_io
import json

def request_data(sub, size, fields, epoch, initial):
    url = 'https://api.pushshift.io/reddit/search/comment/?subreddit='+str(sub)+'&size='+str(size)+'&fields='+str(fields)+'&before='+str(epoch)
    #print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    obj_num = len(data["data"])

    # for datum in data["data"]:
    #     print(datum["body"])

    epoch = data["data"][obj_num-1]["created_utc"]

    if not initial:
        data = json_io.update(data)
    
    json_io.write(data)
    
    return epoch
