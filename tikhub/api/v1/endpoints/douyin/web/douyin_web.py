# 导入API SDK Client类
import json

from tikhub.client.api_client import APIClient


class DouyinWeb:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取单个作品数据 | Get single video data
    async def fetch_one_video(self, aweme_id: str):
        """
        获取单个作品数据 | Get single video data
        :param aweme_id: 作品id | Video id
        :return: 作品数据 | Video data
        """
        endpoint = "/api/v1/douyin/web/fetch_one_video"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}")
        return data

    # 获取单个作品视频弹幕数据 | Get single video danmaku data
    async def fetch_one_video_danmaku(self, item_id: str, duration: int, end_time: int, start_time: int):
        """
        获取单个作品视频弹幕数据 | Get single video danmaku data
        :param item_id: 作品id | Video id
        :param duration: 视频总时长 | Video total duration
        :param end_time: 结束时间 | End time
        :param start_time: 开始时间 | Start time
        :return: 视频弹幕数据 | Video danmaku data
        """
        endpoint = "/api/v1/douyin/web/fetch_one_video_danmaku"
        data = await self.client.fetch_get_json(
            f"{endpoint}?item_id={item_id}&duration={duration}&end_time={end_time}&start_time={start_time}")
        return data

    # 获取用户主页作品数据 | Get user homepage video data
    async def fetch_user_post_videos(self, sec_user_id: str, max_cursor: int, count: int):
        """
        获取用户主页作品数据 | Get user homepage video data
        :param sec_user_id: 用户sec_user_id | User sec_user_id
        :param max_cursor: 最大游标 | Maximum cursor
        :param count: 最大数量 | Maximum count number
        :return: 用户作品数据 | User video data
        """
        endpoint = "/api/v1/douyin/web/fetch_user_post_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&count={count}")
        return data

    # 获取用户喜欢作品数据 | Get user like video data
    async def fetch_user_like_videos(self, sec_user_id: str, max_cursor: int, counts: int):
        """
        获取用户喜欢作品数据 | Get user like video data
        :param sec_user_id: 用户sec_user_id | User sec_user_id
        :param max_cursor: 最大游标 | Maximum cursor
        :param counts: 最大数量 | Maximum count number
        :return: 用户作品数据 | User video data
        """
        endpoint = "/api/v1/douyin/web/fetch_user_like_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&counts={counts}")
        return data

    # 获取用户收藏作品数据 | Get user collection video data
    async def fetch_user_collection_videos(self, cookie: str, max_cursor: int, counts: int):
        """
        获取用户收藏作品数据 | Get user collection video data
        :param cookie: 用户网页版抖音Cookie | Your web version of Douyin Cookie
        :param max_cursor: 最大游标 | Maximum cursor
        :param counts: 最大数量 | Maximum count number
        :return: 用户作品数据 | User video data
        """
        endpoint = "/api/v1/douyin/web/fetch_user_collection_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?cookie={cookie}&max_cursor={max_cursor}&counts={counts}")
        return data

    # 获取用户合辑作品数据 | Get user mix video data
    async def fetch_user_mix_videos(self, mix_id: str, max_cursor: int, counts: int):
        """
        获取用户合辑作品数据 | Get user mix video data
        :param mix_id: 合辑id | Mix id
        :param max_cursor: 最大游标 | Maximum cursor
        :param counts: 最大数量 | Maximum count number
        :return: 用户作品数据 | User video data
        """
        endpoint = "/api/v1/douyin/web/fetch_user_mix_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?mix_id={mix_id}&max_cursor={max_cursor}&counts={counts}")
        return data

    # 获取用户直播流数据 | Get user live video data
    async def fetch_user_live_videos(self, webcast_id: str):
        """
        获取用户直播流数据 | Get user live video data
        :param webcast_id: 直播间webcast_id | Room webcast_id
        :return: 直播流数据 | Live stream data
        """
        endpoint = "/api/v1/douyin/web/fetch_user_live_videos"
        data = await self.client.fetch_get_json(f"{endpoint}?webcast_id={webcast_id}")
        return data

    # 获取指定用户的直播流数据 | Get live video data of specified user
    async def fetch_user_live_videos_by_room_id(self, room_id: str):
        """
        获取指定用户的直播流数据 | Get live video data of specified user
        :param room_id: 直播间room_id | Room room_id
        :return: 直播流数据 | Live stream data
        """
        endpoint = "/api/v1/douyin/web/fetch_user_live_videos_by_room_id"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}")
        return data

    # 获取直播间送礼用户排行榜 | Get live room gift user ranking
    async def fetch_live_gift_ranking(self, room_id: str, rank_type: int):
        """
        获取直播间送礼用户排行榜 | Get live room gift user ranking
        :param room_id: 直播间room_id | Room room_id
        :param rank_type: 排行类型 | Leaderboard type
        :return: 排行榜数据 | Leaderboard data
        """
        endpoint = "/api/v1/douyin/web/fetch_live_gift_ranking"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}&rank_type={rank_type}")
        return data

    # 抖音直播间商品信息 | Douyin live room product information
    async def fetch_live_room_product_result(self, room_id: str, author_id: str, limit: int):
        """
        抖音直播间商品信息 | Douyin live room product information
        :param room_id: 直播间room_id | Room room_id
        :param author_id: 作者id | Author id
        :param limit: 数量 | Number
        :return: 商品信息 | Product information
        """
        endpoint = "/api/v1/douyin/web/fetch_live_room_product_result"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}&author_id={author_id}&limit={limit}")
        return data

    # 获取指定用户的信息 | Get information of specified user
    async def handler_user_profile(self, sec_user_id: str):
        """
        获取指定用户的信息 | Get information of specified user
        :param sec_user_id: 用户sec_user_id | User sec_user_id
        :return: 用户信息 | User information
        """
        endpoint = "/api/v1/douyin/web/handler_user_profile"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}")
        return data

    # 获取单个视频评论数据 | Get single video comments data
    async def fetch_video_comments(self, aweme_id: str, cursor: int, count: int):
        """
        获取单个视频评论数据 | Get single video comments data
        :param aweme_id: 作品id | Video id
        :param cursor: 游标 | Cursor
        :param count: 数量 | Number
        :return: 评论数据 | Comments data
        """
        endpoint = "/api/v1/douyin/web/fetch_video_comments"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定视频的评论回复数据 | Get comment replies data of specified video
    async def fetch_video_comments_reply(self, item_id: str, comment_id: str, cursor: int, count: int):
        """
        获取指定视频的评论回复数据 | Get comment replies data of specified video
        :param item_id: 作品id | Video id
        :param comment_id: 评论id | Comment id
        :param cursor: 游标 | Cursor
        :param count: 数量 | Number
        :return: 评论回复数据 | Comment replies data
        """
        endpoint = "/api/v1/douyin/web/fetch_video_comment_replies"
        data = await self.client.fetch_get_json(
            f"{endpoint}?item_id={item_id}&comment_id={comment_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
    async def fetch_general_search_result(self, keyword: str, offset: int, count: int, sort_type: str,
                                          publish_time: str, filter_duration: str):
        """
        获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
        :param keyword: 关键词 | Keyword
        :param offset: 偏移量 | Offset
        :param count: 数量 | Number
        :param sort_type: 0:综合排序 1:最多点赞 2:最新发布 | 0: Comprehensive sorting 1: Most likes 2: Latest release
        :param publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 | 0: Unlimited 1: Last day 7: Last week 180: Last half year
        :param filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 | 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes
        :return: 综合搜索结果 | Comprehensive search results
        """
        endpoint = "/api/v1/douyin/web/fetch_general_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}")
        return data

    # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
    async def fetch_video_search_result(self, keyword: str, offset: int, count: int, sort_type: str, publish_time: str,
                                        filter_duration: str):
        """
        获取指定关键词的视频搜索结果 | Get video search results of specified keywords
        :param keyword: 关键词 | Keyword
        :param offset: 偏移量 | Offset
        :param count: 数量 | Number
        :param sort_type: 0:综合排序 1:最多点赞 2:最新发布 | 0: Comprehensive sorting 1: Most likes 2: Latest release
        :param publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年 | 0: Unlimited 1: Last day 7: Last week 180: Last half year
        :param filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上 | 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes
        :return: 视频搜索结果 | Video search results
        """
        endpoint = "/api/v1/douyin/web/fetch_video_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}")
        return data

    # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
    async def fetch_user_search_result(self, keyword: str, offset: int, count: int, douyin_user_fans: str,
                                       douyin_user_type: str):
        """
        获取指定关键词的用户搜索结果 | Get user search results of specified keywords
        :param keyword: 关键词 | Keyword
        :param offset: 偏移量 | Offset
        :param count: 数量 | Number
        :param douyin_user_fans: 留空:不限, "0_1k": 1000以下, "1k_1w": 1000-1万, "1w_10w": 1w-10w, "10w_100w": 10w-100w，"100w_": 100w以上
        :param douyin_user_type: 留空:不限, "common_user": 普通用户, "enterprise_user": 企业认证, "personal_user": 个人认证
        :return: 用户搜索结果 | User search results
        """
        endpoint = "/api/v1/douyin/web/fetch_user_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&douyin_user_fans={douyin_user_fans}&douyin_user_type={douyin_user_type}")
        return data

    # 获取指定关键词的直播搜索结果 | Get live search results of specified keywords
    async def fetch_live_search_result(self, keyword: str, offset: int, count: int):
        """
        获取指定关键词的直播搜索结果 | Get live search results of specified keywords
        :param keyword: 关键词 | Keyword
        :param offset: 偏移量 | Offset
        :param count: 数量 | Number
        :return: 直播搜索结果 | Live search results
        """
        endpoint = "/api/v1/douyin/web/fetch_live_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取抖音热榜数据 | Get Douyin hot search results
    async def fetch_hot_search_result(self):
        """
        获取抖音热榜数据 | Get Douyin hot search results
        :return: 热榜数据 | Hot search results
        """
        endpoint = "/api/v1/douyin/web/fetch_hot_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 抖音视频频道数据 | Douyin video channel data
    async def fetch_video_channel_result(self, tag_id: int, count: int, refresh_index: int):
        """
        抖音视频频道数据 | Douyin video channel data
        :param tag_id: 标签id | Tag id
        :param count: 数量 | Number
        :param refresh_index: 刷新索引 | Refresh index
        :return: 视频频道数据 | Video channel data
        """
        endpoint = "/api/v1/douyin/web/fetch_video_channel_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?tag_id={tag_id}&count={count}&refresh_index={refresh_index}")
        return data

    # 获取抖音Web的游客Cookie | Get the guest Cookie of Douyin Web
    async def fetch_douyin_web_guest_cookie(self, user_agent: str):
        """
        获取抖音Web的游客Cookie | Get the guest Cookie of Douyin Web
        :param user_agent: 用户浏览器代理 | User browser agent
        :return: 游客Cookie | Guest Cookie
        """
        endpoint = "/api/v1/douyin/web/fetch_douyin_web_guest_cookie"
        data = await self.client.fetch_get_json(f"{endpoint}?user_agent={user_agent}")
        return data

    # 生成真实msToken | Generate real msToken
    async def gen_real_msToken(self):
        """
        生成真实msToken | Generate real msToken
        :return: msToken
        """
        endpoint = "/api/v1/douyin/web/generate_real_msToken"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 生成ttwid | Generate ttwid
    async def gen_ttwid(self):
        """
        生成ttwid | Generate ttwid
        :return: ttwid
        """
        endpoint = "/api/v1/douyin/web/generate_ttwid"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 生成verify_fp | Generate verify_fp
    async def gen_verify_fp(self):
        """
        生成verify_fp | Generate verify_fp
        :return: verify_fp
        """
        endpoint = "/api/v1/douyin/web/generate_verify_fp"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 生成s_v_web_id | Generate s_v_web_id
    async def gen_s_v_web_id(self):
        """
        生成s_v_web_id | Generate s_v_web_id
        :return: s_v_web_id
        """
        endpoint = "/api/v1/douyin/web/generate_s_v_web_id"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 使用接口地址生成Xbogus参数 | Generate Xbogus parameters using the interface address
    async def get_x_bogus(self, url: str, user_agent: str):
        """
        使用接口地址生成Xbogus参数 | Generate Xbogus parameters using the interface address
        :param url: 接口地址 | Interface address
        :param user_agent: 用户代理 | User agent
        :return: Xbogus参数 | Xbogus parameters
        """
        endpoint = "/api/v1/douyin/web/generate_x_bogus"
        data = await self.client.fetch_post_json(f"{endpoint}", params={"url": url, "user_agent": user_agent})
        return data

    # 使用接口地址生成Abogus参数 | Generate Abogus parameters using the interface address
    async def get_a_bogus(self, url: str, data: str, user_agent: str, index_0: int, index_1: int, index_2: int):
        """
        使用接口地址生成Abogus参数 | Generate Abogus parameters using the interface address
        :param url: 接口地址，需要使用urlencode(data, safe="*")进行编码 | Interface address, need to be encoded using urlencode(data, safe="*")
        :param data: body，需要使用urlencode(data, safe="*")进行编码 | body, need to be encoded using urlencode(data, safe="*")
        :param user_agent: user-agent
        :param index_0: 加密明文列表的第一个值，无特殊要求，默认为0，不要随意修改 | The first value of the encryption plaintext list, no special requirements, the default is 0, do not modify it at will
        :param index_1: 加密明文列表的第二个值，无特殊要求，默认为1，不要随意修改 | The second value of the encryption plaintext list, no special requirements, the default is 1, do not modify it at will
        :param index_2: 加密明文列表的第三个值，无特殊要求，默认为14，不要随意修改 | The third value of the encryption plaintext list, no special requirements, the default is 14, do not modify it at will
        :return: Abogus参数 | Abogus parameters
        """
        endpoint = "/api/v1/douyin/web/generate_a_bogus"
        data = await self.client.fetch_post_json(
            f"{endpoint}",
            params={"url": url, "data": data, "user_agent": user_agent, "index_0": index_0, "index_1": index_1,
                    "index_2": index_2})
        return data

    # 提取单个用户id | Extract single user id
    async def get_sec_user_id(self, url: str):
        """
        提取单个用户id | Extract single user id
        :param url: 用户主页链接 | User homepage link
        :return: 用户sec_user_id
        """
        endpoint = "/api/v1/douyin/web/get_sec_user_id"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 提取列表用户id | Extract list user id
    async def get_all_sec_user_id(self, url: list):
        """
        提取列表用户id | Extract list user id
        :param url: 用户主页链接列表（最多支持20个链接） | User homepage link list (supports up to 20 links)
        :return: 用户sec_user_id列表 | User sec_user_id list
        """
        endpoint = "/api/v1/douyin/web/get_all_sec_user_id"
        data = await self.client.fetch_post_json(f"{endpoint}", data=json.dumps(url))
        return data

    # 提取单个作品id | Extract single video id
    async def get_aweme_id(self, url: str):
        """
        提取单个作品id | Extract single video id
        :param url: 作品链接 | Video link
        :return: 作品id | Video id
        """
        endpoint = "/api/v1/douyin/web/get_aweme_id"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 提取列表作品id | Extract list video id
    async def get_all_aweme_id(self, url: list):
        """
        提取列表作品id | Extract list video id
        :param url: 作品链接列表（最多支持20个链接） | Video link list (supports up to 20 links)
        :return: 作品id列表 | Video id list
        """
        endpoint = "/api/v1/douyin/web/get_all_aweme_id"
        data = await self.client.fetch_post_json(f"{endpoint}", data=json.dumps(url))
        return data

    # 提取直播间号 | Extract webcast id
    async def get_webcast_id(self, url: str):
        """
        提取直播间号 | Extract webcast id
        :param url: 直播间链接 | Room link
        :return: 直播间号 | Room id
        """
        endpoint = "/api/v1/douyin/web/get_webcast_id"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 提取列表直播间号 | Extract list webcast id
    async def get_all_webcast_id(self, url: list):
        """
        提取列表直播间号 | Extract list webcast id
        :param url: 直播间链接列表（最多支持20个链接） | Room link list (supports up to 20 links)
        :return: 直播间号列表 | Room id list
        """
        endpoint = "/api/v1/douyin/web/get_all_webcast_id"
        # 将列表转换为json格式 | Convert the list to json format
        data = await self.client.fetch_post_json(f"{endpoint}", data=json.dumps(url))
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer jZVuQT5gm2gDj3IB0XKPySMV9B4EmLfyqo5okGfltWp7/VAgQt8unAaMEA=="})

        douyin_web = DouyinWeb(client)

        # 获取单个作品数据 | Get single video data
        # data = await douyin_web.fetch_one_video("7345492945006595379")
        # print(f"fetch_one_video: {data}")

        # 获取单个作品视频弹幕数据 | Get single video danmaku data
        # data = await douyin_web.fetch_one_video_danmaku("7355433624046472498", 15134, 15133, 0)
        # print(f"fetch_one_video_danmaku: {data}")

        # 获取用户主页作品数据 | Get user homepage video data
        # data = await douyin_web.fetch_user_post_videos("MS4wLjABAAAA6Zb5Z5Vv4X3v4VH9VX1z3Y0QV2z6FyJQJ8Q2H3J9zY", 0, 10)
        # print(f"fetch_user_post_videos: {data}")

        # 获取用户喜欢作品数据 | Get user like video data
        # data = await douyin_web.fetch_user_like_videos("MS4wLjABAAAA6Zb5Z5Vv4X3v4VH9VX1z3Y0QV2z6FyJQJ8Q2H3J9zY", 0, 10)
        # print(f"fetch_user_like_videos: {data}")

        # 获取用户收藏作品数据 | Get user collection video data
        # data = await douyin_web.fetch_user_collection_videos("cookie", 0, 10)
        # print(f"fetch_user_collection_videos: {data}")

        # 获取用户合辑作品数据 | Get user mix video data
        # data = await douyin_web.fetch_user_mix_videos("MS4wLjABAAAA6Zb5Z5Vv4X3v4VH9VX1z3Y0QV2z6FyJQJ8Q2H3J9zY", 0, 10)
        # print(f"fetch_user_mix_videos: {data}")

        # 获取用户直播流数据 | Get user live video data
        # data = await douyin_web.fetch_user_live_videos("MS4wLjABAAAA6Zb5Z5Vv4X3v4VH9VX1z3Y0QV2z6FyJQJ8Q2H3J9zY")
        # print(f"fetch_user_live_videos: {data}")

        # 获取指定用户的直播流数据 | Get live video data of specified user
        # data = await douyin_web.fetch_user_live_videos_by_room_id("6958745176821132813")
        # print(f"fetch_user_live_videos_by_room_id: {data}")

        # 获取直播间送礼用户排行榜 | Get live room gift user ranking
        # data = await douyin_web.fetch_live_gift_ranking("6958745176821132813", 1)
        # print(f"fetch_live_gift_ranking: {data}")

        # 抖音直播间商品信息 | Douyin live room product information
        # data = await douyin_web.fetch_live_room_product_result("6958745176821132813", "6958745176821132813", 10)
        # print(f"fetch_live_room_product_result: {data}")

        # 获取指定用户的信息 | Get information of specified user
        # data = await douyin_web.handler_user_profile("MS4wLjABAAAA6Zb5Z5Vv4X3v4VH9VX1z3Y0QV2z6FyJQJ8Q2H3J9zY")
        # print(f"handler_user_profile: {data}")

        # 获取单个视频评论数据 | Get single video comments data
        # data = await douyin_web.fetch_video_comments("7355433624046472498", 0, 10)
        # print(f"fetch_video_comments: {data}")

        # 获取指定视频的评论回复数据 | Get comment replies data of specified video
        # data = await douyin_web.fetch_video_comments_reply("7355433624046472498", "7355433624046472498", 0, 10)
        # print(f"fetch_video_comments_reply: {data}")

        # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
        # data = await douyin_web.fetch_general_search_result("抖音", 0, 10, "0", "0", "0")
        # print(f"fetch_general_search_result: {data}")

        # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
        # data = await douyin_web.fetch_video_search_result("抖音", 0, 10, "0", "0", "0")
        # print(f"fetch_video_search_result: {data}")

        # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
        # data = await douyin_web.fetch_user_search_result("抖音", 0, 10, "", "")
        # print(f"fetch_user_search_result: {data}")

        # 获取指定关键词的直播搜索结果 | Get live search results of specified keywords
        # data = await douyin_web.fetch_live_search_result("抖音", 0, 10)
        # print(f"fetch_live_search_result: {data}")

        # 获取抖音热榜数据 | Get Douyin hot search results
        # data = await douyin_web.fetch_hot_search_result()
        # print(f"fetch_hot_search_result: {data}")

        # 抖音视频频道数据 | Douyin video channel data
        # data = await douyin_web.fetch_video_channel_result(0, 10, 0)
        # print(f"fetch_video_channel_result: {data}")

        # 获取抖音Web的游客Cookie | Get the guest Cookie of Douyin Web
        # data = await douyin_web.fetch_douyin_web_guest_cookie("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        # print(f"fetch_douyin_web_guest_cookie: {data}")

        # 生成真实msToken | Generate real msToken
        # data = await douyin_web.gen_real_msToken()
        # print(f"gen_real_msToken: {data}")

        # 生成ttwid | Generate ttwid
        # data = await douyin_web.gen_ttwid()
        # print(f"gen_ttwid: {data}")

        # 生成verify_fp | Generate verify_fp
        # data = await douyin_web.gen_verify_fp()
        # print(f"gen_verify_fp: {data}")

        # 生成s_v_web_id | Generate s_v_web_id
        # data = await douyin_web.gen_s_v_web_id()
        # print(f"gen_s_v_web_id: {data}")

        # 使用接口地址生成Xbogus参数 | Generate Xbogus parameters using the interface address
        # data = await douyin_web.get_x_bogus("https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engine_version=",
        #                                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
        # print(f"get_x_bogus: {data}")

        # 使用接口地址生成Abogus参数 | Generate Abogus parameters using the interface address
        # data = await douyin_web.get_a_bogus("https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engine_version=",
        #                                   "",
        #                                     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        #                                     0,
        #                                     1,
        #                                     14,
        #                                     )
        # print(f"get_a_bogus: {data}")

        # 提取单个用户id | Extract single user id
        # data = await douyin_web.get_sec_user_id("https://www.douyin.com/user/MS4wLjABAAAA6Zb5Z5Vv4X3v4VH9VX1z3Y0QV2z6FyJQJ8Q2H3J9zY")
        # print(f"get_sec_user_id: {data}")

        # 提取列表用户id | Extract list user id
        # data = await douyin_web.get_all_sec_user_id(["https://www.douyin.com/user/MS4wLjABAAAA6Zb5Z5Vv4X3v4VH9VX1z3Y0QV2z6FyJQJ8Q2H3J9zY"])
        # print(f"get_all_sec_user_id: {data}")

        # 提取单个作品id | Extract single video id
        # data = await douyin_web.get_aweme_id("https://www.douyin.com/video/7355433624046472498")
        # print(f"get_aweme_id: {data}")

        # 提取列表作品id | Extract list video id
        # data = await douyin_web.get_all_aweme_id(["https://www.douyin.com/video/7355433624046472498"])
        # print(f"get_all_aweme_id: {data}")

        # 提取直播间号 | Extract webcast id
        # data = await douyin_web.get_webcast_id("https://v.douyin.com/i8tBR7hX/")
        # print(f"get_webcast_id: {data}")

        # 提取列表直播间号 | Extract list webcast id
        # data = await douyin_web.get_all_webcast_id([
        #     "https://live.douyin.com/775841227732",
        #     "https://live.douyin.com/775841227732?room_id=7318296342189919011&enter_from_merge=web_share_link&enter_method=web_share_link&previous_page=app_code_link",
        #     "https://webcast.amemv.com/douyin/webcast/reflow/7318296342189919011?u_code=l1j9bkbd&did=MS4wLjABAAAAEs86TBQPNwAo-RGrcxWyCdwKhI66AK3Pqf3ieo6HaxI&iid=MS4wLjABAAAA0ptpM-zzoliLEeyvWOCUt-_dQza4uSjlIvbtIazXnCY&with_sec_did=1&use_link_command=1&ecom_share_track_params=&extra_params={\"from_request_id\":\"20231230162057EC005772A8EAA0199906\",\"im_channel_invite_id\":\"0\"}&user_id=3644207898042206&liveId=7318296342189919011&from=share&style=share&enter_method=click_share&roomId=7318296342189919011&activity_info={}",
        #     "6i- Q@x.Sl 03/23 【醒子8ke的直播间】  点击打开👉https://v.douyin.com/i8tBR7hX/  或长按复制此条消息，打开抖音，看TA直播",
        #     "https://v.douyin.com/i8tBR7hX/"
        # ])
        # print(f"get_all_webcast_id: {data}")


    # 运行异步事件循环 | Run asynchronous event loop
    asyncio.run(main())
