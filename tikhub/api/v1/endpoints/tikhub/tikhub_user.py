# 导入API SDK Client类
import json

from tikhub.client.api_client import APIClient


class TikHubUser:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 根据session_id获取用户信息 | Get TikHub user info
    async def get_user_info(self):
        endpoint = "/api/v1/tikhub/user/get_user_info"
        data = await self.client.fetch_get_json(endpoint)
        return data

    # 获取用户每日使用情况 | Get user daily usage
    async def get_user_daily_usage(self):
        endpoint = "/api/v1/tikhub/user/get_user_daily_usage"
        data = await self.client.fetch_get_json(endpoint)
        return data

    # 计算价格 | Calculate price
    async def calculate_price(self, endpoint: str, request_per_day: int):
        __endpoint = "/api/v1/tikhub/user/calculate_price"
        data = await self.client.fetch_get_json(f"{__endpoint}?endpoint={endpoint}&request_per_day={request_per_day}")
        return data

    # 获取阶梯式折扣百分比信息 | Get tiered discount percentage information
    async def get_tiered_discount_info(self):
        endpoint = "/api/v1/tikhub/user/get_tiered_discount_info"
        data = await self.client.fetch_get_json(endpoint)
        return data

    # 获取一个端点的信息 | Get information of an endpoint
    async def get_endpoint_info(self, endpoint: str):
        __endpoint = "/api/v1/tikhub/user/get_endpoint_info"
        data = await self.client.fetch_get_json(f"{__endpoint}?endpoint={endpoint}")
        return data

    # 获取所有端点信息 | Get all endpoints information
    async def get_all_endpoints_info(self):
        endpoint = "/api/v1/tikhub/user/get_all_endpoints_info"
        data = await self.client.fetch_get_json(endpoint)
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        tikhub_user = TikHubUser(client)

        # 根据session_id获取用户信息 | Get TikHub user info
        data = await tikhub_user.get_user_info()
        print(data)

        # 获取用户每日使用情况 | Get user daily usage
        data = await tikhub_user.get_user_daily_usage()
        print(data)

        # 计算价格 | Calculate price
        data = await tikhub_user.calculate_price(endpoint="/api/v1/douyin/app/v1/fetch_one_video",
                                                 request_per_day=100000)
        print(data)

        # 获取阶梯式折扣百分比信息 | Get tiered discount percentage information
        data = await tikhub_user.get_tiered_discount_info()
        print(data)

        # 获取一个端点的信息 | Get information of an endpoint
        data = await tikhub_user.get_endpoint_info(endpoint="/api/v1/douyin/app/v1/fetch_one_video")
        print(data)

        # 获取所有端点信息 | Get all endpoints information
        data = await tikhub_user.get_all_endpoints_info()
        print(data)


    asyncio.run(main())
