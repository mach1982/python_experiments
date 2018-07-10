import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = '4PCu8J76Zh0WugAiE0U4Hx4Ut'
        consumer_secret = 'cYTu24qxaobPGy8OKxtozfPnQBXPcB6FSnNkkTVsJ7AWL9gU63'
        access_token = '16225523-S7xirZGBa4BUUHCJ8uCRGHboy5poeB3shFk9MiZFR'
        access_token_secret = '7X48RTgSm6d6ztTKlBQ1OWjUGJyVNnmkroRR7gtxDmGTR'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def irl():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#IRL #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Ireland: {} %".format(round(100*len(ptweets)/len(tweets))))

def uk():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#GBR #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets UK: {} %".format(round(100*len(ptweets)/len(tweets))))

def fra():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#FRA #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets France: {} %".format(round(100*len(ptweets)/len(tweets))))

def esp():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#ESP #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Spain: {} %".format(round(100*len(ptweets)/len(tweets))))

def por():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
        # calling function to get tweets
    tweets = api.get_tweets(query = '#POR #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Portugal: {} %".format(round(100*len(ptweets)/len(tweets))))

def ger():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#GER #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Germany: {} %".format(round(100*len(ptweets)/len(tweets))))

def ita():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#ITA #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Italy: {} %".format(round(100*len(ptweets)/len(tweets))))

def ukr():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#UKR #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Ukraine: {} %".format(round(100*len(ptweets)/len(tweets))))

def nor():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#NOR #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Norway: {} %".format(round(100*len(ptweets)/len(tweets))))

def fin():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#FIN #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Finland: {} %".format(round(100*len(ptweets)/len(tweets))))

def den():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#DEN #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Denmark: {} %".format(round(100*len(ptweets)/len(tweets))))

def swe():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#SWE #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Sweden: {} %".format(round(100*len(ptweets)/len(tweets))))


def ned():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#NED #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Netherlands: {} %".format(round(100*len(ptweets)/len(tweets))))


def hun():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#HUN #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Hungary: {} %".format(round(100*len(ptweets)/len(tweets))))

def cze():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#CZE #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Czech Republic: {} %".format(round(100*len(ptweets)/len(tweets))))

def cyp():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#CYP #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Cyprus: {} %".format(round(100*len(ptweets)/len(tweets))))

def bgr():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#BGR #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Bulgaria: {} %".format(round(100*len(ptweets)/len(tweets))))


def mda():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#MDA #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Moldova: {} %".format(round(100*len(ptweets)/len(tweets))))


def isr():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#ISR #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Israel: {} %".format(round(100*len(ptweets)/len(tweets))))

def slo():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#SLO #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Slovenia: {} %".format(round(100*len(ptweets)/len(tweets))))

def ltu():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#LTU #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Lithuania: {} %".format(round(100*len(ptweets)/len(tweets))))

def aut():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#AUT #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Austria: {} %".format(round(100*len(ptweets)/len(tweets))))

def est():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#EST #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Estonia: {} %".format(round(100*len(ptweets)/len(tweets))))


def srb():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#SRB #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Serbia: {} %".format(round(100*len(ptweets)/len(tweets))))


def alb():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#ALB #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Albania: {} %".format(round(100*len(ptweets)/len(tweets))))


def aus():
    # creating object of TwitterClient Class    print("1")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = '#AUS #Eurovsion', count =1000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets Australia: {} %".format(round(100*len(ptweets)/len(tweets))))









def main():
    irl()
    uk()
    fra()
    esp()
    por()
    ger()
    ita()
    ukr()
    nor()
    fin()
    den()
    swe()
    ned()
    hun()
    cze()
    bgr()
    mda()
    isr()
    ltu()
    aut()
    est()
    srb()
    alb()
    aus()





if __name__ == "__main__":
    # calling main function
    main()
