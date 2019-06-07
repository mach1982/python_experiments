import tweepy

with open('twitter_creads.txt', 'r') as twitter_creds:
    creds = twitter_creds.read()
    auth_creds =creds.split(" ")

    

    consumer_key = auth_creds[0]
    consumer_secret = auth_creds[1]
    access_token = auth_creds[2]
    access_token_secert = auth_creds[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secert)

api = tweepy.API(auth)

api.update_status('I am tweeting from #Python')
print("Tweet Sent!")