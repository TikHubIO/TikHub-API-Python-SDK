# 导入API SDK Client类

from tikhub.http_client.api_client import APIClient


class DouyinAppV1:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取单个作品数据 | Get single video data
    async def fetch_one_video(self, aweme_id: str):
        endpoint = f"/api/v1/douyin/app/v1/fetch_one_video?aweme_id={aweme_id}"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}")
        return data

    # 根据分享链接获取作品数据 | Get video data by sharing url
    async def fetch_one_video_by_share_url(self, share_url: str):
        endpoint = "/api/v1/douyin/app/v1/fetch_one_video_by_share_url"
        data = await self.client.fetch_get_json(f"{endpoint}?share_url={share_url}")
        return data

    # 获取指定用户的信息 | Get information of specified user
    async def handler_user_profile(self, sec_user_id: str):
        endpoint = f"/api/v1/douyin/app/v1/handler_user_profile?sec_user_id={sec_user_id}"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}")
        return data

    # 获取用户主页作品数据 | Get user homepage video data
    async def fetch_user_post_videos(self, sec_user_id: str, max_cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_user_post_videos?sec_user_id={sec_user_id}&max_cursor={max_cursor}&count={count}"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&count={count}")
        return data

    # 获取用户喜欢作品数据 | Get user like video data
    async def fetch_user_like_videos(self, sec_user_id: str, max_cursor: int, counts: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_user_like_videos?sec_user_id={sec_user_id}&max_cursor={max_cursor}&counts={counts}"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&counts={counts}")
        return data

    # 获取单个视频评论数据 | Get single video comments data
    async def fetch_video_comments(self, aweme_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_video_comments?aweme_id={aweme_id}&cursor={cursor}&count={count}"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定视频的评论回复数据 | Get comment replies data of specified video
    async def fetch_video_comments_reply(self, item_id: str, comment_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_video_comment_replies?item_id={item_id}&comment_id={comment_id}&cursor={cursor}&count={count}"
        data = await self.client.fetch_get_json(
            f"{endpoint}?item_id={item_id}&comment_id={comment_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
    async def fetch_general_search_result(self, keyword: str, offset: int, count: int, sort_type: int,
                                          publish_time: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_general_search_result?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}")
        return data

    # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
    async def fetch_video_search_result(self, keyword: str, offset: int, count: int, sort_type: int, publish_time: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_video_search_result?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}")
        return data

    # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
    async def fetch_user_search_result(self, keyword: str, offset: int, count: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_user_search_result?keyword={keyword}&offset={offset}&count={count}"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定关键词的音乐搜索结果 | Get music search results of specified keywords
    async def fetch_music_search_result(self, keyword: str, offset: int, count: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_music_search_result?keyword={keyword}&offset={offset}&count={count}"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定关键词的话题搜索结果 | Get hashtag search results of specified keywords
    async def fetch_hashtag_search_result(self, keyword: str, offset: int, count: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_hashtag_search_result?keyword={keyword}&offset={offset}&count={count}"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定音乐的详情数据 | Get details of specified music
    async def fetch_music_detail(self, music_id: str):
        endpoint = f"/api/v1/douyin/app/v1/fetch_music_detail?music_id={music_id}"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}")
        return data

    # 获取指定音乐的视频列表数据 | Get video list of specified music
    async def fetch_music_video_list(self, music_id: str, cursor: int, count: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_music_video_list?music_id={music_id}&cursor={cursor}&count={count}"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定话题的详情数据 | Get details of specified hashtag
    async def fetch_hashtag_detail(self, ch_id: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_hashtag_detail?ch_id={ch_id}"
        data = await self.client.fetch_get_json(f"{endpoint}?ch_id={ch_id}")
        return data

    # 获取指定话题的作品数据 | Get video list of specified hashtag
    async def fetch_hashtag_post_list(self, ch_id: int, cursor: int, count: int, sort_type: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_hashtag_video_list?ch_id={ch_id}&cursor={cursor}&count={count}&sort_type={sort_type}"
        data = await self.client.fetch_get_json(
            f"{endpoint}?ch_id={ch_id}&cursor={cursor}&count={count}&sort_type={sort_type}")
        return data

    # 获取抖音热搜榜数据 | Get Douyin hot search list data
    async def fetch_hot_search_list(self):
        endpoint = f"/api/v1/douyin/app/v1/fetch_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 获取抖音直播热搜榜数据 | Get Douyin live hot search list data
    async def fetch_hot_live_search(self):
        endpoint = f"/api/v1/douyin/app/v1/fetch_live_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 获取抖音音乐热榜数据 | Get Douyin music hot search list data
    async def fetch_hot_music_search(self):
        endpoint = f"/api/v1/douyin/app/v1/fetch_music_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 获取抖音品牌热榜分类数据 | Get Douyin brand hot search list data
    async def fetch_hot_brand_search_category(self):
        endpoint = f"/api/v1/douyin/app/v1/fetch_brand_hot_search_list"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 获取抖音品牌热榜具体分类数据 | Get Douyin brand hot search list detail data
    async def fetch_hot_brand_search(self, category_id: int):
        endpoint = f"/api/v1/douyin/app/v1/fetch_brand_hot_search_list_detail?category_id={category_id}"
        data = await self.client.fetch_get_json(f"{endpoint}?category_id={category_id}")
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer jZVuQT5gm2gDj3IB0XKPySMV9B4EmLfyqo5okGfltWp7/VAgQt8unAaMEA=="})

        douyin_app_v1 = DouyinAppV1(client)

        # # 获取单个作品数据 | Get single video data
        # data = await douyin_app_v1.fetch_one_video(aweme_id="7345492945006595379")
        # print(f"fetch_one_video: {data}")
        #
        # # 获取指定用户的信息 | Get information of specified user
        # data = await douyin_app_v1.handler_user_profile(
        #     sec_user_id="MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y")
        # print(f"handler_user_profile: {data}")
        #
        # # 获取用户主页作品数据 | Get user homepage video data
        # data = await douyin_app_v1.fetch_user_post_videos(
        #     sec_user_id="MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE", max_cursor=0, count=10)
        # print(f"fetch_user_post_videos: {data}")
        #
        # # 获取用户喜欢作品数据 | Get user like video data
        # data = await douyin_app_v1.fetch_user_like_videos(
        #     sec_user_id="MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y", max_cursor=0, counts=10)
        # print(f"fetch_user_like_videos: {data}")
        #
        # # 获取单个视频评论数据 | Get single video comments data
        # data = await douyin_app_v1.fetch_video_comments(aweme_id="7345492945006595379", cursor=0, count=10)
        # print(f"fetch_video_comments: {data}")
        #
        # # 获取指定视频的评论回复数据 | Get comment replies data of specified video
        # data = await douyin_app_v1.fetch_video_comments_reply(item_id="7354666303006723354",
        #                                                       comment_id="7354669356632638218",
        #                                                       cursor=0,
        #                                                       count=10)
        # print(f"fetch_video_comments_reply: {data}")
        #
        # # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
        # data = await douyin_app_v1.fetch_general_search_result(keyword="中华娘", offset=0, count=20, sort_type=0,
        #                                                        publish_time=0)
        # print(f"fetch_general_search_result: {data}")
        #
        # # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
        # data = await douyin_app_v1.fetch_video_search_result(keyword="中华娘", offset=0, count=20, sort_type=0,
        #                                                      publish_time=0)
        # print(f"fetch_video_search_result: {data}")
        #
        # # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
        # data = await douyin_app_v1.fetch_user_search_result(keyword="中华娘", offset=0, count=20)
        # print(f"fetch_user_search_result: {data}")
        #
        # # 获取指定关键词的音乐搜索结果 | Get music search results of specified keywords
        # data = await douyin_app_v1.fetch_music_search_result(keyword="中华娘", offset=0, count=20)
        # print(f"fetch_music_search_result: {data}")
        #
        # # 获取指定关键词的话题搜索结果 | Get hashtag search results of specified keywords
        # data = await douyin_app_v1.fetch_hashtag_search_result(keyword="中华娘", offset=0, count=20)
        # print(f"fetch_hashtag_search_result: {data}")
        #
        # # 获取指定音乐的详情数据 | Get details of specified music
        # data = await douyin_app_v1.fetch_music_detail(music_id="7136850194742315016")
        # print(f"fetch_music_detail: {data}")
        #
        # # 抖音音乐视频列表结果 | Get video list of specified music
        # data = await douyin_app_v1.fetch_music_video_list(music_id="7136850194742315016", cursor=0, count=10)
        # print(f"fetch_music_video_list: {data}")
        #
        # # 抖音话题详情数据 | Get details of specified hashtag
        # data = await douyin_app_v1.fetch_hashtag_detail(ch_id=1575791821492238)
        # print(f"fetch_hashtag_detail: {data}")
        #
        # # 获取指定话题的作品数据 | Get video list of specified hashtag
        # data = await douyin_app_v1.fetch_hashtag_post_list(ch_id=1575791821492238, cursor=0, count=10, sort_type=0)
        # print(f"fetch_hashtag_post_list: {data}")
        #
        # # 抖音热搜榜数据 | Get Douyin hot search list data
        # data = await douyin_app_v1.fetch_hot_search_list()
        # print(f"fetch_hot_search_list: {data}")
        #
        # # 抖音直播热搜榜数据 | Get Douyin live hot search list data
        # data = await douyin_app_v1.fetch_hot_live_search()
        # print(f"fetch_hot_live_search: {data}")
        #
        # # 抖音音乐热榜数据 | Get Douyin music hot search list data
        # data = await douyin_app_v1.fetch_hot_music_search()
        # print(f"fetch_hot_music_search: {data}")
        #
        # # 抖音品牌热榜分类数据 | Get Douyin brand hot search list data
        # data = await douyin_app_v1.fetch_hot_brand_search_category()
        # print(f"fetch_hot_brand_search_category: {data}")
        #
        # # 抖音品牌热榜具体分类数据 | Get Douyin brand hot search list detail data
        # data = await douyin_app_v1.fetch_hot_brand_search(category_id=10)
        # print(f"fetch_hot_brand_search: {data}")

    asyncio.run(main())
