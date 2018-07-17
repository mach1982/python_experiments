from textblob import TextBlob
import tweepy

consumer_key =<consumer_key>
consumer_secert=<consumer_secert>

access_token=<access_token=>
accces_secert=<access_token=>

auth = tweepy.OAuthHandler(consumer_key,consumer_secert)
auth.set_access_token(access_token,accces_secert)

api =tweepy.API(auth)

tweets= api.search('#trump',count=500)
countn=0
countp=0
for tweet in tweets:
    #print(tweet.text)
    analysis= TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
       countp += 1
    elif analysis.sentiment.polarity == 0:
        countn +=1
    else:
        print('Nutral')
print('Negative {}'.format(countn))
print('Positive {}'.format(countp))
