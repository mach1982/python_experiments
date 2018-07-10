from textblob import TextBlob
import tweepy

consumer_key ='4PCu8J76Zh0WugAiE0U4Hx4Ut'
consumer_secert='cYTu24qxaobPGy8OKxtozfPnQBXPcB6FSnNkkTVsJ7AWL9gU63'

access_token='16225523-S7xirZGBa4BUUHCJ8uCRGHboy5poeB3shFk9MiZFR'
accces_secert='7X48RTgSm6d6ztTKlBQ1OWjUGJyVNnmkroRR7gtxDmGTR'

auth = tweepy.OAuthHandler(consumer_key,consumer_secert)
auth.set_access_token(access_token,accces_secert)

api =tweepy.API(auth)

tweets= api.search('#Repealthe8th',count=500)

for tweet in tweets:
    #print(tweet.text)
    analysis= TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        print('y')
    elif analysis.sentiment.polarity == 0:
        print('n')
    else:
        print('0')
