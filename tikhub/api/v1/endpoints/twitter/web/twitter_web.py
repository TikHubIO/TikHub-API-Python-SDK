# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class TwitterWeb:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # Fetch tweet detail | 获取推文详情
    async def fetch_tweet_detail(self, focalTweetId: str):
        endpoint = "/api/v1/twitter/web/fetch_tweet_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?focalTweetId={focalTweetId}")
        return data

    # Fetch user profile | 获取用户资料
    async def fetch_user_profile(self, screen_name: str):
        endpoint = "/api/v1/twitter/web/fetch_user_profile"
        data = await self.client.fetch_get_json(f"{endpoint}?screen_name={screen_name}")
        return data

    # Fetch user post tweet | 获取用户发帖
    async def fetch_user_post_tweet(self, userId: str, count: int = 20, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_user_post_tweet"
        data = await self.client.fetch_get_json(f"{endpoint}?userId={userId}&count={count}&cursor={cursor}")
        return data
