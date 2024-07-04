# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class HybridParsing:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 抖音TikTok的混合解析 | Hybrid parsing of Douyin and TikTok
    async def video_data(self, url: str, minimal: bool = False, base64_url: bool = False):
        endpoint = "/api/v1/hybrid/video_data"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}&minimal={minimal}&base64_url={base64_url}")
        return data
