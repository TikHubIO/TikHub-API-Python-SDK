# 导入API SDK Client类

from tikhub.http_client.api_client import APIClient

# 标记已废弃的方法
from tikhub.http_client.deprecated import deprecated


class XiguaAppV2:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取单个作品数据 | Get single video data
    async def fetch_one_video(self, item_id: str):
        endpoint = f"/api/v1/xigua/app/v2/fetch_one_video"
        data = await self.client.fetch_get_json(f"{endpoint}?item_id={item_id}")
        return data

    # 视频评论列表 | Video comment list
    async def fetch_video_comment_list(self, item_id: str, offset: int = 0, count: int = 20):
        endpoint = f"/api/v1/xigua/app/v2/fetch_video_comment_list"
        data = await self.client.fetch_get_json(f"{endpoint}?item_id={item_id}&offset={offset}&count={count}")
        return data

    # 搜索视频 | Search video
    async def search_video(self, keyword: str, offset: int = 0, order_type: str = None, min_duration: int = None, max_duration: int = None):
        endpoint = f"/api/v1/xigua/app/v2/search_video"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&order_type={order_type}&min_duration={min_duration}&max_duration={max_duration}")
        return data

    # 个人信息 | Personal information
    async def fetch_user_info(self, user_id: str):
        endpoint = f"/api/v1/xigua/app/v2/fetch_user_info"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}")
        return data

    # 获取个人作品列表 | Get user post list
    async def fetch_user_post_list(self, user_id: str, max_behot_time: str = None):
        endpoint = f"/api/v1/xigua/app/v2/fetch_user_post_list"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}&max_behot_time={max_behot_time}")
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        xigua_app_v2 = XiguaAppV2(client)

    asyncio.run(main())
