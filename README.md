<div align="center">
<h1><a href="https://pypi.org/project/tikhub">TikHub-API-Python-SDK</a></h1>
<a href="https://github.com/TikHubIO/TikHub-API-Python-SDK/blob/main/README.en.md">English</a> | <a href="https://github.com/TikHubIO/TikHub-API-Python-SDK/blob/main/README.md">简体中文</a>
</div>

#### **简介**

🎉「[TikHub.io](https://tikhub.io/)」是一个**开箱即用的集成工具以及服务的平台**，我们的目标是帮助用户快速开展业务，并且支持功能定制。我们的愿景是组建一个社区创业项目，独木难成林，合作能共赢，**每一个社区成员都有机会将他们编写的功能或接口接入我们的平台，并且从中获得收益**。我们已经积累了大量的注册用户以及社区用户，并且为了实现这一愿景，我们正在积极筹划和落实合作策略，以确保生态的持续健康发展，欢迎各位加入我们的[Discord](https://discord.gg/aMEAS8Xsvz)社区。

#### 备注

* TikHub API目前提供以下服务，并且还在不断更新中：
  * [抖音网页版数据接口](https://api.tikhub.io/#/Douyin-Web-API)
  * [抖音App V1数据接口](https://api.tikhub.io/#/Douyin-App-V1-API)
  * [抖音App V2数据接口](https://api.tikhub.io/#/Douyin-App-V2-API)
  * [抖音App V3数据接口](https://api.tikhub.io/#/Douyin-App-V3-API)
  * [TikTok网页版数据接口](https://api.tikhub.io/#/TikTok-Web-API)
  * [TikTok App V2数据接口](https://api.tikhub.io/#/TikTok-App-V2-API)
  * [TikTok App V3数据接口](https://api.tikhub.io/#/TikTok-App-V3-API)
  * [西瓜视频App V2数据接口](https://api.tikhub.io/#/Xigua-App-V2-API)
  * [小红书网页版数据接口](https://api.tikhub.io/#/Xiaohongshu-Web-API)
  * [快手网页版数据接口](https://api.tikhub.io/#/Kuaishou-Web-API)
  * [微博网页版数据接口](https://api.tikhub.io/#/Weibo-Web-API)
  * [Instagram Web以及APP数据接口](https://api.tikhub.io/#/Instagram-Web-And-APP-API)
  * [YouTube Web数据接口](https://api.tikhub.io/#/YouTube-Web-API)
  * [网易云音乐App数据接口](https://api.tikhub.io/#/NetEase-Cloud-Music-API)
  * [Twitter Web数据接口](https://api.tikhub.io/#/Twitter-Web-API)
  * [验证码绕过接口](https://api.tikhub.io/#/Captcha-Solver)
  * [临时邮箱接口](https://api.tikhub.io/#/Temp-Mail-API)
* 请将任何问题或错误报告给[Discord服务器](https://discord.gg/aMEAS8Xsvz)。
---

#### **快速开始**

> 参考资料

- **Swagger UI Docs**: [Swagger UI](https://api.tikhub.io)
- **Documentation/文档**: [API Documentation](https://docs.tikhub.io/)

[TikHub.io](https://tikhub.io/)的大多数API都是RESTFUL的，这意味着你只需要使用基本的HTTP请求即可完成调用。

所有的API都是基于OPenAPI规范进行编写的，这意味着你可以使用我们的`openapi.json`自动生成任何形式的API文档：

[https://api.tikhub.io/openapi.json](https://api.tikhub.io/openapi.json)

当然，我们已经默认使用了Swagger UI来展示我们的API文档，你可以在网页上打开下面的链接，然后在网页上进行API Token的认证，随后点击任意端点然后点击`Try it out`即可测试你所需要的端点，大多数端点都已经携带了默认值或演示值，这会更好的帮助你理解调用的所需参数：

[https://api.tikhub.io](https://api.tikhub.io)

---

#### **鉴权**

> 简介

接口文档中带有🔒图标的端点需要在请求头中携带API Token才可以调用，调用这些接口会使用你账户中的剩余免费额度或账户余额，同时每一个端点还会根据API Token所有者的email地址进行请求速率的限制，每个端点之间都有彼此独立的RPS（Requests per second），在大多数情况下，用户可以每秒请求5次同一个端点。

> 生成API Token

获取API Token的步骤也很简单，你只需要登录到我们的用户后台 [TikHub User](https://tikhub.io/users/api_keys)，然后点击左侧的`API Keys`就可以生成你自己的API Token，同时，你可以自定义API Token的权限（`Scopes`），也可以设置API Token的过期日期（`Expire Date`），还可以手动暂时关闭API Token（`Status`）。

> 在API文档网页上使用

当你完成上面的步骤后，你可以复制你的API Token，然后回到我们的Swagger UI网页，点击页面右侧的绿色`Authorize`，然后在弹窗底部的`Value`输入框中粘贴API Token即可完成鉴权。

> 在HTTP请求中使用

如果你想在HTTP请求中携带API Token，请仔细阅读下方的格式，并且需要在请求头中携带一个叫`Authorization`的字段，下面我将给出一个JSON作为header的示范：

{

"Authorization":"Bearer Your_API_Token"

}

> 备注

请不要分享你的API Token，这可能会造成你的财产损失等一些列问题，我们强烈建议为你的每一个项目都使用不同的API Token，同时不要忘记在创建API Token时勾选对应的`Scopes`，否则在请求时会遇到权限不足的问题。

---

## **使用SDK**

- 通过PyPi安装我们的[SDK](https://pypi.org/project/tikhub/)

```console
pip install tikhub
```

- 导入SDK

```python
from tikhub import Client
```

- 初始化Client

```python
client = Client(base_url="https://api.tikhub.io", 
                api_key="YOUR_API_TOKEN",
                proxies=None,
                max_retries=3,
                max_connections=50,
                timeout=60,
                max_tasks=50)
```

- 请求用户数据示例

```python
# 请求用户信息 | Request user info
user_info = await client.TikHubUser.get_user_info()
print(user_info)

# 请求用户每日使用情况 | Request user daily usage
user_daily_usage = await client.TikHubUser.get_user_daily_usage()
print(user_daily_usage)

# 计算价格 | Calculate price
price = await client.TikHubUser.calculate_price(endpoint="/api/v1/douyin/app/v1/fetch_one_video", request_per_day=100)
print(price)

# 获取阶梯式折扣百分比信息 | Get tiered discount percentage information
tiered_discount_info = await client.TikHubUser.get_tiered_discount_info()
print(tiered_discount_info)

# 获取一个端点的信息 | Get information of an endpoint
endpoint_info = await client.TikHubUser.get_endpoint_info(endpoint="/api/v1/douyin/app/v1/fetch_one_video")
print(endpoint_info)

# 获取所有端点信息 | Get all endpoints information
all_endpoints_info = await client.TikHubUser.get_all_endpoints_info()
print(all_endpoints_info)
```

- Client中的可用属性

```python
# TikHub User | TikHub用户接口
self.TikHubUser = TikHubUser(self.client)

# Douyin | 抖音
self.DouyinWeb = DouyinWeb(self.client)
self.DouyinAppV1 = DouyinAppV1(self.client)
self.DouyinAppV2 = DouyinAppV2(self.client)
self.DouyinAppV3 = DouyinAppV3(self.client)

# TikTok | TikTok
self.TikTokWeb = TikTokWeb(self.client)
self.TikTokAppV2 = TikTokAppV2(self.client)
self.TikTokAppV3 = TikTokAppV3(self.client)

# Instagram | Instagram
self.InstagramWeb = InstagramWeb(self.client)

# Weibo | 微博
self.WeiboWeb = WeiboWeb(self.client)

# Captcha Solver | 验证码解决器
self.CaptchaSolver = CaptchaSolver(self.client)

# Xigua Video APP V2 | 西瓜视频APP V2
self.XiguaAppV2 = XiguaAppV2(self.client)

# XiaoHongShu Web | 小红书网页端
self.XiaohongshuWeb = XiaohongshuWeb(self.client)

# KuaiShou Web | 快手网页端
self.KuaishouWeb = KuaishouWeb(self.client)

# YouTube Web | YouTube网页端
self.YouTubeWeb = YouTubeWeb(self.client)

# 网易云音乐APP | NetEase Cloud Music APP
self.NetEaseCloudMusicAppV1 = NetEaseCloudMusicAppV1(self.client)

# Twitter Web | Twitter网页端
self.TwitterWeb = TwitterWeb(self.client)

# Hybrid Parsing
self.HybridParsing = HybridParsing(self.client)
```

- 使用`DouyinAppV1`的`fetch_one_video`方法调用接口获取单一视频数据。

```python
# 导入异步io库 | Import asyncio
import asyncio

# 导入tikhub | Import tikhub
from tikhub import Client

# 初始化Client | Initialize Client
client = Client(base_url="https://api.tikhub.io", 
                api_key="YOUR_API_TOKEN",
                proxies=None,
                max_retries=3,
                max_connections=50,
                timeout=60,
                max_tasks=50)

if __name__ == "__main__":
    # 获取单个作品数据 | Get single video data
    video_data = asyncio.run(client.DouyinAppV1.fetch_one_video(aweme_id="7345492945006595379"))
    print(video_data)
```

- 我们已经使用HTTPX的对大多数端点进行了异步封装，如果你的代码是同步执行的，你可以使用下面的代码防止异步传染。

```python
# 导入异步io库 | Import asyncio
import asyncio

# 导入tikhub | Import tikhub
from tikhub import Client

# 初始化Client | Initialize Client
client = Client(base_url="https://api.tikhub.io", 
                api_key="YOUR_API_TOKEN",
                proxies=None,
                max_retries=3,
                max_connections=50,
                timeout=60,
                max_tasks=50)

# 获取抖音单一视频数据 | Get a single video data from Douyin
def fetch_one_video(aweme_id: str):
    # 创建一个异步事件循环
    # Create an asynchronous event loop
    loop = asyncio.get_event_loop()

    # 使用异步事件循环运行客户端的fetch_one_video方法，防止异步传染到其他代码。
    # Run the client's fetch_one_video method with the asynchronous event loop, preventing asynchronous infection to other code.
    try:
        __video_data = loop.run_until_complete(client.DouyinAppV1.fetch_one_video(aweme_id=aweme_id))
        return __video_data
    except Exception as e:
        # 如果出现异常，返回异常信息
        # If an exception occurs, return the exception information
        return str(e)
    finally:
        # 关闭异步事件循环
        # Close the asynchronous event
        loop.close()

# 调用fetch_one_video方法 | Call the fetch_one_video method
if __name__ == "__main__":
    video_data = fetch_one_video(aweme_id="7345492945006595379")
    print(video_data)
```

- 由于章节有限，在此处就不列出完整的方法了，你可以通过查看源代码的形式查看每一个属性内实现的方法，每一个方法的命名都是根据端点的`uri`来命名的，例如`/api/v1/douyin/app/v1/fetch_one_video`的方法名就是`fetch_one_video`，你可以根据API文档中的端点来查找对应的方法。
- 并且每个方法接受的参数都已经加上了`type hints`，你可以通过查看方法的参数来了解该方法需要传入的参数类型，这样可以更好的帮助你调用方法。
- 文档中可以自动帮你生成不同编程语言的代码，具体请查看[API Documentation](https://docs.tikhub.io/)。
- 目前可以自动生成代码的编程语言有：
   - Shell
   - JavaScript
   - Java
   - Swift
   - Go
   - PHP
   - Python
   - HTTP
   - C
   - C#
   - Objective-C
   - Ruby
   - OCaml
   - Dart
   - R
