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

    # SearchTimeline | 搜索时间线
    async def fetch_search_timeline(self, rawQuery: str, count: int = 20, product: str = 'Top', cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_search_timeline"
        data = await self.client.fetch_get_json(f"{endpoint}?rawQuery={rawQuery}&count={count}&product={product}&cursor={cursor}")
        return data

    # Post Comments | 获取评论
    async def fetch_post_comments(self, tweetId: str, rankingModel: str = 'Relevance', cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_post_comments"
        data = await self.client.fetch_get_json(f"{endpoint}?tweetId={tweetId}&rankingModel={rankingModel}&cursor={cursor}")
        return data

    # Fetch user tweet replies | 获取用户推文回复
    async def fetch_user_tweet_replies(self, userId: str, count: int = 20, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_user_tweet_replies"
        data = await self.client.fetch_get_json(f"{endpoint}?userId={userId}&count={count}&cursor={cursor}")
        return data

    # UserHighlightsTweets | 获取用户高光推文
    async def fetch_user_highlights_tweets(self, userId: str, count: int = 20, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_user_highlights_tweets"
        data = await self.client.fetch_get_json(f"{endpoint}?userId={userId}&count={count}&cursor={cursor}")
        return data

    # UserMedia | 获取用户媒体
    async def fetch_user_media(self, userId: str, count: int = 20, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_user_media"
        data = await self.client.fetch_get_json(f"{endpoint}?userId={userId}&count={count}&cursor={cursor}")
        return data

