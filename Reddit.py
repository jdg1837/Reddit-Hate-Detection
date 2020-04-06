import karma
import json_io
import requests
import json

def request_data(sub, size, fields, epoch, initial, users):
    url = 'https://api.pushshift.io/reddit/search/comment/?subreddit='+str(sub)+'&size='+str(size)+'&fields='+str(fields)+'&before='+str(epoch)
    #print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    obj_num = len(data["data"])

    if obj_num == 0:
        return epoch, -1

    # for datum in data["data"]:
    #     u = datum["author"]
    #     if u == '[deleted]':
    #         continue
    #     if u not in users.keys():
    #         link_karma, comment_karma = karma.get_user_karma(u)
    #         users[u] = (link_karma,comment_karma)

    epoch = data["data"][obj_num-1]["created_utc"]

    if not initial:
        data = json_io.update(data)
    
    json_io.write(data)
    
    return epoch, obj_num