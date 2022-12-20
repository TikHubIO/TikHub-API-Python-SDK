import asyncio
import time

from tikhub.api import API


async def async_test() -> None:
    # 异步测试/Async test

    tiktok_url = 'https://www.tiktok.com/@evil0ctal/video/7156033831819037994'

    tiktok_music_url = 'https://www.tiktok.com/music/original-sound-7128362040359488261'

    douyin_url = 'https://www.douyin.com/video/7153585499477757192'

    douyin_user_url = 'https://www.douyin.com/user/MS4wLjABAAAAaNJuvXC83kL5nhaZHubKdjsRJQovgz58wXzlLnJUsslG-Kb24TM1QJlf_2HMaUJk'

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
    print(f'Get {len(aweme_list)} liked videos from profile')

    # 总耗时/Total time
    total_time = round(time.time() - start_time, 2)
    print("\nTest completed, total time: {}s".format(total_time))


if __name__ == '__main__':
    api = API(
        username='test',
        password='test',
        proxy=None,
    )
    asyncio.run(async_test())
