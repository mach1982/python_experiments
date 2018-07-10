import tweepy
import pandas as pd

consumer_key = '4PCu8J76Zh0WugAiE0U4Hx4Ut'
consumer_secert = 'cYTu24qxaobPGy8OKxtozfPnQBXPcB6FSnNkkTVsJ7AWL9gU63'

access_token = '16225523-S7xirZGBa4BUUHCJ8uCRGHboy5poeB3shFk9MiZFR'
accces_secert = '7X48RTgSm6d6ztTKlBQ1OWjUGJyVNnmkroRR7gtxDmGTR'

auth = tweepy.OAuthHandler(consumer_key,consumer_secert)
auth.set_access_token(access_token,accces_secert)

api = tweepy.API(auth,wait_on_rate_limit=False)

tweets = api.search("#Eurovsion")



tweets_df = pd.DataFrame(vars(tweets[i]) for i in range(len(tweets)))
tweets_df.to_csv(t.csv)
print("Finished")
