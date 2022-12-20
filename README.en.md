# tkhub_pp([API.TikHub.io](https://api.tikhub.io/docs))

[API.TikHub.io](https://api.tikhub.io/docs), is an asynchronous high-performance Douyin and TikTok data crawling tool. This Repo is a PyPi package based on this API, which is convenient for developers to call.

## note

> This project uses the following Emoji to indicate the development status in the development chart!

| Emoji |                                                representative meaning                                               |
| :---: | :-----------------------------------------------------------------------------------------------------------------: |
|   🚀  |                         Rocket - The feature is written, tested, and deployed to production.                        |
|   ✅   | Checkmark - The feature is written but has yet to be tested and will be deployed to production once the tests pass. |
|   ❌   |                    Cross sign - The feature has not yet been written or has not been written yet.                   |
|   🔜  |                      SOON BREAK - Feature proposed but not yet assigned a designated developer.                     |
|   ⚠️  |                    Warning symbol - There is a problem with the function that needs to be fixed.                    |

## project progress

| state | API endpoint path |        Function        |
| :---: | :---------------: | :--------------------: |
|   🚀  |      `/token`     | generate`Bearer Token` |
|   🚀  |    `/users/me/`   |  Get user information  |

> Requirements for each interface endpoint

| state | support platform |                       need                       | start date |  ETA date |  Developer |
| :---: | :--------------- | :----------------------------------------------: | :--------: | :-------: | :--------: |
|   🚀  | Douyin, TikTok   |             Crawl a single video data            | 2022/10/08 | completed | @Evil0ctal |
|   🚀  | Douyin, TikTok   |         Crawl a single video comment data        | 2022/10/08 | completed | @Evil0ctal |
|   🚀  | Douyin, TikTok   |             Crawl the soundtrack data            | 2022/10/08 | completed | @Evil0ctal |
|   🚀  | Douyin, TikTok   |          Crawl user homepage video data          | 2022/10/08 | completed | @Evil0ctal |
|   🚀  | Douyin, TikTok   | Crawl the user homepage has liked the video data | 2022/10/08 | completed | @Evil0ctal |

> Production and deployment of Douyin-related interfaces - API tags: Douyin

| state |        API endpoint path        |                     Function                     |         issue         |
| :---: | :-----------------------------: | :----------------------------------------------: | :-------------------: |
|   🚀  |      `/douyin_video_data/`      |             Crawl a single video data            |    no known issues    |
|   ⚠️  |    `/douyin_video_comments/`    |         Crawl a single video comment data        | Invalid to be updated |
|   ⚠️  |     `/douyin_music_videos/`     |             Crawl the soundtrack data            | Invalid to be updated |
|   🚀  |    `/douyin_profile_videos/`    |          Crawl user homepage video data          |    no known issues    |
|   🚀  | `/douyin_profile_liked_videos/` | Crawl the user homepage has liked the video data |    no known issues    |

> Production deployment of TikTok-related interfaces - API tags: TikTok

| state |        API endpoint path        |                     Function                     |      issue      |
| :---: | :-----------------------------: | :----------------------------------------------: | :-------------: |
|   🚀  |      `/tiktok_video_data/`      |             Crawl a single video data            | no known issues |
|   🚀  |    `/tiktok_video_comments/`    |         Crawl a single video comment data        | no known issues |
|   🚀  |     `/tiktok_music_videos/`     |             Crawl the soundtrack data            | no known issues |
|   🚀  |    `/tiktok_profile_videos/`    |          Crawl user homepage video data          | no known issues |
|   🚀  | `/tiktok_profile_liked_videos/` | Crawl the user homepage has liked the video data | no known issues |

## to do`Todo`the list

-   [ ] ⚠️ fix`/douyin_video_comments/`endpoint
-   [ ] ⚠️ fix`/douyin_music_videos/`endpoint

## Example of use

```python
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
        username='test',
        password='test',
        proxy=None,
    )
    asyncio.run(async_test())
```
