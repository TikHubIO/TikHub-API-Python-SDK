import asyncio
import platform

from tikhub.AiohttpClient import AiohttpClient


class Auth:
    # 初始化/initialization
    def __init__(self, token: str, domain: str = 'https://api.tikhub.io', proxy: str = None):
        super().__init__()
        self.token = token  # Token/token
        self.domain = domain  # 域名/domain
        self.proxies = proxy  # HTTP代理/HTTP proxy
        self.headers = {'Authorization': f'Bearer {token}'} if 'bearer ' not in token.lower() else {'Authorization': token}
        self.client = AiohttpClient()
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    """__________________________________________⬇️️认证(authenticate)⬇️️__________________________________________"""

    # 检查Token是否过期或无效/Check if the token is expired or invalid
    @staticmethod
    async def check_token(response: dict):
        if response['status'] != 200:
            error = Exception(f'Error: {response}')
            raise error

    # 获取TikHub用户信息/Get TikHub user information
    async def get_user_info(self) -> dict:
        url = f'{self.domain}/users/me/'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')

    # 每日签到/Daily check-in
    async def daily_check_in(self) -> dict:
        url = f'{self.domain}/promotion/daily_check_in'
        result = await self.client.request('GET', url, self.headers, None, None, None)
        await self.check_token(result)
        return result.get('json')


if __name__ == '__main__':

    token = input('请输入token: ')

    auth = Auth(token)

    r = None

    # 读取用户信息/Read user information
    r = asyncio.run(auth.get_user_info())
    print(r)

    # 每日签到/Daily check-in
    r = asyncio.run(auth.daily_check_in())
    print(r)

