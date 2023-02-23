import aiohttp

class AiohttpClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def request(self, method, url, headers=None, params=None, data=None, json=None) -> (int, str, dict):
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers, params=params, data=data, json=json) as response:
                response_text = await response.text()
                response_json = None
                if response_text:
                    response_json = await response.json()
                return response.status, response_text, response_json
