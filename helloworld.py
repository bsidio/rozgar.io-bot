import tweepy

consumer_key = 'Bh8CetMcGwMjTRgf0yx2oOts9'
consumer_secret = 'c70kVPrJgKl5mfj45h69W8a2kTTOs6nXMFOvz47LPJRDVOw1R1'
access_token = '881276163540140032-03bBNHx7kHNxuWrG6Zas6ewnN7qYT0H'
access_token_secret = 'UDyE8GGnlxRFumELoNxt5zANyttpAIbeimdJcveZTVBO3'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = 'Hello, world!First Tweet from Sids Bot'
api.update_status(status=tweet)
