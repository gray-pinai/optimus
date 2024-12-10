import tweepy
from datetime import datetime

from config import CONFIG


class TwitterService:

    #tweepy client实例化
    client = None

    def __init__(self):
        #init client
        self.client = tweepy.Client(
            bearer_token = CONFIG["twitter_api"]["bearer_token"],
            consumer_key = CONFIG["twitter_api"]["api_key"],
            consumer_secret = CONFIG["twitter_api"]["api_secret"],
            access_token = CONFIG["twitter_api"]["access_token"],
            access_token_secret = CONFIG["twitter_api"]["access_token_secret"]
        )

    #向tt发送一条推文
    async def send(self, content: str):
        response = self.client.create_tweet(text=content)
        return response
    
    #从tt获取timeline数据
    async def fetch_data(self, account: str, start_time: datetime, end_time: datetime):
        twitter_user = self.client.get_user(username=account).data
        twitter_contents = self.client.get_users_tweets(
            twitter_user.id,
            start_time=start_time,
            end_time=end_time,
            tweet_fields=['id', 'created_at', 'text', 'author_id']
        )

        return twitter_contents

    