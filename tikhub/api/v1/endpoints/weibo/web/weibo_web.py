# 导入API SDK Client类
import json

from tikhub.client.api_client import APIClient

class WeiboWeb:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client


    # 获取单个作品数据 | Get single video data
    async def fetch_post_detail(self, id: str):
        endpoint = "/api/v1/weibo/web/fetch_post_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?id={id}")
        return data

    # 获取用户信息 | Get user information
    async def fetch_user_info(self, uid: str):
        endpoint = "/api/v1/weibo/web/fetch_user_info"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}")
        return data

    # 获取微博用户文章数据 | Get Weibo user article data
    async def fetch_user_posts(self, uid: str, page: int, feature: int):
        endpoint = "/api/v1/weibo/web/fetch_user_posts"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}&page={page}&feature={feature}")
        return data

if __name__ == "__main__":
    import asyncio

    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        weibo_web = WeiboWeb(client)

        # 获取单个作品数据 | Get single video data
        data = await weibo_web.fetch_post_detail("5008127060086127")
        print(data)

        # 获取用户信息 | Get user information
        data = await weibo_web.fetch_user_info("7277477906")
        print(data)

        # 获取微博用户文章数据 | Get Weibo user article data
        data = await weibo_web.fetch_user_posts("7277477906", 1, 0)
        print(data)

    asyncio.run(main())
