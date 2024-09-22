# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class TikTokAppV2:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取单个作品数据 | Get single video data
    async def fetch_one_video(self, aweme_id: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_one_video"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}")
        return data

    # 根据分享链接获取作品数据 | Get video data by sharing url
    async def fetch_one_video_by_share_url(self, share_url: str):
        endpoint = "/api/v1/tiktok/app/v2/fetch_one_video_by_share_url"
        data = await self.client.fetch_get_json(f"{endpoint}?share_url={share_url}")
        return data

    # 获取指定用户的信息 | Get information of specified user
    async def handler_user_profile(self, sec_user_id: str):
        endpoint = "/api/v1/tiktok/app/v2/handler_user_profile"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}")
        return data

    # 获取用户主页作品数据 | Get user homepage video data
    async def fetch_user_post_videos(self, sec_user_id: str, max_cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_user_post_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&count={count}")
        return data

    # 获取用户喜欢作品数据 | Get user like video data
    async def fetch_user_like_videos(self, sec_user_id: str, max_cursor: int, counts: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_user_like_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&counts={counts}")
        return data

    # 获取单个视频评论数据 | Get single video comments data
    async def fetch_video_comments(self, aweme_id: str, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_video_comments"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定视频的评论回复数据 | Get comment replies data of specified video
    async def fetch_video_comments_reply(self, item_id: str, comment_id: str, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_video_comment_replies"
        data = await self.client.fetch_get_json(
            f"{endpoint}?item_id={item_id}&comment_id={comment_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
    async def fetch_general_search_result(self, keyword: str, offset: int, count: int, sort_type: int,
                                          publish_time: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_general_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}")
        return data

    # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
    async def fetch_video_search_result(self, keyword: str, offset: int, count: int, sort_type: int, publish_time: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_video_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}")
        return data

    # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
    async def fetch_user_search_result(self, keyword: str, offset: int, count: int, user_search_follower_count: str,
                                       user_search_profile_type: str, user_search_other_pref: str):
        endpoint = "/api/v1/tiktok/app/v2/fetch_user_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&user_search_follower_count={user_search_follower_count}&user_search_profile_type={user_search_profile_type}&user_search_other_pref={user_search_other_pref}")
        return data

    # 获取指定关键词的音乐搜索结果 | Get music search results of specified keywords
    async def fetch_music_search_result(self, keyword: str, offset: int, count: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_music_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定关键词的话题搜索结果 | Get hashtag search results of specified keywords
    async def fetch_hashtag_search_result(self, keyword: str, offset: int, count: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_hashtag_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定关键词的直播搜索结果 | Get live search results of specified keywords
    async def fetch_live_search_result(self, keyword: str, offset: int, count: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_live_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定音乐的详情数据 | Get details of specified music
    async def fetch_music_detail(self, music_id: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_music_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}")
        return data

    # 抖音音乐视频列表结果 | Get video list of specified music
    async def fetch_music_video_list(self, music_id: int, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_music_video_list"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}&cursor={cursor}&count={count}")
        return data

    # 抖音话题详情数据 | Get details of specified hashtag
    async def fetch_hashtag_detail(self, ch_id: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_hashtag_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?ch_id={ch_id}")
        return data

    # 获取指定话题的作品数据 | Get video list of specified hashtag
    async def fetch_hashtag_post_list(self, ch_id: int, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v2/fetch_hashtag_video_list"
        data = await self.client.fetch_get_json(f"{endpoint}?ch_id={ch_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定用户的粉丝列表数据 | Get follower list of specified user
    async def fetch_user_follower_list(self, sec_user_id: str, count: int = 20, min_time: int = 0, page_token: str = ""):
        endpoint = "/api/v1/tiktok/app/v2/fetch_user_follower_list"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&count={count}&min_time={min_time}&page_token={page_token}")
        return data

    # 获取指定用户的关注列表数据 | Get following list of specified user
    async def fetch_user_following_list(self, sec_user_id: str, count: int = 20, min_time: int = 0, page_token: str = ""):
        endpoint = "/api/v1/tiktok/app/v2/fetch_user_following_list"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&count={count}&min_time={min_time}&page_token={page_token}")
        return data

    # 获取直播间排行榜数据 | Get live room ranking list
    async def fetch_live_ranking_list(self, room_id: str, anchor_id: str):
        endpoint = "/api/v1/tiktok/app/v2/fetch_live_ranking_list"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}&anchor_id={anchor_id}")
        return data

    # 检测直播间是否在线 | Check if live room is online
    async def check_live_room_online(self, room_id: str):
        endpoint = "/api/v1/tiktok/app/v2/check_live_room_online"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}")
        return data

    # 视频主页Feed (Home Feed) | Get video home feed
    async def fetch_home_feed(self):
        endpoint = "/api/v1/tiktok/app/v2/fetch_home_feed"
        data = await self.client.fetch_get_json(endpoint)
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        tiktok_app_v2 = TikTokAppV2(client)

        # 获取单个作品数据 | Get single video data
        data = await tiktok_app_v2.fetch_one_video(aweme_id=6953882931123590914)
        print(data)

        # 获取指定用户的信息 | Get information of specified user
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        data = await tiktok_app_v2.handler_user_profile(sec_user_id)
        print(data)

        # 获取用户主页作品数据 | Get user homepage video data
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        data = await tiktok_app_v2.fetch_user_post_videos(sec_user_id, max_cursor=0, count=10)
        print(data)

        # 获取用户喜欢作品数据 | Get user like video data
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        data = await tiktok_app_v2.fetch_user_like_videos(sec_user_id, max_cursor=0, counts=10)
        print(data)

        # 获取单个视频评论数据 | Get single video comments data
        aweme_id = "6953882931123590914"
        data = await tiktok_app_v2.fetch_video_comments(aweme_id, cursor=0, count=10)
        print(data)

        # 获取指定视频的评论回复数据 | Get comment replies data of specified video
        item_id = "6953882931123590914"
        comment_id = "6953882931123590914"
        data = await tiktok_app_v2.fetch_video_comments_reply(item_id, comment_id, cursor=0, count=10)
        print(data)

        # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
        keyword = "抖音"
        offset = 0
        count = 10
        sort_type = 0
        publish_time = 0
        data = await tiktok_app_v2.fetch_general_search_result(keyword, offset, count, sort_type, publish_time)
        print(data)

        # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
        keyword = "抖音"
        offset = 0
        count = 10
        sort_type = 0
        publish_time = 0
        data = await tiktok_app_v2.fetch_video_search_result(keyword, offset, count, sort_type, publish_time)
        print(data)

        # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
        keyword = "抖音"
        offset = 0
        count = 10
        user_search_follower_count = "0"
        user_search_profile_type = "0"
        user_search_other_pref = "0"
        data = await tiktok_app_v2.fetch_user_search_result(keyword, offset, count, user_search_follower_count, user_search_profile_type, user_search_other_pref)
        print(data)

        # 获取指定关键词的音乐搜索结果 | Get music search results of specified keywords
        keyword = "抖音"
        offset = 0
        count = 10
        data = await tiktok_app_v2.fetch_music_search_result(keyword, offset, count)
        print(data)

        # 获取指定关键词的话题搜索结果 | Get hashtag search results of specified keywords
        keyword = "抖音"
        offset = 0
        count = 10
        data = await tiktok_app_v2.fetch_hashtag_search_result(keyword, offset, count)
        print(data)

        # 获取指定关键词的直播搜索结果 | Get live search results of specified keywords
        keyword = "抖音"
        offset = 0
        count = 10
        data = await tiktok_app_v2.fetch_live_search_result(keyword, offset, count)
        print(data)

        # 获取指定音乐的详情数据 | Get details of specified music
        music_id = 6953882931123590914
        data = await tiktok_app_v2.fetch_music_detail(music_id)
        print(data)

        # 抖音音乐视频列表结果 | Get video list of specified music
        music_id = 6953882931123590914
        cursor = 0
        count = 10
        data = await tiktok_app_v2.fetch_music_video_list(music_id, cursor, count)
        print(data)

        # 抖音话题详情数据 | Get details of specified hashtag
        ch_id = 6953882931123590914
        data = await tiktok_app_v2.fetch_hashtag_detail(ch_id)
        print(data)

        # 获取指定话题的作品数据 | Get video list of specified hashtag
        ch_id = 6953882931123590914
        cursor = 0
        count = 10
        data = await tiktok_app_v2.fetch_hashtag_post_list(ch_id, cursor, count)
        print(data)

        # 获取指定用户的粉丝列表数据 | Get follower list of specified user
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        count = 10
        max_time = 0
        data = await tiktok_app_v2.fetch_user_follower_list(sec_user_id, count, max_time)
        print(data)

        # 获取指定用户的关注列表数据 | Get following list of specified user
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        count = 10
        max_time = 0
        data = await tiktok_app_v2.fetch_user_following_list(sec_user_id, count, max_time)
        print(data)

        # 获取直播间排行榜数据 | Get live room ranking list
        room_id = "6953882931123590914"
        anchor_id = "6953882931123590914"
        data = await tiktok_app_v2.fetch_live_ranking_list(room_id, anchor_id)
        print(data)

        # 检测直播间是否在线 | Check if live room is online
        room_id = "6953882931123590914"
        data = await tiktok_app_v2.check_live_room_online(room_id)
        print(data)




