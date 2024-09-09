# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class XiaohongshuWeb:
    def __init__(self, client: APIClient):
        self.client = client

    # 获取笔记信息
    async def get_note_info(self, note_id: str):
        endpoint = "/api/v1/xiaohongshu/web/get_note_info"
        data = await self.client.fetch_get_json(f"{endpoint}?note_id={note_id}")
        return data

    # 获取笔记信息 V2
    async def get_note_info_v2(self, note_id: str):
        endpoint = "/api/v1/xiaohongshu/web/get_note_info_v2"
        data = await self.client.fetch_get_json(f"{endpoint}?note_id={note_id}")
        return data

    # 获取用户信息
    async def get_user_info(self, user_id: str):
        endpoint = "/api/v1/xiaohongshu/web/get_user_info"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}")
        return data

    # 搜索笔记
    async def search_notes(self, keyword: str, page: int = 1, sort: str = "general", noteType: str = "_0"):
        endpoint = "/api/v1/xiaohongshu/web/search_notes"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&page={page}&sort={sort}&noteType={noteType}")
        return data

    # 获取用户的笔记
    async def get_user_notes(self, user_id: str, lastCursor: str = None):
        endpoint = "/api/v1/xiaohongshu/web/get_user_notes"
        data = await self.client.fetch_get_json(f"{endpoint}?user_id={user_id}&lastCursor={lastCursor}")
        return data

    # 获取笔记评论
    async def get_note_comments(self, note_id: str, lastCursor: str = None):
        endpoint = "/api/v1/xiaohongshu/web/get_note_comments"
        data = await self.client.fetch_get_json(f"{endpoint}?note_id={note_id}&lastCursor={lastCursor}")
        return data

    # 获取笔记评论回复
    async def get_note_comment_replies(self, note_id: str, comment_id: str, lastCursor: str = None):
        endpoint = "/api/v1/xiaohongshu/web/get_note_comment_replies"
        data = await self.client.fetch_get_json(f"{endpoint}?note_id={note_id}&comment_id={comment_id}&lastCursor={lastCursor}")
        return data

    # 搜索用户
    async def search_users(self, keyword: str, page: int = 1):
        endpoint = "/api/v1/xiaohongshu/web/search_users"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&page={page}")
        return data
