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

### 项目进度

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

## 1. 制作待办事宜 `Todo` 列表

- [ ] 🎉 修复失效端点
