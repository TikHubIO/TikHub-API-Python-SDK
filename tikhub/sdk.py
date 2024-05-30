# sdk.py
from tikhub.client.api_client import APIClient

# TikHub
from tikhub.api.v1.endpoints.tikhub.tikhub_user import TikHubUser


# Douyin
from tikhub.api.v1.endpoints.douyin.web.douyin_web import DouyinWeb
from tikhub.api.v1.endpoints.douyin.app.douyin_app_v1 import DouyinAppV1
from tikhub.api.v1.endpoints.douyin.app.douyin_app_v2 import DouyinAppV2
from tikhub.api.v1.endpoints.douyin.app.douyin_app_v3 import DouyinAppV3

# TikTok
from tikhub.api.v1.endpoints.tiktok.web.tiktok_web import TikTokWeb
from tikhub.api.v1.endpoints.tiktok.app.tiktok_app_v2 import TikTokAppV2
from tikhub.api.v1.endpoints.tiktok.app.tiktok_app_v3 import TikTokAppV3

# Instagram
from tikhub.api.v1.endpoints.instagram.web.instagram_web import InstagramWeb

# Weibo
from tikhub.api.v1.endpoints.weibo.web.weibo_web import WeiboWeb


class Client:
    def __init__(self, base_url: str = 'https://beta.tikhub.io', api_key: str = None):
        # Base URL
        self.base_url = base_url

        # API Key
        self.api_key = api_key
        if not self.api_key:
            raise RuntimeError("API Key is required to use the SDK. | 需要API Key才能使用SDK。")

        # API Client
        self.client = APIClient(
            base_url=self.base_url,
            client_headers={"Authorization": f"Bearer {self.api_key}"},
            proxies=None,
            max_retries=3,
            max_connections=50,
            timeout=10,
            max_tasks=50,
        )

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
