# 导入API SDK Client类

from tikhub.http_client.api_client import APIClient


class CaptchaSolver:
    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # Cloudflare Turnstile
    async def cloudflare_turnstile(self, sitekey: str, url: str, proxy: dict = None):
        endpoint = "/api/v1/captcha/cloudflare_turnstile"
        payload = {
            "sitekey": sitekey,
            "url": url,
            "proxy": proxy
        }
        return await self.client.fetch_post_json(endpoint, payload)

    # Recaptcha V2
    async def recaptcha_v2(self, sitekey: str, url: str, proxy: dict = None):
        endpoint = "/api/v1/captcha/recaptcha_v2"
        payload = {
            "sitekey": sitekey,
            "url": url,
            "proxy": proxy
        }
        return await self.client.fetch_post_json(endpoint, payload)

    # Recaptcha V3
    async def recaptcha_v3(self, sitekey: str, url: str, action: str = None, proxy: dict = None):
        endpoint = "/api/v1/captcha/recaptcha_v3"
        payload = {
            "sitekey": sitekey,
            "url": url,
            "action": action,
            "proxy": proxy
        }
        return await self.client.fetch_post_json(endpoint, payload)

    # hCaptcha
    async def hcaptcha(self, sitekey: str, url: str, proxy: dict = None):
        endpoint = "/api/v1/captcha/hcaptcha"
        payload = {
            "sitekey": sitekey,
            "url": url,
            "proxy": proxy
        }
        return await self.client.fetch_post_json(endpoint, payload)

    # Tencent Captcha
    async def tencent_captcha(self, app_id: str, url: str, proxy: dict = None):
        endpoint = "/api/v1/captcha/tencent_captcha"
        payload = {
            "app_id": app_id,
            "url": url,
            "proxy": proxy
        }
        return await self.client.fetch_post_json(endpoint, payload)

    # Amazon Captcha
    async def amazon_captcha(self, app_id: str, url: str, proxy: dict = None):
        endpoint = "/api/v1/captcha/amazon_captcha"
        payload = {
            "app_id": app_id,
            "url": url,
            "proxy": proxy
        }
        return await self.client.fetch_post_json(endpoint, payload)
