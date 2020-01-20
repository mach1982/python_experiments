from textblob import TextBlob
import tweepy

consumer_key = 'consumer_key '
consumer_secret = 'consumer_secret
access_token = 'access_token 
access_token_secret = 'access_token_secret '

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,accces_secert)

api =tweepy.API(auth)



tweets= api.search('#Brexit',count=1000)
countn=0
countp=0
countne=0
for tweet in tweets:
    #print(tweet.text)
    analysis= TextBlob(tweet.text)
   # print(analysis.sentiment)
    if analysis.sentiment.polarity > 0:
       countp += 1
    elif analysis.sentiment.polarity == 0:
        countn +=1
    else:
       countne +=1

print('Positive {}'.format(countp))
print('Negative {}'.format(countn))
print('Nutral {}'.format(countne))
print('Total tweets scanned : {}'.format(countn+countp+countne))

