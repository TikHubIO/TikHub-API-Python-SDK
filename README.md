# 更新 - 2023年6月15日

<div align="center">
<h1><a href="https://pypi.org/project/tikhub">TikHub_API</a></h1>
<a href="https://github.com/TikHubIO/TikHub_API_PyPi/blob/main/README.en.md">English</a> | <a href="https://github.com/TikHubIO/TikHub_API_PyPi/blob/main/README.md">简体中文</a>
</div>
<h4>简介</h4>
<p><a href="https://tikhub.io">TikHub</a>是抖音与TikTok非官方的RESTful API平台。</p>
<p>我们提供的API只能获取公开数据，即任何人都可以通过浏览器及APP等访问抖音或TikTok以获取它们。</p>
<p>如果您有任何建议或者需求，请联系我们，更多的功能正在开发中，敬请期待！</p>
<hr>
<h4>鉴权</h4>
<p>接口文档中带有🔒的接口需要在请求头中携带Token才可调用。</p>
<p>调用这些接口会使用你账户中的剩余请求次数！</p>

<hr>
<h4>购买</h4>
<p>Website(🚧ing): <a href="https://tikhub.io">dash.tikhub.io</a></p>
<p>Discord(💳buy): <a href="https://discord.gg/kk23BGeYrJ">https://discord.gg/kk23BGeYrJ</a></p>
<p>Github: <a href="https://github.com/TikHubIO">https://github.com/TikHubIO</a></p>
<p>Email: <a href="mailto:tikhub.io@proton.me">tikhub.io@proton.me</a></p>
<p>WeChat/微信: Evil-Bot</p>
<hr>
<h4>公告</h4>
<p>TikHub的API将使用<strong>免费加付费</strong>的形式运行。</p>
<p>登录后，通过签到可以随机获得50-100次API请求，每24小时可签到一次。</p
<hr>

## 使用示例

> 查看[test.py](https://github.com/TikHubIO/Douyin-TikTok-API-Python-SDK/blob/main/test/test.py)

- 第一步/first step: 安装/Install

```bash
pip install tikhub
```

- 第二步/second step: 初始化/Initialization

``` python
from tikhub import TikTokAPI, DouyinAPI

token = input('Please enter your TikTok token: ')
tiktok_api = TikTokAPI(token)
douyin_api = DouyinAPI(token)

```

- 第三步/third step: 调用方法/call the function

``` python
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
```


