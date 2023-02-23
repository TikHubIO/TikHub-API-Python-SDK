#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author: https://github.com/orgs/TikHubIO
# @Time: 2022/12/15
# @Update: 2023/02/22
# @Version: 1.0.2
# @Description:
# TikHub REST API Python SDK


import platform
import asyncio
import urllib.parse

from tenacity import *
from tikhub.aiohttp_client import AiohttpClient


class API(object):

    """__________________________________________⬇️️initialization(初始化)⬇️️__________________________________________"""


    # 初始化/initialization
    def __init__(self, domain: str = 'https://api.tikhub.io',
                 email: str = None,
                 password: str = None,
                 proxy: str = None):
        # TikHub API domain/TikHub API域名
        self.domain = domain
        # HTTP代理/HTTP proxy
        self.proxies = proxy
        # 用户名/username
        self.email = email
        # 密码/password
        self.password = password
        # 请求头/request header
        self.headers = {}
        # 异步客户端/Asynchronous client
        self.client = AiohttpClient()
        # 针对Windows系统的异步事件规则/Asynchronous event rules for Windows systems
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


    """__________________________________________⬇️️认证(authenticate)⬇️️__________________________________________"""


    # 校验token是否有效/Check if the token is valid
    async def check_token(self, status_code: int):
        if status_code != 200:
            await self.user_login()


    # 利用用户名和密码获取token构造请求头
    # Use username and password to get token to construct request header
    async def user_login(self) -> dict:
        url = f'{self.domain}/user/login'
        params = "token_expiry_minutes=43200&keep_login=false"
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
        data={'username': self.email, 'password': self.password}
        status_code, text, json_data = await self.client.request("POST", url, params=params, headers=headers, data=urllib.parse.urlencode(data))
        # 更新请求头/Update request header
        self.headers = json_data.get('request_headers')
        return json_data


    # 获取TikHub用户信息
    # Get TikHub user information
    async def get_user_info(self) -> dict:
        url = f'{self.domain}/users/me/'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        return json_data


    # 获取TikHub促销礼包，用于兑换免费的抖音无水印视频下载次数
    # Get TikHub promotional packages for free Douyin no watermark video download
    async def claim_promotion(self, promotion_id: int) -> dict:
        url = f'{self.domain}/promotions/claim/'
        params = {'promotion_id': promotion_id}
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers, params=params)
        await self.check_token(status_code)
        return json_data


    # 每日签到
    # Daily check-in
    async def daily_check_in(self) -> dict:
        url = f'{self.domain}/users/daily_check_in/'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        return json_data


    """__________________________________________⬇️️TikTok API⬇️️__________________________________________"""


    # 获取单个视频数据
    # Get single video data
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(7))
    async def get_tiktok_video_data(self, tiktok_video_url: str) -> list:
        aweme_list = []
        url = f'{self.domain}/tiktok_video_data/?tiktok_video_url={tiktok_video_url}'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        # 账号可用性检测/Account availability check
        if not json_data.get('detail'):
            aweme_list.extend(json_data.get('aweme_list'))
        return aweme_list


    # 获取用户主页的所有视频数据
    # Get all video data on the user's homepage
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(7))
    async def get_tiktok_profile_videos(self, tiktok_video_url: str, cursor:int=None, count:int=None, get_all:bool=False) -> list:
        # 空列表/empty list
        aweme_list = []
        # 默认值/Default value
        cursor = cursor or 0
        count = count or 20
        url = f'{self.domain}/tiktok_profile_videos/?tiktok_video_url={tiktok_video_url}&cursor={cursor}&count={count}'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        # 账号可用性检测/Account availability check
        if not json_data.get('detail'):
            aweme_list.extend(json_data.get('aweme_list'))
        # 是否获取所有数据/Whether to get all data
        while get_all and json_data.get('has_more'):
            url = json_data.get('next_url')
            status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
            await self.check_token(status_code)
            # 账号可用性检测/Account availability check
            if not json_data.get('detail'):
                aweme_list.extend(json_data.get('aweme_list'))
        # 执行完成后返回视频列表/Return video list after completion
        return aweme_list


    # 获取用户主页的所有点赞视频数据
    # Get all liked video data on the user's homepage
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(7))
    async def get_tiktok_profile_liked_videos(self, tiktok_video_url: str, cursor:int=None, count:int=None, get_all:bool=False) -> list:
        # 空列表/empty list
        aweme_list = []
        # 默认值/Default value
        cursor = cursor or 0
        count = count or 20
        url = f'{self.domain}/tiktok_profile_liked_videos/?tiktok_video_url={tiktok_video_url}&cursor={cursor}&count={count}'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        # 账号可用性检测/Account availability check
        if not json_data.get('detail'):
            aweme_list.extend(json_data.get('aweme_list'))
        # 是否获取所有数据/Whether to get all data
        while get_all and json_data.get('has_more'):
            url = json_data.get('next_url')
            status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
            await self.check_token(status_code)
            # 账号可用性检测/Account availability check
            if not json_data.get('detail'):
                aweme_list.extend(json_data.get('aweme_list'))
        # 执行完成后返回视频列表/Return video list after completion
        return aweme_list


    # 获取TikTok视频的所有评论数据
    # Get all comment data of TikTok video
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(7))
    async def get_tiktok_video_comments(self, tiktok_video_url: str, cursor:int=None, count:int=None, get_all:bool=False) -> list:
        comments_list = []
        # 默认值/Default value
        cursor = cursor or 0
        count = count or 20
        url = f'{self.domain}/tiktok_video_comments/?tiktok_video_url={tiktok_video_url}&cursor={cursor}&count={count}'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        # 账号可用性检测/Account availability check
        if not json_data.get('detail'):
            comments_list.extend(json_data.get('comments_list'))
        # 是否获取所有数据/Whether to get all data
        while get_all and json_data.get('has_more'):
            url = json_data.get('next_url')
            status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
            await self.check_token(status_code)
            # 账号可用性检测/Account availability check
            if not json_data.get('detail'):
                comments_list.extend(json_data.get('comments_list'))
        # 执行完成后返回视频列表/Return video list after completion
        return comments_list


    # 获取音乐页面上的所有(理论上能抓取到的)视频数据
    # Get all (theoretically) video data on the music page
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(7))
    async def get_tiktok_music_videos(self, tiktok_music_url: str, cursor:int=None, count:int=None, get_all:bool=False) -> list:
        aweme_list = []
        # 默认值/Default value
        cursor = cursor or 0
        count = count or 20
        url = f'{self.domain}/tiktok_music_videos/?tiktok_music_video_url={tiktok_music_url}&cursor={cursor}&count={count}'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        # 账号可用性检测/Account availability check
        if not json_data.get('detail'):
            aweme_list.extend(json_data.get('aweme_list'))
        # 是否获取所有数据/Whether to get all data
        while get_all and json_data.get('has_more'):
            url = json_data.get('next_url')
            status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
            await self.check_token(status_code)
            # 账号可用性检测/Account availability check
            if not json_data.get('detail'):
                aweme_list.extend(json_data.get('aweme_list'))
        # 执行完成后返回视频列表/Return video list after completion
        return aweme_list


    """__________________________________________⬇️️Douyin API⬇️__________________________________________"""


    # 获取抖音用户单个视频数据
    # Get a single video data of Douyin user
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(7))
    async def get_douyin_video_data(self, douyin_video_url: str) -> list:
        aweme_list = []
        url = f'{self.domain}/douyin_video_data/?douyin_video_url={douyin_video_url}'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        # 账号可用性检测/Account availability check
        if not json_data.get('detail'):
            aweme_list.extend(json_data.get('aweme_list'))
        return aweme_list


    # 获取抖音用户主页的所有视频数据
    # Get all video data of Douyin user home page
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(7))
    async def get_douyin_profile_videos(self, douyin_user_url: str, cursor:int=None, count:int=None, get_all:bool=False) -> list:
        # 空列表/empty list
        aweme_list = []
        # 默认值/Default value
        cursor = cursor or 0
        count = count or 20
        url = f'{self.domain}/douyin_profile_videos/?douyin_profile_url={douyin_user_url}&cursor={cursor}&count={count}'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        # 账号可用性检测/Account availability check
        if not json_data.get('detail'):
            aweme_list.extend(json_data.get('aweme_list'))
        # 是否获取所有数据/Whether to get all data
        while get_all and json_data.get('has_more'):
            url = json_data.get('next_url')
            status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
            await self.check_token(status_code)
            # 账号可用性检测/Account availability check
            if not json_data.get('detail'):
                aweme_list.extend(json_data.get('aweme_list'))
        # 执行完成后返回视频列表/Return video list after completion
        return aweme_list


    # 获取抖音用户主页的所有点赞视频数据
    # Get all liked video data of Douyin user home page
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(7))
    async def get_douyin_profile_liked_videos(self, douyin_user_url: str, cursor:int=None, count:int=None, get_all:bool=False) -> list:
        aweme_list = []
        url = f'{self.domain}/douyin_profile_liked_videos/?douyin_profile_url={douyin_user_url}&cursor={cursor}&count={count}'
        status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
        await self.check_token(status_code)
        # 账号可用性检测/Account availability check
        if not json_data.get('detail'):
            aweme_list.extend(json_data.get('aweme_list'))
        # 是否获取所有数据/Whether to get all data
        while get_all and json_data.get('has_more'):
            url = json_data.get('next_url')
            status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
            await self.check_token(status_code)
            # 账号可用性检测/Account availability check
            if not json_data.get('detail'):
                aweme_list.extend(json_data.get('aweme_list'))
        # 执行完成后返回视频列表/Return video list after completion
        return aweme_list


    # 获取抖音视频的所有评论数据
    # Get all comment data of Douyin video
    @retry(stop=stop_after_attempt(4), wait=wait_fixed(7))
    async def get_douyin_video_comments(self, douyin_video_url: str, cursor: int = None, count: int = None,
                                            get_all: bool = False) -> list:
            comments_list = []
            # 默认值/Default value
            cursor = cursor or 0
            count = count or 20
            url = f'{self.domain}/douyin_video_comments/?douyin_video_url={douyin_video_url}&cursor={cursor}&count={count}'
            status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
            await self.check_token(status_code)
            # 账号可用性检测/Account availability check
            if not json_data.get('detail'):
                comments_list.extend(json_data.get('comments_list'))
            # 是否获取所有数据/Whether to get all data
            while get_all and json_data.get('has_more'):
                url = json_data.get('next_url')
                status_code, text, json_data = await self.client.request("GET", url, headers=self.headers)
                await self.check_token(status_code)
                # 账号可用性检测/Account availability check
                if not json_data.get('detail'):
                    comments_list.extend(json_data.get('comments_list'))
            # 执行完成后返回视频列表/Return video list after completion
            return comments_list

