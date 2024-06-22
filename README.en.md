<div align="center">
<h1><a href="https://pypi.org/project/tikhub">TikHub-API-Python-SDK</a></h1>
<a href="https://github.com/TikHubIO/TikHub-API-Python-SDK/blob/main/README.en.md">English</a> | <a href="https://github.com/TikHubIO/TikHub-API-Python-SDK/blob/main/README.md">简体中文</a>
</div>

#### **Introduction**

🎉「[TikHub.io](https://tikhub.io/)"Is a**A platform for out-of-the-box integration tools and services**, our goal is to help users quickly start business and support function customization. Our vision is to form a community entrepreneurship project. A single tree cannot grow into a forest, but cooperation can lead to a win-win situation.**Every community member has the opportunity to integrate the functions or interfaces they write into our platform and benefit from them**. We have accumulated a large number of registered users and community users, and in order to realize this vision, we are actively planning and implementing cooperation strategies to ensure the sustainable and healthy development of the ecosystem. Welcome everyone to join us[Discord](https://discord.gg/aMEAS8Xsvz)Community.

* * *

#### **quick start**

[TikHub.io](https://tikhub.io/)Most of the APIs are RESTFUL, which means you only need to use basic HTTP requests to complete the call.

All APIs are written based on the OPenAPI specification, which means you can use our`openapi.json`Automatically generate any form of API documentation:

<https://api.tikhub.io/openapi.json>

Of course, we have used Swagger UI by default to display our API documents. You can open the following link on the web page, then authenticate the API Token on the web page, then click on any endpoint and click`Try it out`You can test the endpoints you need. Most endpoints already carry default values ​​or demo values, which will better help you understand the required parameters of the call:

<https://api.tikhub.io>

* * *

#### **Authentication**

> Introduction

The endpoints with the 🔒 icon in the interface document need to carry the API Token in the request header before they can be called. Calling these interfaces will use the remaining free quota or account balance in your account. At the same time, each endpoint will also be based on the email of the API Token owner. The address limits the request rate. Each endpoint has independent RPS (Requests per second). In most cases, users can request the same endpoint 5 times per second.

> Generate API Token

The steps to obtain API Token are also very simple, you only need to log in to our user backend[Stay tuned](https://tikhub.io/users/api_keys), then click on the left`API Keys`You can generate your own API Token, and at the same time, you can customize the permissions of the API Token (`Scopes`), you can also set the expiration date of the API Token (`Expire Date`), you can also manually temporarily close the API Token (`Status`）。

> Used on the API documentation web page

After you complete the above steps, you can copy your API Token, then return to our Swagger UI web page and click the green on the right side of the page`Authorize`, and then at the bottom of the pop-up window`Value`Paste the API Token in the input box to complete the authentication.

> Used in HTTP requests

If you want to carry the API Token in the HTTP request, please read the format below carefully, and you need to carry a called`Authorization`Field, below I will give an example of JSON as header:

{

"Authorization":"Bearer Your_API_Token"

}

> Remark

Please do not share your API Token, as this may cause you to lose property and other problems. We strongly recommend using a different API Token for each of your projects, and don’t forget to check the corresponding box when creating the API Token.`Scopes`, otherwise you will encounter insufficient permissions when requesting.

* * *

## **Use SDK**

-   Install ours via PyPi[SDK](https://pypi.org/project/tikhub/)

```console
pip install tikhub
```

-   Import SDK

```python
from tikhub import Client
```

-   InitializeClient

```python
client = Client(base_url="https://api.tikhub.io", 
                api_key="YOUR_API_TOKEN",
                proxies=None,
                max_retries=3,
                max_connections=50,
                timeout=10,
                max_tasks=50)
```

-   Request user data example

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

-   Available properties in Client

```python
# TikHub
self.TikHubUser = TikHubUser(self.client)

# Douyin
self.DouyinWeb = DouyinWeb(self.client)
self.DouyinAppV1 = DouyinAppV1(self.client)
self.DouyinAppV2 = DouyinAppV2(self.client)
self.DouyinAppV3 = DouyinAppV3(self.client)

# TikTok
self.TikTokWeb = TikTokWeb(self.client)
self.TikTokAppV2 = TikTokAppV2(self.client)
self.TikTokAppV3 = TikTokAppV3(self.client)

# Instagram
self.InstagramWeb = InstagramWeb(self.client)

# Weibo
self.WeiboWeb = WeiboWeb(self.client)

# Captcha Solver
self.CaptchaSolver = CaptchaSolver(self.client)
```

-   use`DouyinAppV1`of`fetch_one_video`The method calls the interface to obtain single video data.

```python
# 获取单个作品数据 | Get single video data
video_data = await client.DouyinAppV1.fetch_one_video(aweme_id="7345492945006595379")
print(video_data)
```

-   We have used HTTPX to asynchronously encapsulate most endpoints. If your code is executed synchronously, you can use the following code to prevent asynchronous infection.

```python
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
```

-   Due to the limited chapters, the complete methods are not listed here. You can view the methods implemented in each attribute by viewing the source code, and the parameters accepted by each method have been added.`type hints`。
