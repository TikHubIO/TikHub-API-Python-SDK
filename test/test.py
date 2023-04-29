import asyncio

from tikhub import TikTokAPI, DouyinAPI


if __name__ == '__main__':
    token = input('Please enter your TikTok token: ')

    tiktok_api = TikTokAPI(token)
    douyin_api = DouyinAPI(token)

    tiktok_video_url = "https://www.tiktok.com/@evil0ctal/video/7201344014984006954"

    r = None

    # 读取用户信息/Read user information
    r = asyncio.run(tiktok_api.get_user_info())
    print(r)

    tiktok_video_url = 'https://www.tiktok.com/@evil0ctal/video/7156033831819037994'
    tiktok_music_url = 'https://www.tiktok.com/music/original-sound-7128362040359488261'

    # 解析单一tiktok视频/Parse a single tiktok video
    # r = asyncio.run(tiktok_api.get_tiktok_video_data(tiktok_video_url))
    # print(r)

    # 解析tiktok用户信息/Parse tiktok user information
    # r = asyncio.run(tiktok_api.get_tiktok_user_data(tiktok_video_url))
    # print(r)

    # 解析tiktok用户的所有视频数据/Parse all video data of tiktok user
    # r = asyncio.run(tiktok_api.get_tiktok_profile_videos(tiktok_video_url, count=1))
    # print(r)

    # 解析tiktok用户的所有喜欢视频数据/Parse all liked video data of tiktok user
    # r = asyncio.run(tiktok_api.get_tiktok_profile_liked_videos(tiktok_video_url, count=1))
    # print(r)

    # 解析tiktok视频的所有评论数据/Parse all comment data of tiktok video
    # r = asyncio.run(tiktok_api.get_tiktok_video_comments(tiktok_video_url, count=1))
    # print(r)

    # 解析配乐页视频数据/Parse video data of music page
    # r = asyncio.run(tiktok_api.get_tiktok_music_videos(tiktok_music_url, count=1))
    # print(r)

    # 解析tiktok热搜/Parse tiktok hot search
    r = asyncio.run(tiktok_api.get_tiktok_search_data_hot('evil0ctal'))
    print(r)
