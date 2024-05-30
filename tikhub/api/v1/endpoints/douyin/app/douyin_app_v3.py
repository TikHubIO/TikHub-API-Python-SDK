# 导入API SDK Client类

from tikhub.http_client.api_client import APIClient

# 标记已废弃的方法
from tikhub.http_client.deprecated import deprecated


class DouyinAppV3:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取单个作品数据
    async def fetch_one_video(self, aweme_id: str):
        endpoint = f"/api/v1/douyin/app/v3/fetch_one_video"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}")
        return data

    # 获取指定用户的信息
    async def handler_user_profile(self, sec_user_id: str):
        endpoint = f"/api/v1/douyin/app/v3/handler_user_profile"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}")
        return data

    # 获取用户作品集合数据
    async def fetch_user_post_videos(self, sec_user_id: str, max_cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_user_post_videos"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&count={count}")
        return data

    # 获取用户喜欢作品数据
    async def fetch_user_like_videos(self, sec_user_id: str, max_cursor: int, counts: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_user_like_videos"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&counts={counts}")
        return data

    # 获取单个视频评论数据
    async def fetch_video_comments(self, aweme_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_video_comments"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定视频的评论回复数据
    async def fetch_video_comments_reply(self, item_id: str, comment_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_video_comment_replies"
        data = await self.client.fetch_get_json(f"{endpoint}?item_id={item_id}&comment_id={comment_id}&cursor={cursor}&count={count}")
        return data

    # 抖音视频合集详情数据
    async def fetch_video_mix_detail(self, mix_id: str):
        endpoint = f"/api/v1/douyin/app/v3/fetch_video_mix_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?mix_id={mix_id}")
        return data

    # 抖音视频合集作品列表数据
    async def fetch_video_mix_post_list(self, mix_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_video_mix_post_list"
        data = await self.client.fetch_get_json(f"{endpoint}?mix_id={mix_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定关键词的综合搜索结果
    async def fetch_general_search_result(self, keyword: str, offset: int, count: int, sort_type: str, publish_time: str, filter_duration: str, content_type: str):
        endpoint = f"/api/v1/douyin/app/v3/fetch_general_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}&content_type={content_type}")
        return data

    # 获取指定关键词的视频搜索结果
    async def fetch_video_search_result(self, keyword: str, offset: int, count: int, sort_type: str, publish_time: str, filter_duration: str):
        endpoint = f"/api/v1/douyin/app/v3/fetch_video_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}")
        return data

    # 获取指定关键词的用户搜索结果
    async def fetch_user_search_result(self, keyword: str, offset: int, count: int, douyin_user_fans: str, douyin_user_type: str):
        endpoint = f"/api/v1/douyin/app/v3/fetch_user_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&douyin_user_fans={douyin_user_fans}&douyin_user_type={douyin_user_type}")
        return data

    # 获取指定关键词的直播搜索结果
    async def fetch_live_search_result(self, keyword: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_live_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&cursor={cursor}&count={count}")
        return data

    # 获取指定关键词的音乐搜索结果
    async def fetch_music_search_result(self, keyword: str, offset: int, count: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_music_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定关键词的话题搜索结果
    async def fetch_hashtag_search_result(self, keyword: str, offset: int, count: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_hashtag_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定音乐的详情数据
    async def fetch_music_detail(self, music_id: str):
        endpoint = f"/api/v1/douyin/app/v3/fetch_music_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}")
        return data

    # 抖音音乐视频列表结果
    async def fetch_music_video_list(self, music_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_music_video_list"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}&cursor={cursor}&count={count}")
        return data

    # 抖音话题详情数据
    async def fetch_hashtag_detail(self, ch_id: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_hashtag_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?ch_id={ch_id}")
        return data

    # 获取指定话题的作品数据
    async def fetch_hashtag_video_list(self, ch_id: int, cursor: int, sort_type: int, count: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_hashtag_video_list"
        data = await self.client.fetch_get_json(f"{endpoint}?ch_id={ch_id}&cursor={cursor}&sort_type={sort_type}&count={count}")
        return data

    # 抖音热搜榜数据
    async def fetch_hot_search_list(self):
        endpoint = f"/api/v1/douyin/app/v3/fetch_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 抖音直播热搜榜数据
    async def fetch_hot_live_search(self):
        endpoint = f"/api/v1/douyin/app/v3/fetch_live_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 抖音音乐热榜数据
    async def fetch_hot_music_search(self):
        endpoint = f"/api/v1/douyin/app/v3/fetch_music_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 抖音品牌热榜分类数据
    async def fetch_hot_brand_search_category(self):
        endpoint = f"/api/v1/douyin/app/v3/fetch_brand_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 抖音品牌热榜具体分类数据
    async def fetch_hot_brand_search(self, category_id: int):
        endpoint = f"/api/v1/douyin/app/v3/fetch_brand_hot_search_list_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?category_id={category_id}")
        return data

    # 生成抖音短链接
    async def fetch_douyin_short_url(self, url: str):
        endpoint = f"/api/v1/douyin/app/v3/generate_douyin_short_url"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 生成抖音视频分享二维码
    async def fetch_douyin_video_qrcode(self, object_id: str):
        endpoint = f"/api/v1/douyin/app/v3/generate_douyin_video_share_qrcode"
        data = await self.client.fetch_get_json(f"{endpoint}?object_id={object_id}")
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        douyin_app_v3 = DouyinAppV3(client)

        # 获取单个作品数据
        data = await douyin_app_v3.fetch_one_video("6954433834136592141")
        print(data)

        # 获取指定用户的信息
        data = await douyin_app_v3.handler_user_profile("MS4wLjABAAAA9VQ5z5zq8s7tjUvJ1nJYwzYz1pQ5Zb1z9z4Q1z4z1o")
        print(data)

        # 获取用户作品集合数据
        data = await douyin_app_v3.fetch_user_post_videos("MS4wLjABAAAA9VQ5z5zq8s7tjUvJ1nJYwzYz1pQ5Zb1z9z4Q1z4z1o", 0, 10)
        print(data)

        # 获取用户喜欢作品数据
        data = await douyin_app_v3.fetch_user_like_videos("MS4wLjABAAAA9VQ5z5zq8s7tjUvJ1nJYwzYz1pQ5Zb1z9z4Q1z4z1o", 0, 10)
        print(data)

        # 获取单个视频评论数据
        data = await douyin_app_v3.fetch_video_comments("6954433834136592141", 0, 10)
        print(data)

        # 获取指定视频的评论回复数据
        data = await douyin_app_v3.fetch_video_comments_reply("6954433834136592141", "6954433834136592141", 0, 10)
        print(data)

        # 抖音视频合集详情数据
        data = await douyin_app_v3.fetch_video_mix_detail("6954433834136592141")
        print(data)

        # 抖音视频合集作品列表数据
        data = await douyin_app_v3.fetch_video_mix_post_list("6954433834136592141", 0, 10)
        print(data)

        # 获取指定关键词的综合搜索结果
        data = await douyin_app_v3.fetch_general_search_result("抖音", 0, 10, "general", "all", "all", "all")
        print(data)

        # 获取指定关键词的视频搜索结果
        data = await douyin_app_v3.fetch_video_search_result("抖音", 0, 10, "general", "all", "all")
        print(data)

        # 获取指定关键词的用户搜索结果
        data = await douyin_app_v3.fetch_user_search_result("抖音", 0, 10, "all", "all")
        print(data)

        # 获取指定关键词的直播搜索结果
        data = await douyin_app_v3.fetch_live_search_result("抖音", 0, 10)
        print(data)

        # 获取指定关键词的音乐搜索结果
        data = await douyin_app_v3.fetch_music_search_result("抖音", 0, 10)
        print(data)

        # 获取指定关键词的话题搜索结果
        data = await douyin_app_v3.fetch_hashtag_search_result("抖音", 0, 10)
        print(data)

        # 获取指定音乐的详情数据
        data = await douyin_app_v3.fetch_music_detail("6954433834136592141")
        print(data)

        # 抖音音乐视频列表结果
        data = await douyin_app_v3.fetch_music_video_list("6954433834136592141", 0, 10)
        print(data)

        # 抖音话题详情数据
        data = await douyin_app_v3.fetch_hashtag_detail(6954433834136592141)
        print(data)

        # 获取指定话题的作品数据
        data = await douyin_app_v3.fetch_hashtag_video_list(6954433834136592141, 0, 0, 10)
        print(data)

        # 抖音热搜榜数据
        data = await douyin_app_v3.fetch_hot_search_list()
        print(data)

        # 抖音直播热搜榜数据
        data = await douyin_app_v3.fetch_hot_live_search()
        print(data)

        # 抖音音乐热榜数据
        data = await douyin_app_v3.fetch_hot_music_search()
        print(data)

        # 抖音品牌热榜分类数据
        data = await douyin_app_v3.fetch_hot_brand_search_category()
        print(data)

        # 抖音品牌热榜具体分类数据
        data = await douyin_app_v3.fetch_hot_brand_search(1)
        print(data)

        # 生成抖音短链接
        data = await douyin_app_v3.fetch_douyin_short_url("https://v.douyin.com/e8e3m5v/")
        print(data)

        # 生成抖音视频分享二维码
        data = await douyin_app_v3.fetch_douyin_video_qrcode("6954433834136592141")
        print(data)


    asyncio.run(main())