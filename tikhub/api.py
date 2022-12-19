#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author: https://github.com/orgs/TikHubIO
# @Time: 2022/12/15
# @Update: 2022/12/19
# @Version: 1.0.0
# @Description: Douyin/TikTok async data scraper, base on TikHub API.


import aiohttp
import platform
import asyncio

from tenacity import *


class API(object):

    """__________________________________________⬇️initialization(初始化)⬇__________________________________________"""

    # 初始化/initialization
    def __init__(self,
                 domain: str = 'https://api.tikhub.io',
                 username: str = None,
                 password: str = None,
                 proxy: str = None):
        # TikHub API domain/TikHub API域名
        self.domain = domain
        # HTTP代理/HTTP proxy
        self.proxies = proxy
        # 用户名/username
        self.username = username
        # 密码/password
        self.password = password
        # 请求头/request header
        self.headers = {}
        # 针对Windows系统的异步事件规则/Asynchronous event rules for Windows systems
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    """__________________________________________⬇️认证(authenticate)⬇__________________________________________"""

    # 校验token是否有效/Check if the token is valid
    async def check_token(self, status_code: int):
        if status_code == 401:
            await self.authenticate()
            raise Exception('authenticate failed, please check your username and password!')

    # 构造TikHub请求头/Construct TikHub request header
    async def authenticate(self) -> dict:
        # 利用用户名和密码获取token构造请求头/Use username and password to get token to construct request header
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.domain}/token',
                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                    data={'username': self.username, 'password': self.password},
                    proxy=self.proxies, timeout=10) as response:
                # 401错误，认证失败/401 error, authentication failed
                if response.status == 401:
                    raise Exception('authenticate failed, please check your username and password!')
                response = await response.json()
                token = response.get('access_token')
                token_type = response.get('token_type')
                header = {
                    'Authorization': f'{token_type} {token}',
                }
                self.headers.update(header)
                print(f'Construct TikHub request headers completed: \n{self.headers}')
                return self.headers

    # 获取TikHub用户信息/Get TikHub user information
    async def get_user_info(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{self.domain}/users/me/',
                    headers=self.headers,
                    proxy=self.proxies, timeout=10) as response:
                await self.check_token(response.status)
                response = await response.json()
                print(f'Get TikHub user information completed: \n{response}')
                return response

    """__________________________________________⬇️TikTok API⬇__________________________________________"""

    # 获取单个视频数据/Get single video data
    @retry(wait=wait_fixed(1), stop=stop_after_attempt(3))
    async def get_tiktok_video_data(self, tiktok_video_url: str) -> list:
        api_url = f'{self.domain}/tiktok_video_data/?tiktok_video_url={tiktok_video_url}'
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    api_url,
                    headers=self.headers,
                    proxy=self.proxies, timeout=10) as response:
                await self.check_token(response.status)
                response = await response.json()
                aweme_list = response.get('aweme_list')
                print(f'{tiktok_video_url} --- {response.get("status")}')
                return aweme_list

    # 获取用户主页的所有视频数据/Get all video data on the user's homepage
    @retry(wait=wait_fixed(1), stop=stop_after_attempt(3))
    async def get_tiktok_profile_videos(self, tiktok_video_url: str, count: int) -> list:
        aweme_list = []
        api_url = f'{self.domain}/tiktok_profile_videos/?tiktok_video_url={tiktok_video_url}&cursor=0&count=20'
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    api_url,
                    headers=self.headers,
                    proxy=self.proxies, timeout=10) as response:
                await self.check_token(response.status)
                response = await response.json()
                # 获取视频列表/Get video list
                aweme_list.extend(response.get('aweme_list'))
                # 判断是否超出count/if more than count
                if len(aweme_list) >= count:
                    return aweme_list[:count]
                # 获取下一页视频列表/Get the next page video list
                while response.get('has_more'):
                    api_url = response.get('next_url')
                    async with session.get(
                            api_url,
                            headers=self.headers,
                            proxy=self.proxies, timeout=10) as response:
                        await self.check_token(response.status)
                        response = await response.json()
                        aweme_list.extend(response.get('aweme_list'))
                        # 判断是否超出count/if more than count
                        if len(aweme_list) >= count:
                            return aweme_list[:count]
                print(f'{tiktok_video_url} --- {response.get("status")}')
        return aweme_list

    # 获取用户主页的所有点赞视频数据/Get all liked video data on the user's homepage
    @retry(wait=wait_fixed(1), stop=stop_after_attempt(3))
    async def get_tiktok_profile_liked_videos(self, tiktok_video_url: str, count: int) -> list:
        aweme_list = []
        api_url = f'{self.domain}/tiktok_profile_liked_videos/?tiktok_video_url={tiktok_video_url}&cursor=0&count=20'
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    api_url,
                    headers=self.headers,
                    proxy=self.proxies, timeout=10) as response:
                await self.check_token(response.status)
                response = await response.json()
                # 获取视频列表/Get video list
                aweme_list.extend(response.get('aweme_list'))
                # 判断是否超出count/if more than count
                if len(aweme_list) >= count:
                    return aweme_list[:count]
                # 获取下一页视频列表/Get the next page video list
                while response.get('has_more'):
                    api_url = response.get('next_url')
                    async with session.get(
                            api_url,
                            headers=self.headers,
                            proxy=self.proxies, timeout=10) as response:
                        await self.check_token(response.status)
                        response = await response.json()
                        aweme_list.extend(response.get('aweme_list'))
                        # 判断是否超出count/if more than count
                        if len(aweme_list) >= count:
                            return aweme_list[:count]
                print(f'{tiktok_video_url} --- {response.get("status")}')
        return aweme_list

    # 获取TikTok视频的所有评论数据/Get all comment data of TikTok video
    @retry(wait=wait_fixed(1), stop=stop_after_attempt(3))
    async def get_tiktok_video_comments(self, tiktok_video_url: str, count: int) -> list:
        comments_list = []
        api_url = f'{self.domain}/tiktok_video_comments/?tiktok_video_url={tiktok_video_url}&cursor=0&count=20'
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    api_url,
                    headers=self.headers,
                    proxy=self.proxies, timeout=10) as response:
                await self.check_token(response.status)
                response = await response.json()
                # 获取视频列表/Get video list
                comments_list.extend(response.get('comments_list'))
                # 判断是否超出count/if more than count
                if len(comments_list) >= count:
                    return comments_list[:count]
                # 获取下一页视频列表/Get the next page video list
                while response.get('has_more'):
                    api_url = response.get('next_url')
                    async with session.get(
                            api_url,
                            headers=self.headers,
                            proxy=self.proxies, timeout=10) as response:
                        await self.check_token(response.status)
                        response = await response.json()
                        comments_list.extend(response.get('comments_list'))
                        # 判断是否超出count/if more than count
                        if len(comments_list) >= count:
                            return comments_list[:count]
                print(f'{tiktok_video_url} --- {response.get("status")}')
        return comments_list

    # 获取音乐页面上的所有(理论上能抓取到的)视频数据/Get all (theoretically) video data on the music page
    @retry(wait=wait_fixed(1), stop=stop_after_attempt(3))
    async def get_tiktok_music_videos(self, tiktok_music_url: str, count: int) -> list:
        aweme_list = []
        api_url = f'{self.domain}/tiktok_music_videos/?tiktok_music_video_url={tiktok_music_url}&cursor=0&count=20'
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    api_url,
                    headers=self.headers,
                    proxy=self.proxies, timeout=10) as response:
                await self.check_token(response.status)
                response = await response.json()
                # 获取视频列表/Get video list
                aweme_list.extend(response.get('aweme_list'))
                # 判断是否超出count/if more than count
                if len(aweme_list) >= count:
                    return aweme_list[:count]
                # 获取下一页视频列表/Get the next page video list
                while response.get('has_more'):
                    api_url = response.get('next_url')
                    async with session.get(
                            api_url,
                            headers=self.headers,
                            proxy=self.proxies, timeout=10) as response:
                        await self.check_token(response.status)
                        response = await response.json()
                        aweme_list.extend(response.get('aweme_list'))
                        # 判断是否超出count/if more than count
                        if len(aweme_list) >= count:
                            return aweme_list[:count]
                print(f'{tiktok_music_url} --- {response.get("status")}')
        return aweme_list

    """__________________________________________⬇️Douyin API⬇__________________________________________"""

    # 获取抖音用户单个视频数据/Get a single video data of Douyin user
    @retry(wait=wait_fixed(1), stop=stop_after_attempt(3))
    async def get_douyin_video_data(self, douyin_video_url: str) -> list:
        api_url = f'{self.domain}/douyin_video_data/?douyin_video_url={douyin_video_url}'
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    api_url,
                    headers=self.headers,
                    proxy=self.proxies, timeout=10) as response:
                await self.check_token(response.status)
                response = await response.json()
                print(f'{douyin_video_url} --- {response.get("status")}')
        return response.get('aweme_list')

    # 获取抖音用户主页的所有视频数据/Get all video data of Douyin user home page
    @retry(wait=wait_fixed(1), stop=stop_after_attempt(3))
    async def get_douyin_profile_videos(self, douyin_user_url: str, count: int) -> list:
        aweme_list = []
        api_url = f'{self.domain}/douyin_profile_videos/?douyin_profile_url={douyin_user_url}&cursor=0&count=20'
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    api_url,
                    headers=self.headers,
                    proxy=self.proxies, timeout=10) as response:
                await self.check_token(response.status)
                response = await response.json()
                # 获取视频列表/Get video list
                aweme_list.extend(response.get('aweme_list'))
                # 判断是否超出count/if more than count
                if len(aweme_list) >= count:
                    return aweme_list[:count]
                # 获取下一页视频列表/Get the next page video list
                while response.get('has_more'):
                    api_url = response.get('next_url')
                    async with session.get(
                            api_url,
                            headers=self.headers,
                            proxy=self.proxies, timeout=10) as response:
                        await self.check_token(response.status)
                        response = await response.json()
                        aweme_list.extend(response.get('aweme_list'))
                        # 判断是否超出count/if more than count
                        if len(aweme_list) >= count:
                            return aweme_list[:count]
                print(f'{douyin_user_url} --- {response.get("status")}')
        return aweme_list

    # 获取抖音用户主页的所有点赞视频数据/Get all liked video data of Douyin user home page
    @retry(wait=wait_fixed(1), stop=stop_after_attempt(3))
    async def get_douyin_profile_liked_videos(self, douyin_user_url: str, count: int) -> list:
        aweme_list = []
        api_url = f'{self.domain}/douyin_profile_liked_videos/?douyin_profile_url={douyin_user_url}&cursor=0&count=20'
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    api_url,
                    headers=self.headers,
                    proxy=self.proxies, timeout=10) as response:
                await self.check_token(response.status)
                response = await response.json()
                # 获取视频列表/Get video list
                aweme_list.extend(response.get('aweme_list'))
                # 判断是否超出count/if more than count
                if len(aweme_list) >= count:
                    return aweme_list[:count]
                # 获取下一页视频列表/Get the next page video list
                while response.get('has_more'):
                    api_url = response.get('next_url')
                    async with session.get(
                            api_url,
                            headers=self.headers,
                            proxy=self.proxies, timeout=10) as response:
                        await self.check_token(response.status)
                        response = await response.json()
                        aweme_list.extend(response.get('aweme_list'))
                        # 判断是否超出count/if more than count
                        if len(aweme_list) >= count:
                            return aweme_list[:count]
                print(f'{douyin_user_url} --- {response.get("status")}')
        return aweme_list


