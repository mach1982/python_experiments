from textblob import TextBlob
import tweepy

consumer_key = ' ypur consumer_key'
consumer_secret = 'your  consumer_secre'
access_token = 'your access_token '
accces_secert= 'accces_secert'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,accces_secert)

api =tweepy.API(auth)



tweets= api.search('Ashley Roberts',count=100)
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

