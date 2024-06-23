# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class KuaishouWeb:

    def __init__(self, client: APIClient):
        self.client = client

    # 获取单个作品数据 (Fetch Single Video)
    async def fetch_one_video(self, photo_id: str):
        endpoint = "/api/v1/kuaishou/web/fetch_one_video"
        data = await self.client.fetch_get_json(f"{endpoint}?photo_id={photo_id}")
        return data

    # 获取单个作品评论数据 (Fetch Single Video Comment Data)
    async def fetch_one_video_comment(self, photo_id: str, pcursor: str = None):
        endpoint = "/api/v1/kuaishou/web/fetch_one_video_comment"
        data = await self.client.fetch_get_json(f"{endpoint}?photo_id={photo_id}&pcursor={pcursor}")
        return data

    # 获取主页视频数据 (Fetch Home Page Video Data)
    async def fetch_home_page_video(self, user_id: str, pcursor: str = None):
        endpoint = "/api/v1/kuaishou/web/fetch_home_page_video"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}&pcursor={pcursor}")
        return data

    # 获取主页信息数据 (Fetch Home Page Info Data)
    async def fetch_home_page_info(self, user_id: str):
        endpoint = "/api/v1/kuaishou/web/fetch_home_page_info"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}")
        return data