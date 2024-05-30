import asyncio
from tikhub.sdk import Client


async def main():
    client = Client(base_url="https://beta.tikhub.io", api_key="l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw==")

    # 请求用户信息 | Request user info
    user_info = await client.TikHubUser.get_user_info()
    print(user_info)

    # 请求用户每日使用情况 | Request user daily usage
    user_daily_usage = await client.TikHubUser.get_user_daily_usage()
    print(user_daily_usage)

    # 计算价格 | Calculate price
    price = await client.TikHubUser.calculate_price(endpoint="/api/v1/douyin/app/v1/fetch_one_video", request_per_day=100)
    print(price)

    # 获取阶梯式折扣百分比信息 | Get tiered discount percentage information
    tiered_discount_info = await client.TikHubUser.get_tiered_discount_info()
    print(tiered_discount_info)

    # 获取一个端点的信息 | Get information of an endpoint
    endpoint_info = await client.TikHubUser.get_endpoint_info(endpoint="/api/v1/douyin/app/v1/fetch_one_video")
    print(endpoint_info)

    # 获取所有端点信息 | Get all endpoints information
    all_endpoints_info = await client.TikHubUser.get_all_endpoints_info()
    print(all_endpoints_info)


asyncio.run(main())
