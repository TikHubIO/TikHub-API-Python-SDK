# 导入API SDK Client类

from tikhub.http_client.api_client import APIClient

# 标记已废弃的方法
from tikhub.http_client.deprecated import deprecated


class DouyinAppV2:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取单个作品数据 | Get single video data
    async def fetch_one_video(self, aweme_id: str):
        endpoint = f"/api/v1/douyin/app/v2/fetch_one_video"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}")
        return data

    # 获取指定用户的信息 | Get information of specified user
    async def handler_user_profile(self, sec_user_id: str):
        endpoint = f"/api/v1/douyin/app/v2/handler_user_profile"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}")
        return data

    # 获取用户主页作品数据 | Get user homepage video data
    async def fetch_user_post_videos(self, sec_user_id: str, max_cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_user_post_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&count={count}")
        return data

    # 获取用户喜欢作品数据 | Get user like video data
    async def fetch_user_like_videos(self, sec_user_id: str, max_cursor: int, counts: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_user_like_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&counts={counts}")
        return data

    # 获取单个视频评论数据 | Get single video comments data
    async def fetch_video_comments(self, aweme_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_video_comments"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定视频的评论回复数据 | Get comment replies data of specified video
    async def fetch_video_comments_reply(self, item_id: str, comment_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_video_comment_replies"
        data = await self.client.fetch_get_json(
            f"{endpoint}?item_id={item_id}&comment_id={comment_id}&cursor={cursor}&count={count}")
        return data

    # 获取抖音视频合集详情数据 | Get Douyin video mix detail data
    async def fetch_video_mix_detail(self, mix_id: str):
        endpoint = f"/api/v1/douyin/app/v2/fetch_video_mix_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?mix_id={mix_id}")
        return data

    # 获取抖音视频合集作品列表数据 | Get Douyin video mix post list data
    async def fetch_video_mix_post_list(self, mix_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_video_mix_post_list"
        data = await self.client.fetch_get_json(f"{endpoint}?mix_id={mix_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
    @deprecated(
        "fetch_hashtag_detail is deprecated and will be removed in a future release. Use V3 API instead. | fetch_hashtag_detail已弃用，将在未来版本中删除。请使用V3 API。")
    async def fetch_general_search_result(self, keyword: str, offset: int, count: int, sort_type: int,
                                          publish_time: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_general_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}")
        return data

    # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
    @deprecated(
        "fetch_hashtag_detail is deprecated and will be removed in a future release. Use V3 API instead. | fetch_hashtag_detail已弃用，将在未来版本中删除。请使用V3 API。")
    async def fetch_video_search_result(self, keyword: str, offset: int, count: int, sort_type: int, publish_time: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_video_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}")
        return data

    # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
    @deprecated(
        "fetch_hashtag_detail is deprecated and will be removed in a future release. Use V3 API instead. | fetch_hashtag_detail已弃用，将在未来版本中删除。请使用V3 API。")
    async def fetch_user_search_result(self, keyword: str, offset: int, count: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_user_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定关键词的音乐搜索结果 | Get music search results of specified keywords
    @deprecated(
        "fetch_hashtag_detail is deprecated and will be removed in a future release. Use V3 API instead. | fetch_hashtag_detail已弃用，将在未来版本中删除。请使用V3 API。")
    async def fetch_music_search_result(self, keyword: str, offset: int, count: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_music_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定关键词的话题搜索结果 | Get topic search results of specified keywords
    @deprecated(
        "fetch_hashtag_detail is deprecated and will be removed in a future release. Use V3 API instead. | fetch_hashtag_detail已弃用，将在未来版本中删除。请使用V3 API。")
    async def fetch_hashtag_search_result(self, keyword: str, offset: int, count: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_hashtag_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定音乐的详情数据 | Get details of specified music
    async def fetch_music_detail(self, music_id: str):
        endpoint = f"/api/v1/douyin/app/v2/fetch_music_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}")
        return data

    # 抖音音乐视频列表结果 | Douyin music video list result
    async def fetch_music_video_list(self, music_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_music_video_list"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}&cursor={cursor}&count={count}")
        return data

    # 抖音话题详情数据 | Douyin topic details data
    @deprecated("fetch_hashtag_detail is deprecated and will be removed in a future release. Use V3 API instead. | fetch_hashtag_detail已弃用，将在未来版本中删除。请使用V3 API。")
    async def fetch_hashtag_detail(self, ch_id: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_hashtag_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?ch_id={ch_id}")
        return data

    # 获取指定话题的作品数据 | Get video data of specified topic
    async def fetch_hashtag_video_list(self, ch_id: int, cursor: int, count: int, sort_type: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_hashtag_video_list"
        data = await self.client.fetch_get_json(
            f"{endpoint}?ch_id={ch_id}&cursor={cursor}&count={count}&sort_type={sort_type}")
        return data

    # 抖音热搜榜数据 | Douyin hot search list data
    async def fetch_hot_search_list(self):
        endpoint = f"/api/v1/douyin/app/v2/fetch_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 抖音直播热搜榜数据 | Douyin live hot search list data
    async def fetch_live_hot_search_list(self):
        endpoint = f"/api/v1/douyin/app/v2/fetch_live_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 抖音音乐热榜数据 | Douyin music hot search list data
    async def fetch_hot_music_search(self):
        endpoint = f"/api/v1/douyin/app/v2/fetch_music_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 抖音品牌热榜分类数据 | Douyin brand hot search category data
    async def fetch_hot_brand_search_category(self):
        endpoint = f"/api/v1/douyin/app/v2/fetch_brand_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 抖音品牌热榜具体分类数据 | Douyin brand hot search list detail data
    async def fetch_brand_hot_search_list_detail(self, category_id: int):
        endpoint = f"/api/v1/douyin/app/v2/fetch_brand_hot_search_list_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?category_id={category_id}")
        return data

    # 生成抖音短链接 | Generate Douyin short link
    async def generate_douyin_short_url(self, url: str):
        endpoint = f"/api/v1/douyin/app/v2/generate_douyin_short_url"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 生成抖音视频分享二维码 | Generate Douyin video share QR code
    async def generate_douyin_video_share_qrcode(self, object_id: int):
        endpoint = f"/api/v1/douyin/app/v2/generate_douyin_video_share_qrcode"
        data = await self.client.fetch_get_json(f"{endpoint}?object_id={object_id}")
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        douyin_app_v2 = DouyinAppV2(client)

        # # 获取单个作品数据 | Get single video data
        # data = await douyin_app_v2.fetch_one_video(aweme_id="7345492945006595379")
        # print(f"fetch_one_video: {data}")
        #
        # # 获取单个视频评论数据 | Get single video comments data
        # data = await douyin_app_v2.fetch_video_comments(aweme_id="7345492945006595379", cursor=0, count=10)
        # print(f"fetch_video_comments: {data}")
        #
        # # 获取指定视频的评论回复数据 | Get comment replies data of specified video
        # data = await douyin_app_v2.fetch_video_comments_reply(item_id="7354666303006723354",
        #                                                       comment_id="7354669356632638218",
        #                                                       cursor=0,
        #                                                       count=10)
        # print(f"fetch_video_comments_reply: {data}")
        #
        # # 抖音视频合集详情数据 | Douyin video mix detail data
        # data = await douyin_app_v2.fetch_video_mix_detail(mix_id="7302011174286002217")
        # print(f"fetch_video_mix_detail: {data}")
        #
        # # 抖音视频合集作品列表数据 | Douyin video mix post list data
        # data = await douyin_app_v2.fetch_video_mix_post_list(mix_id="7302011174286002217", cursor=0, count=10)
        # print(f"fetch_video_mix_post_list: {data}")
        #
        # # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
        # data = await douyin_app_v2.fetch_general_search_result(keyword="中华娘", offset=0, count=20, sort_type=0,
        #                                                        publish_time=0)
        # print(f"fetch_general_search_result: {data}")
        #
        # # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
        # data = await douyin_app_v2.fetch_video_search_result(keyword="中华娘", offset=0, count=20, sort_type=0,
        #                                                      publish_time=0)
        # print(f"fetch_video_search_result: {data}")
        #
        # # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
        # data = await douyin_app_v2.fetch_user_search_result(keyword="中华娘", offset=0, count=20)
        # print(f"fetch_user_search_result: {data}")
        #
        # # 获取指定关键词的音乐搜索结果 | Get music search results of specified keywords
        # data = await douyin_app_v2.fetch_music_search_result(keyword="中华娘", offset=0, count=20)
        # print(f"fetch_music_search_result: {data}")
        #
        # # 获取指定关键词的话题搜索结果 | Get hashtag search results of specified keywords
        # data = await douyin_app_v2.fetch_hashtag_search_result(keyword="中华娘", offset=0, count=20)
        # print(f"fetch_hashtag_search_result: {data}")
        #
        # # 获取指定音乐的详情数据 | Get details of specified music
        # data = await douyin_app_v2.fetch_music_detail(music_id="7136850194742315016")
        # print(f"fetch_music_detail: {data}")
        #
        # # 抖音音乐视频列表结果 | Get video list of specified music
        # data = await douyin_app_v2.fetch_music_video_list(music_id="7136850194742315016", cursor=0, count=10)
        # print(f"fetch_music_video_list: {data}")

        # 抖音话题详情数据 | Get details of specified hashtag
        # data = await douyin_app_v2.fetch_hashtag_detail(ch_id=1575791821492238)
        # print(f"fetch_hashtag_detail: {data}")

        # # 获取指定话题的作品数据 | Get video list of specified hashtag
        # data = await douyin_app_v2.fetch_hashtag_video_list(ch_id=1575791821492238, cursor=0, sort_type=0, count=10)
        # print(f"fetch_hashtag_video_list: {data}")
        #
        # # 抖音热搜榜数据 | Get Douyin hot search list data
        # data = await douyin_app_v2.fetch_hot_search_list()
        # print(f"fetch_hot_search_list: {data}")
        #
        # # 抖音直播热搜榜数据 | Get Douyin live hot search list data
        # data = await douyin_app_v2.fetch_live_hot_search_list()
        # print(f"fetch_live_hot_search_list: {data}")
        #
        # # 抖音音乐热榜数据 | Get Douyin music hot search list data
        # data = await douyin_app_v2.fetch_hot_music_search()
        # print(f"fetch_hot_music_search: {data}")
        #
        # # 抖音品牌热榜分类数据 | Get Douyin brand hot search category data
        # data = await douyin_app_v2.fetch_hot_brand_search_category()
        # print(f"fetch_hot_brand_search_category: {data}")
        #
        # # 抖音品牌热榜具体分类数据 | Get Douyin brand hot search list detail data
        # data = await douyin_app_v2.fetch_brand_hot_search_list_detail(category_id=1)
        # print(f"fetch_brand_hot_search_list_detail: {data}")
        #
        # # 生成抖音短链接 | Generate Douyin short link
        # data = await douyin_app_v2.generate_douyin_short_url(url="https://v.douyin.com/e3m8a8t/")
        # print(f"generate_douyin_short_url: {data}")

        # 生成抖音视频分享二维码 | Generate Douyin video share QR code
        # data = await douyin_app_v2.generate_douyin_video_share_qrcode(object_id=7348044435755846962)
        # print(f"generate_douyin_video_share_qrcode: {data}")


    asyncio.run(main())
