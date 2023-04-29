import asyncio
import re
from typing import Union

from tikhub.Auth import Auth


class DouyinAPI(Auth):

    def __init__(self, token: str):
        super().__init__(token)
        self.scraper_utils = None

    """_________________________________⬇️Douyin杂项(Douyin Utils)⬇️_________________________________"""

    # 获取抖音视频ID/Get Douyin video ID
    async def get_douyin_video_id(self, original_url: str) -> Union[str, None]:
        try:
            video_url = await self.scraper_utils.convert_share_urls(original_url)
            # 链接类型:
            # 视频页 https://www.douyin.com/video/7086770907674348841
            if '/video/' in video_url:
                key = re.findall('/video/(\d+)?', video_url)[0]
                print('获取到的抖音视频ID为: {}'.format(key))
                return key
            # 发现页 https://www.douyin.com/discover?modal_id=7086770907674348841
            elif 'discover?' in video_url:
                key = re.findall('modal_id=(\d+)', video_url)[0]
                print('获取到的抖音视频ID为: {}'.format(key))
                return key
            # 直播页
            elif 'live.douyin' in video_url:
                # https://live.douyin.com/1000000000000000000
                video_url = video_url.split('?')[0] if '?' in video_url else video_url
                key = video_url.replace('https://live.douyin.com/', '')
                print('获取到的抖音直播ID为: {}'.format(key))
                return key
            # note
            elif 'note' in video_url:
                # https://www.douyin.com/note/7086770907674348841
                key = re.findall('/note/(\d+)?', video_url)[0]
                print('获取到的抖音笔记ID为: {}'.format(key))
                return key
        except Exception as e:
            print('获取抖音视频ID出错了:{}'.format(e))
            raise {'error': '获取抖音视频ID出错了'}

    # 获取抖音音乐ID/Get Douyin music ID
    async def get_douyin_music_id(self, original_url) -> Union[str, None]:
        try:
            # 转换链接
            if '/music/' not in original_url:
                original_url = await self.scraper_utils.convert_share_urls(original_url)
            # 获取音乐id
            music_id = re.findall(r'/music/(\d+)', original_url)[0]
            print('抖音music_id:{}'.format(music_id))
            return music_id
        except Exception as e:
            # 报错后判断为长链接，直接截取视频id
            print('获取抖音music_id失败，原因：{}'.format(str(e)))
            return None

    # 获取抖音用户sec_uid/Get Douyin user sec_uid
    async def get_douyin_user_sec_uid(self, original_url: str) -> Union[str, None]:
        try:
            # 获取作者主页链接
            if '/user/' not in original_url:
                # 从请求头中获取作者主页链接
                original_url = await self.scraper_utils.convert_share_urls(original_url)
                # print('获取到的作者主页链接:{}'.format(original_url))
            # 获取用户sec_uid
            if '?' in original_url:
                original_url = original_url.split('?')[0]
            for one in re.finditer(r'user\/([\d\D]*)', str(original_url)):
                sec_uid = one.group(1)
                # print('获取到的用户sec_uid:{}'.format(sec_uid))
                return sec_uid
        except Exception as e:
            print('获取douyin用户sec_uid出错了:{}'.format(e))
            return None

    """_________________________________⬇️Douyin爬虫(Douyin Scraper)⬇️_________________________________"""

    async def get_douyin_video_data(self, douyin_video_url: str = None, video_id: int = None,
                                    language: str = 'zh') -> dict:
        endpoint = "/douyin/video_data/"
        video_id = video_id or await self.get_douyin_video_id(douyin_video_url)
        params = f'video_id={video_id}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_user_data(self, douyin_user_url: str = None, sec_user_id: str = None,
                                   language: str = 'zh') -> dict:
        endpoint = "/douyin/user_data/"
        sec_user_id = sec_user_id or await self.get_douyin_user_sec_uid(douyin_user_url)
        params = f'sec_user_id={sec_user_id}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_user_profile_videos_data(self, douyin_user_url: str = None, sec_user_id: str = None,
                                                  cursor: int = 0,
                                                  count: int = 20, language: str = 'zh') -> dict:
        endpoint = "/douyin/user_profile_videos_data/"
        sec_user_id = sec_user_id or await self.get_douyin_user_sec_uid(douyin_user_url)
        params = f'sec_user_id={sec_user_id}&cursor={cursor}&count={count}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_user_profile_liked_videos_data(self, douyin_user_url: str = None, sec_user_id: str = None,
                                                  cursor: int = 0,
                                                  count: int = 20, language: str = 'zh') -> dict:
        endpoint = "/douyin/user_profile_liked_videos_data/"
        sec_user_id = sec_user_id or await self.get_douyin_user_sec_uid(douyin_user_url)
        params = f'sec_user_id={sec_user_id}&cursor={cursor}&count={count}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_video_comments(self, douyin_video_url: str = None, video_id: int = None, cursor: int = 0,
                                        count: int = 20, language: str = 'zh') -> dict:
        endpoint = "/douyin/video_comments/"
        video_id = video_id or await self.get_douyin_video_id(douyin_video_url)
        params = f'video_id={video_id}&cursor={cursor}&count={count}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_music_data(self, douyin_music_url: str = None, music_id: int = None,
                                    language: str = 'zh') -> dict:
        endpoint = "/douyin/music_data/"
        music_id = music_id or await self.get_douyin_music_id(douyin_music_url)
        params = f'music_id={music_id}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_music_videos_data(self, douyin_music_url: str = None, music_id: int = None, cursor: int = 0,
                                           count: int = 20, language: str = 'zh') -> dict:
        endpoint = "/douyin/music_videos_data/"
        music_id = music_id or await self.get_douyin_music_id(douyin_music_url)
        params = f'music_id={music_id}&cursor={cursor}&count={count}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_hot_search_data(self, language: str = 'zh') -> dict:
        endpoint = "/douyin/hot_search_data/"
        params = f'language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_hot_live_data(self, language: str = 'zh') -> dict:
        endpoint = "/douyin/hot_live_data/"
        params = f'language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_hot_music_data(self, cursor: int = 0, count: int = 50, language: str = 'zh') -> dict:
        endpoint = "/douyin/hot_music_data/"
        params = f'cursor={cursor}&count={count}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_search_data_general(self, keyword: str, cursor: int = 0, count: int = 20, language: str = 'zh',
                                             sort_type: str = 0, publish_time: str = 0, filter_duration: str = None,
                                             content_type: str = 0) -> dict:
        endpoint = "/douyin/search_data_general/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&language={language}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}&content_type={content_type}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_search_data_videos(self, keyword: str, cursor: int = 0, count: int = 20, language: str = 'zh',
                                            sort_type: str = 0, publish_time: str = 0, filter_duration: str = None,
                                            content_type: str = 0) -> dict:
        endpoint = "/douyin/search_data_videos/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&language={language}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}&content_type={content_type}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_search_data_users(self, keyword: str, cursor: int = 0, count: int = 20, language: str = 'zh',
                                           sort_type: str = 0, publish_time: str = 0, filter_duration: str = None,
                                           content_type: str = 0) -> dict:
        endpoint = "/douyin/search_data_users/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&language={language}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}&content_type={content_type}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_search_data_products(self, keyword: str, cursor: int = 0, count: int = 20, language: str = 'zh',
                                              sort_type: str = 0, publish_time: str = 0, filter_duration: str = None,
                                              content_type: str = 0) -> dict:
        endpoint = "/douyin/search_data_products/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&language={language}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}&content_type={content_type}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_search_data_music(self, keyword: str, cursor: int = 0, count: int = 20, language: str = 'zh',
                                           sort_type: str = 0, publish_time: str = 0, filter_duration: str = None,
                                           content_type: str = 0) -> dict:
        endpoint = "/douyin/search_data_music/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&language={language}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}&content_type={content_type}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_search_data_challenge(self, keyword: str, cursor: int = 0, count: int = 20, language: str = 'zh',
                                               sort_type: str = 0, publish_time: str = 0,
                                               filter_duration: str = None,
                                               content_type: str = 0) -> dict:
        endpoint = "/douyin/search_data_challenge/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&language={language}&sort_type={sort_type}&publish_time={publish_time}&filter_duration={filter_duration}&content_type={content_type}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    async def get_douyin_live_room_data(self, url: str) -> dict:
        endpoint = "/douyin/live_room_data/"
        params = f'url={url}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')


