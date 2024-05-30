# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class InstagramWeb:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取用户信息 | Fetch user info
    async def fetch_user_info(self, username: str):
        endpoint = "/api/v1/instagram/web/user_info"
        data = await self.client.fetch_get_json(f"{endpoint}?username={username}")
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        instagram_web = InstagramWeb(client)

        # 获取用户信息 | Fetch user info
        data = await instagram_web.fetch_user_info("instagram")
        print(data)


    asyncio.run(main())


