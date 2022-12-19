# TikHub_PyPi([API.TikHub.io](https://api.tikhub.io/docs))

[API.TikHub.io](https://api.tikhub.io/docs)，是一个异步高性能的Douyin，TikTok数据爬取工具，此Repo为基于该API的PyPi包，方便各位开发者调用。


## 注释

> 本项目使用以下Emoji在开发图表中表明开发状态!

| Emoji | 代表的含义 |
| :---: | :---: |
| 🚀 | 火箭 - 功能已编写完成并测试通过，并且已部署至生产环境。|
| ✅ | 勾选符 - 功能已编写完成，但还有待测试，测试通过后将部署至生产环境。|
| ❌ | 叉号符 - 功能尚未开始编写或还未编写完成。|
| 🔜 | SOON符 - 功能已提出但尚未分配指定开发人员。|
| ⚠️ | 警告符 - 功能出现问题待修复。|

## 项目进度

| 状态 | API端点路径 | 功能 |
| :---: | :---: | :---: |
| 🚀 | `/token` | 生成`Bearer Token` |
| 🚀 | `/users/me/` | 获取用户信息 |

> 各接口端点需求

| 状态 | 支持平台 | 需求 | 开始日期 | ETA日期 | 开发者 |
| :---: | :--- | :---: | :---: | :---: |:---: |
| 🚀 | 抖音, TikTok | 爬取单个视频数据 | 2022/10/08 | 已完成 | @Evil0ctal |
| 🚀 | 抖音, TikTok | 爬取单个视频评论数据 | 2022/10/08 | 已完成 | @Evil0ctal |
| 🚀 | 抖音, TikTok | 爬取配乐作品数据 | 2022/10/08 | 已完成 | @Evil0ctal |
| 🚀 | 抖音, TikTok | 爬取用户主页视频数据 | 2022/10/08 | 已完成 | @Evil0ctal |
| 🚀 | 抖音, TikTok | 爬取用户主页已点赞视频数据 | 2022/10/08 | 已完成 | @Evil0ctal |

> 抖音相关接口生产部署 - API tags: Douyin

| 状态 | API端点路径 | 功能 | issue |
| :---: | :---: | :---: | :---: |
| 🚀 | `/douyin_video_data/` | 爬取单个视频数据 | 无已知问题 |
| ⚠️ | `/douyin_video_comments/` | 爬取单个视频评论数据 | 失效待更新 |
| ⚠️ | `/douyin_music_videos/` | 爬取配乐作品数据 | 失效待更新 |
| 🚀 | `/douyin_profile_videos/` | 爬取用户主页视频数据 | 无已知问题 |
| 🚀 | `/douyin_profile_liked_videos/` | 爬取用户主页已点赞视频数据 | 无已知问题 |

> TikTok相关接口生产部署 - API tags: TikTok

| 状态 | API端点路径 | 功能 | issue |
| :---: | :---: | :---: | :---: |
| 🚀 | `/tiktok_video_data/` | 爬取单个视频数据 | 无已知问题 |
| 🚀 | `/tiktok_video_comments/` | 爬取单个视频评论数据 | 无已知问题 |
| 🚀 | `/tiktok_music_videos/` | 爬取配乐作品数据 | 无已知问题 |
| 🚀 | `/tiktok_profile_videos/` | 爬取用户主页视频数据 | 无已知问题 |
| 🚀 | `/tiktok_profile_liked_videos/` | 爬取用户主页已点赞视频数据 | 无已知问题 |

## 待办事宜 `Todo` 列表

- [ ] ⚠️ 修复`/douyin_video_comments/`端点
- [ ] ⚠️ 修复`/douyin_music_videos/`端点

## 使用示例

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
