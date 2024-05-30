# 导入API SDK Client类
import json

from tikhub.http_client.api_client import APIClient


class TikTokAppV3:

    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取单个作品数据 | Get single video data
    async def fetch_one_video(self, aweme_id: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_one_video"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}")
        return data

    # 获取指定用户的信息 | Get information of specified user
    async def handler_user_profile(self, sec_user_id: str):
        endpoint = "/api/v1/tiktok/app/v3/handler_user_profile"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}")
        return data

    # 获取用户主页作品数据 | Get user homepage video data
    async def fetch_user_post_videos(self, sec_user_id: str, max_cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_user_post_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&count={count}")
        return data

    # 获取用户喜欢作品数据 | Get user like video data
    async def fetch_user_like_videos(self, sec_user_id: str, max_cursor: int, counts: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_user_like_videos"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&max_cursor={max_cursor}&counts={counts}")
        return data

    # 获取单个视频评论数据 | Get single video comments data
    async def fetch_video_comments(self, aweme_id: str, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_video_comments"
        data = await self.client.fetch_get_json(f"{endpoint}?aweme_id={aweme_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定视频的评论回复数据 | Get comment replies data of specified video
    async def fetch_video_comments_reply(self, item_id: str, comment_id: str, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_video_comment_replies"
        data = await self.client.fetch_get_json(
            f"{endpoint}?item_id={item_id}&comment_id={comment_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
    async def fetch_general_search_result(self, keyword: str, offset: int, count: int, sort_type: int,
                                          publish_time: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_general_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}")
        return data

    # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
    async def fetch_video_search_result(self, keyword: str, offset: int, count: int, sort_type: int, publish_time: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_video_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&sort_type={sort_type}&publish_time={publish_time}")
        return data

    # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
    async def fetch_user_search_result(self, keyword: str, offset: int, count: int, user_search_follower_count: str,
                                       user_search_profile_type: str, user_search_other_pref: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_user_search_result"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&offset={offset}&count={count}&user_search_follower_count={user_search_follower_count}&user_search_profile_type={user_search_profile_type}&user_search_other_pref={user_search_other_pref}")
        return data

    # 获取指定关键词的音乐搜索结果 | Get music search results of specified keywords
    async def fetch_music_search_result(self, keyword: str, offset: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_music_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定关键词的话题搜索结果 | Get hashtag search results of specified keywords
    async def fetch_hashtag_search_result(self, keyword: str, offset: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_hashtag_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定关键词的直播搜索结果 | Get live search results of specified keywords
    async def fetch_live_search_result(self, keyword: str, offset: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_live_search_result"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取指定音乐的详情数据 | Get details of specified music
    async def fetch_music_detail(self, music_id: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_music_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}")
        return data

    # 抖音音乐视频列表结果 | Get video list of specified music
    async def fetch_music_video_list(self, music_id: int, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_music_video_list"
        data = await self.client.fetch_get_json(f"{endpoint}?music_id={music_id}&cursor={cursor}&count={count}")
        return data

    # 抖音话题详情数据 | Get details of specified hashtag
    async def fetch_hashtag_detail(self, ch_id: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_hashtag_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?ch_id={ch_id}")
        return data

    # 获取指定话题的作品数据 | Get video list of specified hashtag
    async def fetch_hashtag_video_list(self, ch_id: int, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_hashtag_video_list"
        data = await self.client.fetch_get_json(f"{endpoint}?ch_id={ch_id}&cursor={cursor}&count={count}")
        return data

    # 获取指定用户的粉丝列表数据 | Get follower list of specified user
    async def fetch_user_follower_list(self, sec_user_id: str, count: int, max_time: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_user_follower_list"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&count={count}&max_time={max_time}")
        return data

    # 获取指定用户的关注列表数据 | Get following list of specified user
    async def fetch_user_following_list(self, sec_user_id: str, count: int, max_time: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_user_following_list"
        data = await self.client.fetch_get_json(
            f"{endpoint}?sec_user_id={sec_user_id}&count={count}&max_time={max_time}")
        return data

    # TikTok直播间排行榜 | Get live room ranking list
    async def fetch_live_room_rank_list(self, room_id: str, anchor_id: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_live_ranking_list"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}&anchor_id={anchor_id}")
        return data

    # 检测直播间是否在线 | Check if live room is online
    async def fetch_live_room_check(self, room_id: str):
        endpoint = "/api/v1/tiktok/app/v3/check_live_room_online"
        data = await self.client.fetch_get_json(f"{endpoint}?room_id={room_id}")
        return data

    # 获取分享短链接 | Get share short link
    async def fetch_share_short_link(self, url: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_share_short_link"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 获取分享二维码 | Get share QR code
    async def fetch_share_qr_code(self, url: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_share_qr_code"
        data = await self.client.fetch_get_json(f"{endpoint}?url={url}")
        return data

    # 获取地点搜索结果 | Get location search results
    async def fetch_location_search(self, keyword: str, offset: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_location_search"
        data = await self.client.fetch_get_json(f"{endpoint}?keyword={keyword}&offset={offset}&count={count}")
        return data

    # 获取商品搜索结果 | Get product search results
    async def fetch_product_search(self, keyword: str, cursor: int, count: int, sort_type: int,
                                   customer_review_four_star: bool, have_discount: bool, min_price: str,
                                   max_price: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_product_search"
        data = await self.client.fetch_get_json(
            f"{endpoint}?keyword={keyword}&cursor={cursor}&count={count}&sort_type={sort_type}&customer_review_four_star={customer_review_four_star}&have_discount={have_discount}&min_price={min_price}&max_price={max_price}")
        return data

    # 获取商品详情数据 | Get product detail data
    async def fetch_product_detail(self, product_id: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_product_detail"
        data = await self.client.fetch_get_json(f"{endpoint}?product_id={product_id}")
        return data

    # 获取商品评价数据 | Get product review data
    async def fetch_product_review(self, product_id: str, cursor: int, size: int, filter_id: int, sort_type: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_product_review"
        data = await self.client.fetch_get_json(
            f"{endpoint}?product_id={product_id}&cursor={cursor}&size={size}&filter_id={filter_id}&sort_type={sort_type}")
        return data

    # 获取商家主页Page列表数据 | Get shop home page list data
    async def fetch_shop_home_page_list(self, sec_user_id: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_shop_home_page_list"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}")
        return data

    # 获取商家主页数据 | Get shop home page data
    async def fetch_shop_home(self, page_id: str, seller_id: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_shop_home"
        data = await self.client.fetch_get_json(f"{endpoint}?page_id={page_id}&seller_id={seller_id}")
        return data

    # 获取商家商品推荐数据 | Get shop product recommend data
    async def fetch_shop_product_recommend(self, seller_id: str, scroll_param: str, page_size: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_shop_product_recommend"
        data = await self.client.fetch_get_json(
            f"{endpoint}?seller_id={seller_id}&scroll_param={scroll_param}&page_size={page_size}")
        return data

    # 获取商家商品列表数据 | Get shop product list data
    async def fetch_shop_product_list(self, seller_id: str, scroll_params: str, page_size: int, sort_field: int,
                                      sort_order: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_shop_product_list"
        data = await self.client.fetch_get_json(
            f"{endpoint}?seller_id={seller_id}&scroll_params={scroll_params}&page_size={page_size}&sort_field={sort_field}&sort_order={sort_order}")
        return data

    # 获取商家信息数据 | Get shop information data
    async def fetch_shop_info(self, shop_id: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_shop_info"
        data = await self.client.fetch_get_json(f"{endpoint}?shop_id={shop_id}")
        return data

    # 获取商家产品分类数据 | Get shop product category data
    async def fetch_shop_product_category(self, seller_id: str):
        endpoint = "/api/v1/tiktok/app/v3/fetch_shop_product_category"
        data = await self.client.fetch_get_json(f"{endpoint}?seller_id={seller_id}")
        return data

    # 获取直播每日榜单数据 | Get live daily rank data
    async def fetch_live_daily_rank(self):
        endpoint = "/api/v1/tiktok/app/v3/fetch_live_daily_rank"
        data = await self.client.fetch_get_json(endpoint)
        return data

    # 获取用户音乐列表数据 | Get user music list data
    async def fetch_user_music_list(self, sec_user_id: str, cursor: int, count: int):
        endpoint = "/api/v1/tiktok/app/v3/fetch_user_music_list"
        data = await self.client.fetch_get_json(f"{endpoint}?sec_user_id={sec_user_id}&cursor={cursor}&count={count}")
        return data


if __name__ == "__main__":
    import asyncio


    async def main():
        client = APIClient(base_url="http://127.0.0.1:8000", client_headers={
            "Authorization": "Bearer l7sVQFh64V8ltC8fzEaNtWE60zVSopDLlpVX62fArT1FznsPds9+2RGoXw=="})

        tiktok_app_v3 = TikTokAppV3(client)

        # 获取单个作品数据 | Get single video data
        aweme_id = 6953663666666666666
        data = await tiktok_app_v3.fetch_one_video(aweme_id)
        print(data)

        # 获取指定用户的信息 | Get information of specified user
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        data = await tiktok_app_v3.handler_user_profile(sec_user_id)
        print(data)

        # 获取用户主页作品数据 | Get user homepage video data
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        max_cursor = 0
        count = 30
        data = await tiktok_app_v3.fetch_user_post_videos(sec_user_id, max_cursor, count)
        print(data)

        # 获取用户喜欢作品数据 | Get user like video data
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        max_cursor = 0
        counts = 30
        data = await tiktok_app_v3.fetch_user_like_videos(sec_user_id, max_cursor, counts)
        print(data)

        # 获取单个视频评论数据 | Get single video comments data
        aweme_id = "6953663666666666666"
        cursor = 0
        count = 30
        data = await tiktok_app_v3.fetch_video_comments(aweme_id, cursor, count)
        print(data)

        # 获取指定视频的评论回复数据 | Get comment replies data of specified video
        item_id = "6953663666666666666"
        comment_id = "6953663666666666666"
        cursor = 0
        count = 30
        data = await tiktok_app_v3.fetch_video_comments_reply(item_id, comment_id, cursor, count)
        print(data)

        # 获取指定关键词的综合搜索结果 | Get comprehensive search results of specified keywords
        keyword = "tiktok"
        offset = 0
        count = 30
        sort_type = 0
        publish_time = 0
        data = await tiktok_app_v3.fetch_general_search_result(keyword, offset, count, sort_type, publish_time)
        print(data)

        # 获取指定关键词的视频搜索结果 | Get video search results of specified keywords
        keyword = "tiktok"
        offset = 0
        count = 30
        sort_type = 0
        publish_time = 0
        data = await tiktok_app_v3.fetch_video_search_result(keyword, offset, count, sort_type, publish_time)
        print(data)

        # 获取指定关键词的用户搜索结果 | Get user search results of specified keywords
        keyword = "tiktok"
        offset = 0
        count = 30
        user_search_follower_count = ""
        user_search_profile_type = ""
        user_search_other_pref = ""
        data = await tiktok_app_v3.fetch_user_search_result(keyword, offset, count, user_search_follower_count,
                                                            user_search_profile_type, user_search_other_pref)
        print(data)

        # 获取指定关键词的音乐搜索结果 | Get music search results of specified keywords
        keyword = "tiktok"
        offset = 0
        count = 30
        data = await tiktok_app_v3.fetch_music_search_result(keyword, offset, count)
        print(data)

        # 获取指定关键词的话题搜索结果 | Get hashtag search results of specified keywords
        keyword = "tiktok"
        offset = 0
        count = 30
        data = await tiktok_app_v3.fetch_hashtag_search_result(keyword, offset, count)
        print(data)

        # 获取指定关键词的直播搜索结果 | Get live search results of specified keywords
        keyword = "tiktok"
        offset = 0
        count = 30
        data = await tiktok_app_v3.fetch_live_search_result(keyword, offset, count)
        print(data)

        # 获取指定音乐的详情数据 | Get details of specified music
        music_id = 6953663666666666666
        data = await tiktok_app_v3.fetch_music_detail(music_id)
        print(data)

        # 抖音音乐视频列表结果 | Get video list of specified music
        music_id = 6953663666666666666
        cursor = 0
        count = 30
        data = await tiktok_app_v3.fetch_music_video_list(music_id, cursor, count)
        print(data)

        # 抖音话题详情数据 | Get details of specified hashtag
        ch_id = 6953663666666666666
        data = await tiktok_app_v3.fetch_hashtag_detail(ch_id)
        print(data)

        # 获取指定话题的作品数据 | Get video list of specified hashtag
        ch_id = 6953663666666666666
        cursor = 0
        count = 30
        data = await tiktok_app_v3.fetch_hashtag_video_list(ch_id, cursor, count)
        print(data)

        # 获取指定用户的粉丝列表数据 | Get follower list of specified user
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        count = 30
        max_time = 0
        data = await tiktok_app_v3.fetch_user_follower_list(sec_user_id, count, max_time)
        print(data)

        # 获取指定用户的关注列表数据 | Get following list of specified user
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        count = 30
        max_time = 0
        data = await tiktok_app_v3.fetch_user_following_list(sec_user_id, count, max_time)
        print(data)

        # TikTok直播间排行榜 | Get live room ranking list
        room_id = "6953663666666666666"
        anchor_id = "6953663666666666666"
        data = await tiktok_app_v3.fetch_live_room_rank_list(room_id, anchor_id)
        print(data)

        # 检测直播间是否在线 | Check if live room is online
        room_id = "6953663666666666666"
        data = await tiktok_app_v3.fetch_live_room_check(room_id)
        print(data)

        # 获取分享短链接 | Get share short link
        url = "https://www.tiktok.com/@tiktok"
        data = await tiktok_app_v3.fetch_share_short_link(url)
        print(data)

        # 获取分享二维码 | Get share QR code
        url = "https://www.tiktok.com/@tiktok"
        data = await tiktok_app_v3.fetch_share_qr_code(url)
        print(data)

        # 获取地点搜索结果 | Get location search results
        keyword = "tiktok"
        offset = 0
        count = 30
        data = await tiktok_app_v3.fetch_location_search(keyword, offset, count)
        print(data)

        # 获取商品搜索结果 | Get product search results
        keyword = "tiktok"
        cursor = 0
        count = 30
        sort_type = 0
        customer_review_four_star = False
        have_discount = False
        min_price = "0"
        max_price = "1000"
        data = await tiktok_app_v3.fetch_product_search(keyword, cursor, count, sort_type, customer_review_four_star,
                                                        have_discount, min_price, max_price)
        print(data)

        # 获取商品详情数据 | Get product detail data
        product_id = "6953663666666666666"
        data = await tiktok_app_v3.fetch_product_detail(product_id)
        print(data)

        # 获取商品评价数据 | Get product review data
        product_id = "6953663666666666666"
        cursor = 0
        size = 30
        filter_id = 0
        sort_type = 0
        data = await tiktok_app_v3.fetch_product_review(product_id, cursor, size, filter_id, sort_type)
        print(data)

        # 获取商家主页Page列表数据 | Get shop home page list data
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        data = await tiktok_app_v3.fetch_shop_home_page_list(sec_user_id)
        print(data)

        # 获取商家主页数据 | Get shop home page data
        page_id = "6953663666666666666"
        seller_id = "6953663666666666666"
        data = await tiktok_app_v3.fetch_shop_home(page_id, seller_id)
        print(data)

        # 获取商家商品推荐数据 | Get shop product recommend data
        seller_id = "6953663666666666666"
        scroll_param = "6953663666666666666"
        page_size = 30
        data = await tiktok_app_v3.fetch_shop_product_recommend(seller_id, scroll_param, page_size)
        print(data)

        # 获取商家商品列表数据 | Get shop product list data
        seller_id = "6953663666666666666"
        scroll_params = "6953663666666666666"
        page_size = 30
        sort_field = 0
        sort_order = 0
        data = await tiktok_app_v3.fetch_shop_product_list(seller_id, scroll_params, page_size, sort_field, sort_order)
        print(data)

        # 获取商家信息数据 | Get shop information data
        shop_id = "6953663666666666666"
        data = await tiktok_app_v3.fetch_shop_info(shop_id)
        print(data)

        # 获取商家产品分类数据 | Get shop product category data
        seller_id = "6953663666666666666"
        data = await tiktok_app_v3.fetch_shop_product_category(seller_id)
        print(data)

        # 获取直播每日榜单数据 | Get live daily rank data
        data = await tiktok_app_v3.fetch_live_daily_rank()
        print(data)

        # 获取用户音乐列表数据 | Get user music list data
        sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
        cursor = 0
        count = 30
        data = await tiktok_app_v3.fetch_user_music_list(sec_user_id, cursor, count)
        print(data)


    asyncio.run(main())
