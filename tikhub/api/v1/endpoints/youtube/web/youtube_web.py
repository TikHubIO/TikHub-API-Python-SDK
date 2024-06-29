# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class YouTubeWeb:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取视频信息 | Get video information
    async def get_video_info(self, id: str):
        endpoint = "/api/v1/youtube/web/get_video_info"
        data = await self.client.fetch_get_json(f"{endpoint}?id={id}")
        return data

    # 获取视频字幕 | Get video subtitles
    async def get_video_subtitles(self, id: str, format: str = "json3"):
        endpoint = "/api/v1/youtube/web/get_video_subtitles"
        data = await self.client.fetch_get_json(f"{endpoint}?id={id}&format={format}")
        return data

    # 获取视频评论 | Get video comments
    async def get_video_comments(self, id: str, continuation: str = None, sort_by: str = None):
        endpoint = "/api/v1/youtube/web/get_video_comments"
        data = await self.client.fetch_get_json(f"{endpoint}?id={id}&continuation={continuation}&sort_by={sort_by}")
        return data

    # 获取短视频信息 | Get short video information
    async def get_short_video_info(self, id: str):
        endpoint = "/api/v1/youtube/web/get_short_video_info"
        data = await self.client.fetch_get_json(f"{endpoint}?id={id}")
        return data

