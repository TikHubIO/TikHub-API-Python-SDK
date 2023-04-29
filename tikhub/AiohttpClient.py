import aiohttp
import asyncio


class AiohttpClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def request(self, method, url, headers=None, params=None, data=None, json=None):
        """
        发起单独的HTTP请求
        :param method: 请求方法
        :param url: 请求URL
        :param headers: 请求头
        :param params: URL参数
        :param data: 表单数据
        :param json: JSON数据
        :return: 包含响应状态码、文本和JSON的字典。
        """
        # 发起一个单独的HTTP请求
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers, params=params, data=data, json=json) as response:
                # 获取响应内容
                response_text = await response.text()
                response_json = None
                if response_text:
                    try:
                        response_json = await response.json()
                    except Exception as e:
                        print("Error in AiohttpClient.request when response.json():", e)
                # 返回响应状态码、文本和JSON
                # return response.status, response_text, response_json
                result = {
                    'status': response.status,
                    'text': response_text,
                    'json': response_json
                }
                return result

    async def make_requests(self, requests: list):
        """
        批量发起HTTP请求
        :param requests: 请求列表, 列表内是元组格式，[(method, url, headers, params, data, json)]。
        :return: 包含所有请求结果的列表。
        """
        # 批量发起HTTP请求
        async with aiohttp.ClientSession() as session:
            # 创建异步任务列表
            tasks = []
            for request in requests:
                method, url, headers, params, data, json = request
                task = session.request(method, url, headers=headers, params=params, data=data, json=json)
                tasks.append(task)
            # 并发处理所有请求
            results = []
            for task in asyncio.as_completed(tasks):
                # 等待异步任务完成
                response = await task
                # 获取响应内容
                response_text = await response.text()
                if response_text:
                    try:
                        response_json = await response.json()
                    except Exception as e:
                        response_json = None
                # 将结果添加到列表中
                results.append({
                    str(response.url): {
                        'method': response.method,
                        'status': response.status,
                        'text': response_text,
                        'json': response_json
                    }
                })
            # 返回所有请求的结果列表
            return results


if __name__ == '__main__':
    # 批量发起HTTP请求
    requests = [
        # GET请求
        ('GET',  # method
         'https://api.tikhub.io/',  # url
         {'Authorization': 'Bearer TOKEN'},  # headers
         None, None, None),  # params, data, json
        # POST请求
        ('POST',
         'https://api.tikhub.io/users/login',
         {'Authorization': 'Bearer TOKEN'},
         None, {'title': 'New post', 'content': 'Hello world!'}, None)
    ]
    client = AiohttpClient()
    results = asyncio.run(client.make_requests(requests))
    print(results)
