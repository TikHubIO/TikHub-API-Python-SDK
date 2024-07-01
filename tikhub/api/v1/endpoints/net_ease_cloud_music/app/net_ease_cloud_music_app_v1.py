# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class NetEaseCloudMusicAppV1:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取单一歌曲信息V1（信息更全）| Fetch one music information V1 (more information)
    async def fetch_one_music_v1(self, music_id: str):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_one_music_v1"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}")
        return data

    # 获取单一歌曲信息V2（信息更少）| Fetch one music information V2 (less information)
    async def fetch_one_music_v2(self, music_id: str):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_one_music_v2"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}")
        return data

    # 获取单一歌曲歌词/Fetch one music lyric
    async def fetch_one_music_lyric(self, music_id: str):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_one_music_lyric"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}")
        return data

    # 获取单一歌曲播放地址V1（只能返回MP3格式，支持参数较少）/Fetch one music URL V1 (only MP3 format is supported, with fewer parameters)
    async def fetch_one_music_url_v1(self, music_id: str, br: str = "192000"):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_one_music_url_v1"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}&br={br}")
        return data

    # 获取单一歌曲播放地址V2（支持更多参数）/Fetch one music URL V2 (support more parameters)
    async def fetch_one_music_url_v2(self, music_id: str, level: str = "exhigh", encodeType: str = "mp3"):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_one_music_url_v2"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}&level={level}&encodeType={encodeType}")
        return data

    # Mlog（音乐视频）播放地址/Mlog (music video) playback address
    async def fetch_music_log_video_url(self, mlogId: str, resolution: str = "1080"):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_music_log_video_url"
        data = await self.client.fetch_get_json(f"{endpoint}?mlogId={mlogId}&resolution={resolution}")
        return data

    # 获取歌曲评论/Fetch music comment
    async def fetch_music_comment(self, resource_id: str, beforeTime: str = "0", limit: str = "30"):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_music_comment"
        data = await self.client.fetch_get_json(
            f"{endpoint}?resource_id={resource_id}&beforeTime={beforeTime}&limit={limit}")
        return data

    # 搜索接口V1/Search interface V1
    async def search_v1(self, keywords: str, offset: str = "0", limit: str = "20", _type: str = "1"):
        endpoint = "/api/v1/net_ease_cloud_music/app/search_v1"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keywords={keywords}&offset={offset}&limit={limit}&type={_type}")
        return data

    # 获取用户歌单/Get user playlist
    async def fetch_user_playlist(self, uid: str, offset: str = "0", limit: str = "20"):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_user_playlist"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}&offset={offset}&limit={limit}")
        return data

    # 获取用户信息/Get user information
    async def fetch_user_info(self, uid: str):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_user_info"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}")
        return data

    # 获取用户动态/Fetch user event
    async def fetch_user_event(self, uid: str, _time: str = "-1", limit: str = "10"):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_user_event"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}&time={_time}&limit={limit}")
        return data

    # 获取用户粉丝列表/Fetch user followers
    async def fetch_user_followers(self, uid: str, lasttime: str = "0", pagesize: str = "20"):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_user_followers"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}&lasttime={lasttime}&pagesize={pagesize}")
        return data

    # 获取用户关注列表/Fetch user follows
    async def fetch_user_follows(self, uid: str, offset: str = "0", limit: str = "20"):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_user_follows"
        data = await self.client.fetch_get_json(f"{endpoint}?uid={uid}&offset={offset}&limit={limit}")
        return data

    # 获取歌手信息/Fetch artist detail
    async def fetch_artist_detail(self, artist_id: str):
        endpoint = "/api/v1/net_ease_cloud_music/app/fetch_artist_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?artist_id={artist_id}")
        return data

    # 解密POST请求中的16进制payload/Decrypt the 16-bit payload in the POST request
    async def decrypt_post_payload(self, payload: str):
        endpoint = "/api/v1/net_ease_cloud_music/app/decrypt_post_payload"
        data = await self.client.fetch_post_json(endpoint, data=payload)
        return data

    # 加密POST请求中的payload并且返回16进制/Encrypt the payload in the POST request and return 16 hexadecimal
    async def encrypt_post_payload(self, uri: str, payload: dict, add_variable: bool = False):
        endpoint = "/api/v1/net_ease_cloud_music/app/encrypt_post_payload"
        endpoint = f"{endpoint}?uri={uri}&add_variable={add_variable}"
        data = await self.client.fetch_post_json(endpoint, data=json.dumps(payload))
        return data
