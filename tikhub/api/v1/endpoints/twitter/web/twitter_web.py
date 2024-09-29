# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class TwitterWeb:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # Fetch tweet detail | 获取推文详情
    async def fetch_tweet_detail(self, tweet_id: str):
        endpoint = "/api/v1/twitter/web/fetch_tweet_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?tweet_id={tweet_id}")
        return data

    # Fetch user profile | 获取用户资料
    async def fetch_user_profile(self, screen_name: str = None, rest_id: int = None):
        endpoint = "/api/v1/twitter/web/fetch_user_profile"
        params = []
        if screen_name:
            params.append(f"screen_name={screen_name}")
        if rest_id:
            params.append(f"rest_id={rest_id}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch user post tweet | 获取用户发帖
    async def fetch_user_post_tweet(self, screen_name: str = None, rest_id: int = None, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_user_post_tweet"
        params = []
        if screen_name:
            params.append(f"screen_name={screen_name}")
        if rest_id:
            params.append(f"rest_id={rest_id}")
        if cursor:
            params.append(f"cursor={cursor}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch search timeline | 搜索
    async def fetch_search_timeline(self, keyword: str, search_type: str = "Top", cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_search_timeline"
        params = [f"keyword={keyword}", f"search_type={search_type}"]
        if cursor:
            params.append(f"cursor={cursor}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch post comments | 获取评论
    async def fetch_post_comments(self, tweet_id: str, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_post_comments"
        params = [f"tweet_id={tweet_id}"]
        if cursor:
            params.append(f"cursor={cursor}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch latest post comments | 获取最新的推文评论
    async def fetch_latest_post_comments(self, tweet_id: str, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_latest_post_comments"
        params = [f"tweet_id={tweet_id}"]
        if cursor:
            params.append(f"cursor={cursor}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch user tweet replies | 获取用户推文回复
    async def fetch_user_tweet_replies(self, screen_name: str, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_user_tweet_replies"
        params = [f"screen_name={screen_name}"]
        if cursor:
            params.append(f"cursor={cursor}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch user highlights tweets | 获取用户高光推文
    async def fetch_user_highlights_tweets(self, user_id: str, count: int = 20, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_user_highlights_tweets"
        params = [f"userId={user_id}", f"count={count}"]
        if cursor:
            params.append(f"cursor={cursor}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch user media | 获取用户媒体
    async def fetch_user_media(self, screen_name: str = None, rest_id: int = None):
        endpoint = "/api/v1/twitter/web/fetch_user_media"
        params = []
        if screen_name:
            params.append(f"screen_name={screen_name}")
        if rest_id:
            params.append(f"rest_id={rest_id}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch retweet user list | 转推用户列表
    async def fetch_retweet_user_list(self, tweet_id: str, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_retweet_user_list"
        params = [f"tweet_id={tweet_id}"]
        if cursor:
            params.append(f"cursor={cursor}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch trending | 趋势
    async def fetch_trending(self, country: str = "UnitedStates"):
        endpoint = "/api/v1/twitter/web/fetch_trending"
        data = await self.client.fetch_get_json(f"{endpoint}?country={country}")
        return data

    # Fetch user followings | 用户关注
    async def fetch_user_followings(self, screen_name: str, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_user_followings"
        params = [f"screen_name={screen_name}"]
        if cursor:
            params.append(f"cursor={cursor}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

    # Fetch user followers | 用户粉丝
    async def fetch_user_followers(self, screen_name: str, cursor: str = None):
        endpoint = "/api/v1/twitter/web/fetch_user_followers"
        params = [f"screen_name={screen_name}"]
        if cursor:
            params.append(f"cursor={cursor}")
        query = "&".join(params)
        data = await self.client.fetch_get_json(f"{endpoint}?{query}")
        return data

