# 导入API SDK Client类
import json

import websockets

from tikhub.http_client.api_client import APIClient


class TikTokWeb:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取单个作品数据 | Get single video data
    async def fetch_post_detail(self, item_id: str):
        endpoint = "/api/v1/tiktok/web/fetch_post_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?itemId={item_id}")
        return data

    # 获取用户的个人信息 | Get user profile
    async def fetch_user_profile(self, secUid: str, uniqueId: str = None):
        endpoint = "/api/v1/tiktok/web/fetch_user_profile"
        data = await self.client.fetch_get_json(f"{endpoint}?secUid={secUid}&uniqueId={uniqueId}")
        return data

    # 获取用户的作品列表 | Get user posts
    async def fetch_user_post(self, secUid: str, cursor: int, count: int, coverFormat: int):
        endpoint = "/api/v1/tiktok/web/fetch_user_post"
        data = await self.client.fetch_get_json(f"{endpoint}?secUid={secUid}&cursor={cursor}&count={count}&coverFormat={coverFormat}")
        return data

    # 获取用户的点赞列表 | Get user likes
    async def fetch_user_like(self, secUid: str, cursor: int, count: int, coverFormat: int):
        endpoint = "/api/v1/tiktok/web/fetch_user_like"
        data = await self.client.fetch_get_json(f"{endpoint}?secUid={secUid}&cursor={cursor}&count={count}&coverFormat={coverFormat}")
        return data

    # 获取用户的收藏列表 | Get user favorites
    async def fetch_user_collect(self, cookie: str, secUid: str, cursor: int, count: int, coverFormat: int):
        endpoint = "/api/v1/tiktok/web/fetch_user_collect"
        data = await self.client.fetch_get_json(f"{endpoint}?cookie={cookie}&secUid={secUid}&cursor={cursor}&count={count}&coverFormat={coverFormat}")
        return data

    # 获取用户的播放列表 | Get user play list
    async def fetch_user_play_list(self, secUid: str, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/web/fetch_user_play_list"
        data = await self.client.fetch_get_json(f"{endpoint}?secUid={secUid}&cursor={cursor}&count={count}")
        return data

    # 获取用户的合辑列表 | Get user mix list
    async def fetch_user_mix(self, mixId: str, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/web/fetch_user_mix"
        data = await self.client.fetch_get_json(f"{endpoint}?mixId={mixId}&cursor={cursor}&count={count}")
        return data

    # 获取作品的评论列表 | Get video comments
    async def fetch_post_comment(self, aweme_id: str, cursor: int, count: int, current_region: str):
        endpoint = "/api/v1/tiktok/web/fetch_post_comment"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}&cursor={cursor}&count={count}&current_region={current_region}")
        return data

    # 获取作品的评论回复列表 | Get video comment replies
    async def fetch_post_comment_reply(self, item_id: str, comment_id: str, cursor: int, count: int, current_region: str):
        endpoint = "/api/v1/tiktok/web/fetch_post_comment_reply"
        data = await self.client.fetch_get_json(f"{endpoint}?item_id={item_id}&comment_id={comment_id}&cursor={cursor}&count={count}&current_region={current_region}")
        return data

    # 获取用户的粉丝列表 | Get user followers
    async def fetch_user_fans(self, secUid: str, count: int, maxCursor: int, minCursor: int):
        endpoint = "/api/v1/tiktok/web/fetch_user_fans"
        data = await self.client.fetch_get_json(f"{endpoint}?secUid={secUid}&count={count}&maxCursor={maxCursor}&minCursor={minCursor}")
        return data

    # 获取用户的关注列表 | Get user followings
    async def fetch_user_follow(self, secUid: str, count: int, maxCursor: int, minCursor: int):
        endpoint = "/api/v1/tiktok/web/fetch_user_follow"
        data = await self.client.fetch_get_json(f"{endpoint}?secUid={secUid}&count={count}&maxCursor={maxCursor}&minCursor={minCursor}")
        return data

    # 获取综合搜索列表 | Get general search list
    async def fetch_general_search(self, keyword: str, count: int, offset: int, search_id: str = None, cookie: str = None):
        endpoint = "/api/v1/tiktok/web/fetch_general_search"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&count={count}&offset={offset}&search_id={search_id}&cookie={cookie}")
        return data

    # 搜索关键字推荐 | Search keyword suggest
    async def fetch_search_keyword_suggest(self, keyword: str):
        endpoint = "/api/v1/tiktok/web/fetch_search_keyword_suggest"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}")
        return data

    # 搜索用户 | Search user
    async def fetch_search_user(self, keyword: str, cursor: int, search_id: str = None, cookie: str = None):
        endpoint = "/api/v1/tiktok/web/fetch_search_user"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&cursor={cursor}&search_id={search_id}&cookie={cookie}")
        return data

    # 搜索视频 | Search video
    async def fetch_search_video(self, keyword: str, count: int, offset: int, search_id: str = None, cookie: str = None):
        endpoint = "/api/v1/tiktok/web/fetch_search_video"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&count={count}&offset={offset}&search_id={search_id}&cookie={cookie}")
        return data

    # 搜索直播 | Search live
    async def fetch_search_live(self, keyword: str, count: int, offset: int, search_id: str = None, cookie: str = None):
        endpoint = "/api/v1/tiktok/web/fetch_search_live"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&count={count}&offset={offset}&search_id={search_id}&cookie={cookie}")
        return data

    # Tag详情 | Tag detail
    async def fetch_tag_detail(self, tag_name: str):
        endpoint = "/api/v1/tiktok/web/fetch_tag_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?tag_name={tag_name}")
        return data

    # Tag作品列表 | Tag post list
    async def fetch_tag_post(self, challengeID: str, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/web/fetch_tag_post"
        data = await self.client.fetch_get_json(f"{endpoint}?challengeID={challengeID}&cursor={cursor}&count={count}")
        return data

    # 生成真实msToken | Generate real msToken
    async def fetch_real_msToken(self):
        endpoint = "/api/v1/tiktok/web/generate_real_msToken"
        data = await self.client.fetch_get_json(endpoint)
        return data

    # 生成ttwid | Generate ttwid
    async def fetch_ttwid(self, cookie: str):
        endpoint = "/api/v1/tiktok/web/generate_ttwid"
        data = await self.client.fetch_get_json(f"{endpoint}?cookie={cookie}")
        return data

    # 生成xbogus | Generate xbogus
    async def gen_xbogus(self, url: str, user_agent: str):
        endpoint = "/api/v1/tiktok/web/generate_xbogus"
        data = await self.client.fetch_post_json(endpoint, data={"url": url, "user_agent": user_agent})
        return data

    # 提取用户sec_user_id | Extract user sec_user_id
    async def get_sec_user_id(self, url: str):
        endpoint = "/api/v1/tiktok/web/get_sec_user_id"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 提取列表用户sec_user_id | Extract list user sec_user_id
    async def get_all_sec_user_id(self, url: list):
        endpoint = "/api/v1/tiktok/web/get_all_sec_user_id"
        data = await self.client.fetch_post_json(endpoint, data={"url": url})
        return data

    # 提取单个作品id | Extract single video id
    async def get_aweme_id(self, url: str):
        endpoint = "/api/v1/tiktok/web/get_aweme_id"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 提取列表作品id | Extract list video id
    async def get_all_aweme_id(self, url: list):
        endpoint = "/api/v1/tiktok/web/get_all_aweme_id"
        data = await self.client.fetch_post_json(endpoint, data={"url": url})
        return data

    # 获取用户unique_id | Get user unique_id
    async def get_unique_id(self, url: str):
        endpoint = "/api/v1/tiktok/web/get_unique_id"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 提取列表unique_id列表 | Get list unique_id
    async def get_all_unique_id(self, url: list):
        endpoint = "/api/v1/tiktok/web/get_all_unique_id"
        data = await self.client.fetch_post_json(endpoint, data={"url": url})
        return data

    # 根据直播间链接提取直播间ID | Extract live room ID based on live room link
    async def get_live_room_id(self, live_room_url: str):
        endpoint = "/api/v1/tiktok/web/get_live_room_id"
        data = await self.client.fetch_get_json(f"{endpoint}?live_room_url={live_room_url}")
        return data

    # 提取直播间弹幕 - HTTP | Extract live room barrage - HTTP
    async def tiktok_live_room(self, live_room_url: str, danmaku_type: str):
        endpoint = "/api/v1/tiktok/web/tiktok_live_room"
        data = await self.client.fetch_get_json(f"{endpoint}?live_room_url={live_room_url}&danmaku_type={danmaku_type}")
        return data

    # 提取直播间弹幕 - WebSocket | Extract live room barrage - WebSocket
    async def tiktok_live_room_ws(self, live_room_url: str, danmaku_type: str):
        """
        提取直播间弹幕 - WebSocket | Extract webcast danmaku - WebSocket
        :param live_room_url: 直播间链接 | Room link
        :param danmaku_type: 弹幕类型 | Danmaku type
        :return: 弹幕数据 | Danmaku data
        """
        endpoint = await self.tiktok_live_room(live_room_url, danmaku_type)
        # $.data.ws_url
        wss_url = endpoint["data"]["ws_url"]
        # 连接 WebSocket
        try:
            async with websockets.connect(wss_url, ping_interval=10, ping_timeout=5) as websocket:
                # 持续接收消息
                while True:
                    response = await websocket.recv()
                    print(f"Received from server: {response}")

                    # 你可以在这里处理接收到的消息 | You can process the received message here

        except Exception as e:
            print(f"Failed to connect: {e}")

    # 直播间开播状态检测 | Live room broadcast status detection
    async def fetch_check_live_alive(self, room_id: str):
        endpoint = "/api/v1/tiktok/web/fetch_check_live_alive"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}")
        return data

    # 通过直播链接获取直播间信息（离线直播间也可以获取） | Get live room information through live link (offline live room can also be obtained)
    async def fetch_tiktok_live_data(self, live_room_url: str):
        endpoint = "/api/v1/tiktok/web/fetch_tiktok_live_data"
        data = await self.client.fetch_get_json(f"{endpoint}?live_room_url={live_room_url}")
        return data

    # 获取直播间首页推荐列表 | Get live room home page recommendation list
    async def fetch_live_recommend(self, related_live_tag: str):
        endpoint = "/api/v1/tiktok/web/fetch_live_recommend"
        data = await self.client.fetch_get_json(f"{endpoint}?related_live_tag={related_live_tag}")
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        tiktok_web = TikTokWeb(client)

        # 获取单个作品数据 | Get single video data
        item_id = "6952419395722484486"
        data = await tiktok_web.fetch_post_detail(item_id)
        print(data)

        # 获取用户的个人信息 | Get user profile
        secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        uniqueId = None
        data = await tiktok_web.fetch_user_profile(secUid, uniqueId)
        print(data)

        # 获取用户的作品列表 | Get user posts
        secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        cursor = 0
        count = 30
        coverFormat = 1
        data = await tiktok_web.fetch_user_post(secUid, cursor, count, coverFormat)
        print(data)

        # 获取用户的点赞列表 | Get user likes
        secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        cursor = 0
        count = 30
        coverFormat = 1
        data = await tiktok_web.fetch_user_like(secUid, cursor, count, coverFormat)
        print(data)

        # 获取用户的收藏列表 | Get user favorites
        cookie = ""
        secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        cursor = 0
        count = 30
        coverFormat = 1
        data = await tiktok_web.fetch_user_collect(cookie, secUid, cursor, count, coverFormat)
        print(data)

        # 获取用户的播放列表 | Get user play list
        secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        cursor = 0
        count = 30
        data = await tiktok_web.fetch_user_play_list(secUid, cursor, count)

        # 获取用户的合辑列表 | Get user mix list
        mixId = "6952419395722484486"
        cursor = 0
        count = 30
        data = await tiktok_web.fetch_user_mix(mixId, cursor, count)
        print(data)

        # 获取作品的评论列表 | Get video comments
        aweme_id = "6952419395722484486"
        cursor = 0
        count = 30
        current_region = "CN"
        data = await tiktok_web.fetch_post_comment(aweme_id, cursor, count, current_region)
        print(data)

        # 获取作品的评论回复列表 | Get video comment replies
        item_id = "6952419395722484486"
        comment_id = "6952419395722484486"
        cursor = 0
        count = 30
        current_region = "CN"
        data = await tiktok_web.fetch_post_comment_reply(item_id, comment_id, cursor, count, current_region)
        print(data)

        # 获取用户的粉丝列表 | Get user followers
        secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        count = 30
        maxCursor = 0
        minCursor = 0
        data = await tiktok_web.fetch_user_fans(secUid, count, maxCursor, minCursor)
        print(data)

        # 获取用户的关注列表 | Get user followings
        secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        count = 30
        maxCursor = 0
        minCursor = 0
        data = await tiktok_web.fetch_user_follow(secUid, count, maxCursor, minCursor)
        print(data)

        # 获取综合搜索列表 | Get general search list
        keyword = "tiktok"
        count = 30
        offset = 0
        data = await tiktok_web.fetch_general_search(keyword, count, offset)
        print(data)

        # 搜索关键字推荐 | Search keyword suggest
        keyword = "tiktok"
        data = await tiktok_web.fetch_search_keyword_suggest(keyword)
        print(data)

        # 搜索用户 | Search user
        keyword = "tiktok"
        cursor = 0
        data = await tiktok_web.fetch_search_user(keyword, cursor)
        print(data)

        # 搜索视频 | Search video
        keyword = "tiktok"
        count = 30
        offset = 0
        data = await tiktok_web.fetch_search_video(keyword, count, offset)
        print(data)

        # 搜索直播 | Search live
        keyword = "tiktok"
        count = 30
        offset = 0
        data = await tiktok_web.fetch_search_live(keyword, count, offset)
        print(data)

        # 生成真实msToken | Generate real msToken
        data = await tiktok_web.fetch_real_msToken()
        print(data)

        # 生成ttwid | Generate ttwid
        cookie = ""
        data = await tiktok_web.fetch_ttwid(cookie)
        print(data)

        # 生成xbogus | Generate xbogus
        url = ""
        user_agent = ""
        data = await tiktok_web.gen_xbogus(url, user_agent)
        print(data)

        # 提取用户sec_user_id | Extract user sec_user_id
        url = ""
        data = await tiktok_web.get_sec_user_id(url)
        print(data)

        # 提取列表用户sec_user_id | Extract list user sec_user_id
        url = []
        data = await tiktok_web.get_all_sec_user_id(url)
        print(data)

        # 提取单个作品id | Extract single video id
        url = ""
        data = await tiktok_web.get_aweme_id(url)
        print(data)

        # 提取列表作品id | Extract list video id
        url = []
        data = await tiktok_web.get_all_aweme_id(url)
        print(data)

        # 获取用户unique_id | Get user unique_id
        url = ""
        data = await tiktok_web.get_unique_id(url)
        print(data)

        # 提取列表unique_id列表 | Get list unique_id
        url = []
        data = await tiktok_web.get_all_unique_id(url)
        print(data)





