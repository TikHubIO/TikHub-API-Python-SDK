# Import API SDK Client class
from tikhub.http_client.api_client import APIClient


class BilibiliWeb:

    # Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # Fetch single video data | 获取单个视频详情信息
    async def fetch_one_video(self, bv_id: str):
        endpoint = "/api/v1/bilibili/web/fetch_one_video"
        data = await self.client.fetch_get_json(f"{endpoint}?bv_id={bv_id}")
        return data

    # Fetch video playurl | 获取视频流地址
    async def fetch_video_playurl(self, bv_id: str, cid: str):
        endpoint = "/api/v1/bilibili/web/fetch_video_playurl"
        data = await self.client.fetch_get_json(f"{endpoint}?bv_id={bv_id}&cid={cid}")
        return data

    # Fetch user post videos | 获取用户发布视频作品数据
    async def fetch_user_post_videos(self, uid: str, pn: int = 1):
        endpoint = "/api/v1/bilibili/web/fetch_user_post_videos"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}&pn={pn}")
        return data

    # Fetch collection folders | 获取用户所有收藏夹信息
    async def fetch_collect_folders(self, uid: str):
        endpoint = "/api/v1/bilibili/web/fetch_collect_folders"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}")
        return data

    # Fetch videos from collection folder | 获取指定收藏夹内视频数据
    async def fetch_user_collection_videos(self, folder_id: str, pn: int = 1):
        endpoint = "/api/v1/bilibili/web/fetch_user_collection_videos"
        data = await self.client.fetch_get_json(f"{endpoint}?folder_id={folder_id}&pn={pn}")
        return data

    # Fetch user profile | 获取指定用户的信息
    async def fetch_user_profile(self, uid: str):
        endpoint = "/api/v1/bilibili/web/fetch_user_profile"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}")
        return data

    # Fetch comprehensive popular videos | 获取综合热门视频信息
    async def fetch_com_popular(self, pn: int = 1):
        endpoint = "/api/v1/bilibili/web/fetch_com_popular"
        data = await self.client.fetch_get_json(f"{endpoint}?pn={pn}")
        return data

    # Fetch video comments | 获取指定视频的评论
    async def fetch_video_comments(self, bv_id: str, pn: int = 1):
        endpoint = "/api/v1/bilibili/web/fetch_video_comments"
        data = await self.client.fetch_get_json(f"{endpoint}?bv_id={bv_id}&pn={pn}")
        return data

    # Fetch comment reply | 获取视频下指定评论的回复
    async def fetch_comment_reply(self, bv_id: str, rpid: str, pn: int = 1):
        endpoint = "/api/v1/bilibili/web/fetch_comment_reply"
        data = await self.client.fetch_get_json(f"{endpoint}?bv_id={bv_id}&pn={pn}&rpid={rpid}")
        return data

    # Fetch user dynamics | 获取指定用户动态
    async def fetch_user_dynamic(self, uid: str, offset: str = ""):
        endpoint = "/api/v1/bilibili/web/fetch_user_dynamic"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}&offset={offset}")
        return data

    # Fetch video danmaku | 获取视频实时弹幕
    async def fetch_video_danmaku(self, cid: str):
        endpoint = "/api/v1/bilibili/web/fetch_video_danmaku"
        data = await self.client.fetch_get_json(f"{endpoint}?cid={cid}")
        return data

    # Fetch live room details | 获取指定直播间信息
    async def fetch_live_room_detail(self, room_id: str):
        endpoint = "/api/v1/bilibili/web/fetch_live_room_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}")
        return data

    # Fetch live room videos | 获取指定直播间视频流
    async def fetch_live_videos(self, room_id: str):
        endpoint = "/api/v1/bilibili/web/fetch_live_videos"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}")
        return data

    # Fetch live streamers in area | 获取指定分区正在直播的主播
    async def fetch_live_streamers(self, area_id: str, pn: int = 1):
        endpoint = "/api/v1/bilibili/web/fetch_live_streamers"
        data = await self.client.fetch_get_json(f"{endpoint}?area_id={area_id}&pn={pn}")
        return data

    # Fetch all live areas | 获取所有直播分区列表
    async def fetch_all_live_areas(self):
        endpoint = "/api/v1/bilibili/web/fetch_all_live_areas"
        data = await self.client.fetch_get_json(endpoint)
        return data

    # Convert bv_id to aid | 通过bv号获得视频aid号
    async def bv_to_aid(self, bv_id: str):
        endpoint = "/api/v1/bilibili/web/bv_to_aid"
        data = await self.client.fetch_get_json(f"{endpoint}?bv_id={bv_id}")
        return data

    # Fetch video parts by bv_id | 通过bv号获得视频分p信息
    async def fetch_video_parts(self, bv_id: str):
        endpoint = "/api/v1/bilibili/web/fetch_video_parts"
        data = await self.client.fetch_get_json(f"{endpoint}?bv_id={bv_id}")
        return data
