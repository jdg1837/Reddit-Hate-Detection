import file_io
import requests
import time
import json
import praw

def url_request(url):
    try:
        return requests.get(url)
    except Exception:
        time.sleep(1)
        return url_request(url)

def request_data(sub, size, fields, epoch, initial):
    url = 'https://api.pushshift.io/reddit/search/comment/?subreddit='+str(sub)+'&size='+str(size)+'&fields='+str(fields)+'&before='+str(epoch)
    #print(url)
    r = url_request(url)
    data = json.loads(r.text)
    obj_num = len(data["data"])

    if obj_num == 0:
        return epoch, -1

    epoch = data["data"][obj_num-1]["created_utc"]

    if not initial:
        data = file_io.update(data)
    
    file_io.write(data)
    
    return epoch, obj_num

def get_user_karma(u):
    userAgent = 'test'
    clientId = 'IT6Gc73BtGDJwg'
    clientSecret = 'fWgdfjr2gDdTX5YNo1jKZZqiRAo'
    r = praw.Reddit(user_agent=userAgent, client_id=clientId, client_secret=clientSecret)
    user = r.redditor(u)
    return user.link_karma, user.comment_karma