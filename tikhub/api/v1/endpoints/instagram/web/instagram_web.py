# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class InstagramWeb:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 根据用户名获取用户数据 | Get user data by username
    async def fetch_user_info_by_username(self, username: str):
        endpoint = "/api/v1/instagram/web_app/fetch_user_info_by_username"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}")
        return data

    # 根据用户ID获取用户数据 | Get user data by user ID
    async def fetch_user_info_by_user_id(self, user_id: str):
        endpoint = "/api/v1/instagram/web_app/fetch_user_info_by_user_id"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}")
        return data

    # 根据用户名获取用户数据V2 | Get user data by username V2
    async def fetch_user_info_by_user_id_v2(self, username: str):
        endpoint = "/api/v1/instagram/web_app/fetch_user_info_by_user_id_v2"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={username}")
        return data

    # 根据用户ID获取用户数据V2 | Get user data by user ID V2
    async def fetch_user_info_by_id_v2(self, user_id: str):
        endpoint = "/api/v1/instagram/web_app/fetch_user_info_by_user_id_v2"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}")
        return data

    # 根据用户ID获取用户数据关于信息 | Get user data about by user ID
    async def fetch_user_about_info_by_user_id(self, user_id: str):
        endpoint = "/api/v1/instagram/web_app/fetch_user_about_info_by_user_id"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}")
        return data

    # 根据用户名获取用户网页接口的个人信息 | Get user info by username web API
    async def fetch_user_info_by_username_web(self, username: str):
        endpoint = "/api/v1/instagram/web_app/fetch_user_info_by_username_web"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}")
        return data

    # 根据用户名获取用户的粉丝数据 | Get user followers by username
    async def fetch_user_followers_by_username(self, username: str, pagination_token: str = None):
        endpoint = "/api/v1/instagram/web_app/fetch_user_followers_by_username"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}&pagination_token={pagination_token}")
        return data

    # 根据用户名获取用户的正在关注的用户数据 | Get user followings by username
    async def fetch_user_following_by_username(self, username: str, pagination_token: str = None):
        endpoint = "/api/v1/instagram/web_app/fetch_user_following_by_username"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}&pagination_token={pagination_token}")
        return data

    # 根据用户ID获取用户发布的帖子 | Get user posts by user ID
    async def fetch_user_posts_by_user_id(self, user_id: str, count: int = 12, end_cursor: str = None):
        endpoint = "/api/v1/instagram/web_app/fetch_user_posts_by_user_id"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}&count={count}&end_cursor={end_cursor}")
        return data

    # 根据用户ID获取用户发布的快拍 | Get user reels by user ID
    async def fetch_user_reels_by_user_id(self, user_id: str, count: int = 12, max_id: str = None):
        endpoint = "/api/v1/instagram/web_app/fetch_user_reels_by_user_id"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}&count={count}&max_id={max_id}")
        return data

    # 根据用户ID获取用户被标记的帖子 | Get user tagged posts by user ID
    async def fetch_user_tagged_posts_by_user_id(self, user_id: str, count: int = 12, end_cursor: str = None):
        endpoint = "/api/v1/instagram/web_app/fetch_user_tagged_posts_by_user_id"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}&count={count}&end_cursor={end_cursor}")
        return data

    # 根据用户ID获取与用户相关的其他用户 | Get user related users by user ID
    async def fetch_related_users_by_user_id(self, user_id: str):
        endpoint = "/api/v1/instagram/web_app/fetch_related_users_by_user_id"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}")
        return data

    # 根据用户名获取相似的账户数据 | Get similar accounts by username
    async def fetch_similar_accounts_by_username(self, username: str):
        endpoint = "/api/v1/instagram/web_app/fetch_similar_accounts_by_username"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}")
        return data


    # 根据关键词搜索用户 | Search users by query
    async def fetch_search_users_by_keyword(self, keyword: str):
        endpoint = "/api/v1/instagram/web_app/fetch_search_users_by_keyword"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}")
        return data

    # 根据URL获取帖子数据 | Get post data by URL
    async def fetch_post_info_by_url(self, url: str):
        endpoint = "/api/v1/instagram/web_app/fetch_post_info_by_url"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 根据帖子ID获取帖子数据 | Get post data by post ID
    async def fetch_post_info_by_post_id(self, post_id: str):
        endpoint = "/api/v1/instagram/web_app/fetch_post_info_by_post_id"
        data = await self.client.fetch_get_json(f"{endpoint}?post_id={post_id}")
        return data

    # 根据帖子URL获取媒体数据 | Get media data by URL
    async def fetch_post_media_by_url(self, url: str):
        endpoint = "/api/v1/instagram/web_app/fetch_post_media_by_url"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 根据音乐ID获取音乐数据 | Get music data by music ID
    async def fetch_music_info_by_music_id(self, music_id: str):
        endpoint = "/api/v1/instagram/web_app/fetch_music_info_by_music_id"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}")
        return data

    # 根据关键词搜索话题数据 | Search hashtags by query
    async def fetch_search_hashtags_by_keyword(self, keyword: str):
        endpoint = "/api/v1/instagram/web_app/fetch_search_hashtags_by_keyword"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}")
        return data

    # 根据关键词获取话题帖子 | Get hashtag posts by query
    async def fetch_hashtag_posts_by_keyword(self, keyword: str, end_cursor: str = None):
        endpoint = "/api/v1/instagram/web_app/fetch_hashtag_posts_by_keyword"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&end_cursor={end_cursor}")
        return data

    # 根据关键词搜索地点数据 | Search locations by query
    async def fetch_search_locations_by_keyword(self, keyword: str):
        endpoint = "/api/v1/instagram/web_app/fetch_search_locations_by_keyword"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}")
        return data

    # 根据地点ID获取地点相关的帖子 | Get location posts by location ID
    async def fetch_location_posts_by_location_id(self, location_id: str, max_id: str = None):
        endpoint = "/api/v1/instagram/web_app/fetch_location_posts_by_location_id"
        data = await self.client.fetch_get_json(f"{endpoint}?location_id={location_id}&max_id={max_id}")
        return data

    # 综合搜索 | Search all by query
    async def fetch_global_search(self, keyword: str):
        endpoint = "/api/v1/instagram/web_app/fetch_global_search"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}")
        return data

    # 根据用户名获取用户的Reels数据V2 | Get user reels by username V2
    async def fetch_user_reels_by_username_v2(self, username: str, pagination_token: str = None):
        endpoint = "/api/v1/instagram/web_app/fetch_user_reels_by_username_v2"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}&pagination_token={pagination_token}")
        return data

    # 根据用户名获取用户的Stories数据 | Get user stories by username
    async def fetch_user_stories_by_username(self, username: str):
        endpoint = "/api/v1/instagram/web_app/fetch_user_stories_by_username"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}")
        return data

    # 根据用户名获取用户的highlights数据 | Get user highlights by username
    async def fetch_user_highlights_by_username(self, username: str):
        endpoint = "/api/v1/instagram/web_app/fetch_user_highlights_by_username"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}")
        return data

    # 根据用户名获取用户的tv_posts数据 | Get user tv_posts by username
    async def fetch_user_tv_posts_by_username(self, username: str, pagination_token: str = None):
        endpoint = "/api/v1/instagram/web_app/fetch_user_tv_posts_by_username"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}&pagination_token={pagination_token}")
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        instagram_web = InstagramWeb(client)

        # 获取用户信息 | Fetch user info
        data = await instagram_web.fetch_user_info_by_username("instagram")
        print(data)


    asyncio.run(main())


