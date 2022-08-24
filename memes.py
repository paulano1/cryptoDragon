import praw

client_id = "3DRl_uwOvzX-OQKm3UTUVQ"
client_secret = 'uhhOUVmC4gZS2iRCmSS29r7gwsTj9A'
user_id = 'Ok_Dev_5899'
user_password = "Azqsxwdc67"
user_agent = "cryptoDragon123"

reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, user_id = user_id, user_password = user_password, user_agent = user_agent)

subreddit = reddit.subreddit("cryptocurrencymemes")

top = subreddit.top(limit = 10)

for sub in top:
    print(sub.url)

