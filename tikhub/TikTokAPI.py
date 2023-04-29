import asyncio
from tikhub.Auth import Auth


class TikTokAPI(Auth):

    def __init__(self, token: str):
        super().__init__(token)

    # 获取TikTok视频信息/Get TikTok video information
    async def get_tiktok_video_data(self, tiktok_video_url: str, region: str = 'US', language: str = 'en') -> dict:
        endpoint = "/tiktok/video_data/"
        params = f'tiktok_video_url={tiktok_video_url}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取TikTok用户信息/Get TikTok user information
    async def get_tiktok_user_data(self, tiktok_video_url: str, region: str = 'US', language: str = 'en') -> dict:
        endpoint = "/tiktok/user_data/"
        params = f'tiktok_video_url={tiktok_video_url}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取TikTok用户视频列表/Get TikTok user video list
    async def get_tiktok_profile_videos(self, tiktok_video_url: str = None, cursor: int = 0,
                                        count: int = 20, region: str = 'US', language: str = 'en') -> dict:
        endpoint = "/tiktok/profile_videos/"
        params = f'tiktok_video_url={tiktok_video_url}&cursor={cursor}&count={count}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取用户主页点赞过的视频列表/Get the list of videos liked on the user's homepage
    async def get_tiktok_profile_liked_videos(self, tiktok_video_url: str = None, cursor: int = 0,
                                              count: int = 20, region: str = 'US', language: str = 'en') -> dict:
        endpoint = "/tiktok/profile_liked_videos/"
        params = f'tiktok_video_url={tiktok_video_url}&cursor={cursor}&count={count}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取TikTok视频评论数据/Get TikTok video comment data
    async def get_tiktok_video_comments(self, tiktok_video_url: str = None, cursor: int = 0,
                                        count: int = 20, region: str = 'US', language: str = 'en') -> dict:
        endpoint = "/tiktok/video_comments/"
        params = f'tiktok_video_url={tiktok_video_url}&cursor={cursor}&count={count}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取配乐页视频数据/Get music page video data
    async def get_tiktok_music_videos(self, tiktok_music_video_url: str = None, cursor: int = 0,
                                      count: int = 20, region: str = 'US', language: str = 'en') -> dict:
        endpoint = "/tiktok/music_videos/"
        params = f'tiktok_music_video_url={tiktok_music_video_url}&cursor={cursor}&count={count}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取TikTok热搜数据/Get TikTok hot search data
    async def get_tiktok_search_data_hot(self, keyword: str, cursor: int = 0, count: int = 20, region: str = 'US',
                                         language: str = 'en') -> dict:
        endpoint = "/tiktok/search_data_hot/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取TikTok搜索用户数据/Get TikTok search user data
    async def get_tiktok_search_data_users(self, keyword: str, cursor: int = 10, region: str = 'US',
                                           language: str = 'en'):
        endpoint = "/tiktok/search_data_users/"
        params = f'keyword={keyword}&cursor={cursor}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取TikTok搜索视频数据/Get TikTok search video data
    async def get_tiktok_search_data_videos(self, keyword: str, cursor: int = 0, count: int = 20, region: str = 'US',
                                            language: str = 'en'):
        endpoint = "/tiktok/search_data_videos/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取TikTok搜索直播数据/Get TikTok search live data
    async def get_tiktok_search_data_live(self, keyword: str, cursor: int = 0, count: int = 20, region: str = 'US',
                                          language: str = 'en'):
        endpoint = "/tiktok/search_data_live/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取TikTok搜索挑战数据/Get TikTok search challenge data
    async def get_tiktok_search_data_challenge(self, keyword: str, cursor: int = 0, count: int = 20, region: str = 'US',
                                               language: str = 'en'):
        endpoint = "/tiktok/search_data_challenge/"
        params = f'keyword={keyword}&cursor={cursor}&count={count}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 获取TikTok挑战数据/Get TikTok challenge data
    async def get_tiktok_challenge_data(self, challenge_id: int, cursor: int = 0, count: int = 20, region: str = 'US',
                                        language: str = 'en'):
        endpoint = "/tiktok/challenge_data/"
        params = f'challenge_id={challenge_id}&cursor={cursor}&count={count}&region={region}&language={language}'
        url = f'{self.domain}{endpoint}?{params}'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')


if __name__ == '__main__':
    token = input('Please enter your TikTok token: ')

    tiktok_api = TikTokAPI(token)

    tiktok_video_url = "https://www.tiktok.com/@evil0ctal/video/7201344014984006954"

    tiktok_music_video_url = "https://www.tiktok.com/music/Original-Sound-7128362040359488261"

    challenge_id = 7551

    r = None

    # 获取视频数据/Get video data
    # r = asyncio.run(tiktok_api.get_tiktok_video_data(tiktok_video_url))

    # 获取用户数据/Get user data
    # r = asyncio.run(tiktok_api.get_tiktok_user_data(tiktok_video_url))

    # 获取用户视频数据/Get user video data
    # r = asyncio.run(tiktok_api.get_tiktok_profile_videos(tiktok_video_url))

    # 获取用户主页点赞过的视频列表/Get the list of videos liked on the user's homepage
    # r = asyncio.run(tiktok_api.get_tiktok_profile_liked_videos(tiktok_video_url))

    # 获取TikTok视频评论数据/Get TikTok video comment data
    # r = asyncio.run(tiktok_api.get_tiktok_video_comments(tiktok_video_url))

    # 获取配乐页视频数据/Get music page video data
    # r = asyncio.run(tiktok_api.get_tiktok_music_videos(tiktok_music_video_url))

    # 获取TikTok热搜数据/Get TikTok hot search data
    # r = asyncio.run(tiktok_api.get_tiktok_search_data_hot('cat'))

    # 获取TikTok搜索用户数据/Get TikTok search user data
    # r = asyncio.run(tiktok_api.get_tiktok_search_data_users('cat'))

    # 获取TikTok搜索视频数据/Get TikTok search video data
    # r = asyncio.run(tiktok_api.get_tiktok_search_data_videos('cat'))

    # 获取TikTok搜索直播数据/Get TikTok search live data
    # r = asyncio.run(tiktok_api.get_tiktok_search_data_live('cat'))

    # 获取TikTok搜索挑战数据/Get TikTok search challenge data
    # r = asyncio.run(tiktok_api.get_tiktok_search_data_challenge('cat'))

    # 获取TikTok挑战数据/Get TikTok challenge data
    r = asyncio.run(tiktok_api.get_tiktok_challenge_data(challenge_id))

    print(r)

