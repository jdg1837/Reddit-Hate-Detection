import praw


def get_user_karma():
    userAgent = 'test'
    clientId = 'IT6Gc73BtGDJwg'
    clientSecret = 'fWgdfjr2gDdTX5YNo1jKZZqiRAo'
    r = praw.Reddit(user_agent=userAgent, client_id=clientId, client_secret=clientSecret)
    user = r.redditor('SuspiciousElderberry')
    print(user.link_karma)
    print(user.comment_karma)