import tweepy
from src.config import BEARER_TOKEN

def post_tweet(tweet_text):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    client.create_tweet(text=tweet_text, user_auth=False)
    print(f"Tweeted: {tweet_text}")