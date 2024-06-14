# 导入API SDK Client类

from tikhub.http_client.api_client import APIClient


class TempMailV1:
    # 初始化 | Initialize
    def __init__(self, client: APIClient):
        self.client = client

    # 获取一个临时邮箱 | Get a temporary email
    async def get_temp_email_address(self):
        endpoint = "/api/v1/temp_mail/v1/get_temp_email_address"
        data = await self.client.fetch_get_json(f"{endpoint}")
        return data

    # 获取邮件列表 | Get a list of emails
    async def get_emails_inbox(self, token: str):
        endpoint = "/api/v1/temp_mail/v1/get_emails_inbox"
        data = await self.client.fetch_get_json(f"{endpoint}?token={token}")
        return data

    # 通过邮件ID获取邮件数据 | Get email data by email ID
    async def get_email_by_id(self, token: str, message_id: str):
        endpoint = "/api/v1/temp_mail/v1/get_email_by_id"
        data = await self.client.fetch_get_json(f"{endpoint}?token={token}&message_id={message_id}")
        return data