"""__________________________________________⬇️测试方法(test methods)⬇__________________________________________"""


async def async_test() -> None:
    # 异步测试/Async test

    tiktok_url = 'https://www.tiktok.com/@evil0ctal/video/7156033831819037994'

    tiktok_music_url = 'https://www.tiktok.com/music/original-sound-7128362040359488261'

    douyin_url = 'https://www.douyin.com/video/7153585499477757192'

    douyin_user_url = 'https://www.douyin.com/user/MS4wLjABAAAA-Hu1YKTuhE3QkCHD5yU26k--RUZiaoMRtpfmeid-Z_o'

    print("Test start...\n")
    start_time = time.time()

    # 获取TikHub请求头/Get TikHub request header
    print("Running test : API.authenticate()")
    await api.authenticate()

    # 获取TikHub用户信息/Get TikHub user information
    print("Running test : API.get_user_info()")
    await api.get_user_info()

    print("\nRunning ALL TikTok methods test...\n")

    # 获取单个视频数据/Get single video data
    print("Running test : API.get_tiktok_video_data()")
    await api.get_tiktok_video_data(tiktok_url)

    # 获取获取用户主页的所有视频数据/Get all video data on the user's homepage
    print("Running test : API.get_tiktok_profile_videos()")
    aweme_list = await api.get_tiktok_profile_videos(tiktok_url, 20)
    print(f'Get {len(aweme_list)} videos from profile')

    # 获取用户主页的所有点赞视频数据/Get all liked video data on the user's homepage
    print("Running test : API.get_tiktok_profile_liked_videos()")
    aweme_list = await api.get_tiktok_profile_liked_videos(tiktok_url, 20)
    print(f'Get {len(aweme_list)} liked videos from profile')

    # 获取TikTok视频的所有评论数据/Get all comment data of TikTok video
    print("Running test : API.get_tiktok_video_comments()")
    comments_list = await api.get_tiktok_video_comments(tiktok_url, 20)
    print(f'Get {len(comments_list)} comments from video')

    # 获取音乐页面上的所有(理论上能抓取到的)视频数据/Get all (theoretically) video data on the music page
    print("Running test : API.get_tiktok_music_videos()")
    aweme_list = await api.get_tiktok_music_videos(tiktok_music_url, 20)
    print(f'Get {len(aweme_list)} videos from music')

    print("\nRunning ALL Douyin methods test...\n")

    # 获取单个视频数据/Get single video data
    print("Running test : API.get_douyin_video_data()")
    await api.get_douyin_video_data(douyin_url)

    # 获取获取用户主页的所有视频数据/Get all video data on the user's homepage
    print("Running test : API.get_douyin_profile_videos()")
    aweme_list = await api.get_douyin_profile_videos(douyin_user_url, 20)
    print(f'Get {len(aweme_list)} videos from profile')

    # 获取用户主页的所有点赞视频数据/Get all liked video data on the user's homepage
    print("Running test : API.get_douyin_profile_liked_videos()")
    aweme_list = await api.get_douyin_profile_liked_videos(douyin_user_url, 20)

    # 总耗时/Total time
    total_time = round(time.time() - start_time, 2)
    print("\nTest completed, total time: {}s".format(total_time))


if __name__ == '__main__':
    api = API(
        domain='http://127.0.0.1',
        username='test',
        password='test',
        proxy=None,
    )
    asyncio.run(async_test())