if __name__ == '__main__':
    # token = input('Please enter your TikTok token: ')

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTM3NzM2NzEsInVzZXJuYW1lIjoiZXZpbDBjdGFsMTk4NUBnbWFpbC5jb20iLCJlbWFpbCI6ImV2aWwwY3RhbDE5ODVAZ21haWwuY29tIiwiZXZpbDEiOiIkMmIkMTIkeVNFOTUzNHljcU4zeUNuYkVaUlBidTNDT2NVQ2dZbmdVSDBKTFh0WW55alFnSXdJRUhxckcifQ.xN6EHgE4J9nWE6qgouhXpF1N1YTj3iuzVpot66u6twY"

    douyin_api = DouyinAPI(token)

    aweme_id = 7199980221733375265

    music_id = 7138334551687825409

    challenge_id = 7551

    sec_user_id = 'MS4wLjABAAAAaNJuvXC83kL5nhaZHubKdjsRJQovgz58wXzlLnJUsslG-Kb24TM1QJlf_2HMaUJk'

    web_rid = 832975436921

    live_url = 'https://live.douyin.com/52328544266'

    r = None

    # print("获取抖音单一视频数据/Get Douyin single video data")
    # r = asyncio.run(douyin_api.get_douyin_video_data(video_id=aweme_id))

    # print("获取抖音用户信息数据/Get Douyin user profile data")
    # r = asyncio.run(douyin_api.get_douyin_user_data(sec_user_id=sec_user_id))

    # print("获取抖音用户主页视频数据/Get Douyin user profile videos data")
    # r = asyncio.run(douyin_api.get_douyin_user_profile_videos_data(sec_user_id=sec_user_id))

    # print("获取抖音主页点赞视频数据/Get Douyin home page liked videos data")
    # r = asyncio.run(douyin_api.get_douyin_user_profile_liked_videos_data(sec_user_id=sec_user_id))

    # print("获取抖音视频评论数据/Get Douyin video comments data")
    # r = asyncio.run(douyin_api.get_douyin_video_comments(video_id=aweme_id))

    # print("获取抖音音乐数据/Get Douyin music data")
    # r = asyncio.run(douyin_api.get_douyin_music_data(music_id=music_id))

    # print("获取抖音音乐视频视频合集数据/Get Douyin music videos data")
    # r = asyncio.run(douyin_api.get_douyin_music_videos_data(music_id=music_id))

    # print("抖音搜索热榜数据/Get Douyin search hot data")
    # r = asyncio.run(douyin_api.get_douyin_hot_search_data())

    # print("获取抖音直播热榜数据/Get Douyin live hot data")
    # r = asyncio.run(douyin_api.get_douyin_hot_live_data())

    # print("获取抖音音乐热榜数据/Get Douyin music hot data")
    # r = asyncio.run(douyin_api.get_douyin_hot_music_data())

    # print("获取抖音综合搜索数据/Get Douyin general search data")
    # r = asyncio.run(douyin_api.get_douyin_search_data_general('猫', 0, 10))

    # print("获取抖音视频搜索数据/Get Douyin video search data")
    # r = asyncio.run(douyin_api.get_douyin_search_data_videos('猫', 0, 10))

    # print("获取抖音用户搜索数据/Get Douyin user search data")
    # r = asyncio.run(douyin_api.get_douyin_search_data_users('猫', 0, 10))

    # print("获取抖音商品搜索数据/Get Douyin product search data")
    # r = asyncio.run(douyin_api.get_douyin_search_data_products('猫', 0, 10))

    # print("获取抖音音乐搜索数据/Get Douyin music search data")
    # r = asyncio.run(douyin_api.get_douyin_search_data_music('猫', 0, 10))

    # print("获取抖音挑战搜索数据/Get Douyin challenge search data")
    # r = asyncio.run(douyin_api.get_douyin_search_data_challenge('猫', 0, 10))

    # print("获取抖音直播间数据/Get Douyin live room data")
    # r = asyncio.run(douyin_api.get_douyin_live_room_data(live_url))

    print(r)
