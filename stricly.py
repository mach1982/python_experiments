from textblob import TextBlob
import tweepy

consumer_key = '4PCu8J76Zh0WugAiE0U4Hx4Ut'
consumer_secret = 'cYTu24qxaobPGy8OKxtozfPnQBXPcB6FSnNkkTVsJ7AWL9gU63'
access_token = '16225523-S7xirZGBa4BUUHCJ8uCRGHboy5poeB3shFk9MiZFR'
accces_secert = '7X48RTgSm6d6ztTKlBQ1OWjUGJyVNnmkroRR7gtxDmGTR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, accces_secert)

api = tweepy.API(auth)

with open('celbs.txt', 'r') as myfile2:
        data2 = myfile2.read()
        celbs = data2.split(",")
f = open("output.txt", "w")

for c in celbs:

    tweets = api.search(c, count=100)
    countn = 0
    countp = 0
    countne = 0
    for tweet in tweets:
        # print(tweet.text)
        analysis = TextBlob(tweet.text)
        # print(analysis.sentiment)
        if analysis.sentiment.polarity > 0:
            countp += 1
        elif analysis.sentiment.polarity == 0:
            countn += 1
        else:
            countne += 1


    print(c)
    f.write('Name {}\n'.format(c))
    print('Positive {}'.format(countp))
    f.write('Positive {}\n'.format(countp))
    print('Negative {}'.format(countn))
    f.write('Negative {}\n'.format(countn))
    print('Neutral {}'.format(countne))
    f.write('Neutral {}\n'.format(countne))
    print('Total tweets scanned : {}'.format(countn + countp + countne))






