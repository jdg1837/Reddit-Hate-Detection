import praw

def get_user_karma(u):
    userAgent = 'test'
    clientId = 'IT6Gc73BtGDJwg'
    clientSecret = 'fWgdfjr2gDdTX5YNo1jKZZqiRAo'
    r = praw.Reddit(user_agent=userAgent, client_id=clientId, client_secret=clientSecret)
    user = r.redditor(u)
    return user.link_karma, user.comment_karma