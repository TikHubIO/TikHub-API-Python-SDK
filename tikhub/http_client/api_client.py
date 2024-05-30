import asyncio
from typing import Union, List, Any

import httpx
from httpx import Response

from tikhub.http_client.api_exceptions import (
    APIError,
    APIConnectionError,
    APIResponseError,
    APITimeoutError,
    APIUnavailableError,
    APIUnauthorizedError,
    APINotFoundError,
    APIRateLimitError,
    APIRetryExhaustedError,
)
from tikhub.http_client.api_logger import logger


class APIClient:
    """
    基础API客户端 (Base API http_client)
    """

    def __init__(
            self,
            base_url: str,
            client_headers: dict,
            proxies: dict = None,
            max_retries: int = 3,
            max_connections: int = 50,
            timeout: int = 30,
            max_tasks: int = 50,
    ):
        if isinstance(proxies, dict):
            self.proxies = proxies
            # [f"{k}://{v}" for k, v in proxies.items()]
        else:
            self.proxies = None

        # API基础URL / API base URL
        self.base_url = base_url
        # API请求头 / API request header
        self.client_headers = client_headers

        # 异步的任务数 / Number of asynchronous tasks
        self._max_tasks = max_tasks
        self.semaphore = asyncio.Semaphore(max_tasks)

        # 限制最大连接数 / Limit the maximum number of connections
        self._max_connections = max_connections
        self.limits = httpx.Limits(max_connections=max_connections)

        # 业务逻辑重试次数 / Business logic retry count
        self._max_retries = max_retries
        # 底层连接重试次数 / Underlying connection retry count
        self.atransport = httpx.AsyncHTTPTransport(retries=max_retries)

        # 超时等待时间 / Timeout waiting time
        self._timeout = timeout
        self.timeout = httpx.Timeout(timeout)
        # 异步客户端 / Asynchronous http_client
        self.aclient = httpx.AsyncClient(
            headers=self.client_headers,
            proxies=self.proxies,
            timeout=self.timeout,
            limits=self.limits,
            transport=self.atransport,
        )

    async def fetch_response(self, endpoint: str) -> Response:
        """获取数据 (Get data)

        Args:
            endpoint (str): 接口地址 (Endpoint URL)

        Returns:
            Response: 原始响应对象 (Raw response object)
        """
        return await self.get_fetch_data(f"{self.base_url}{endpoint}")

    async def fetch_get_json(self, endpoint: str) -> Union[dict, List[Any]]:
        """获取 JSON 数据 (Get JSON data)

        Args:
            endpoint (str): 接口地址 (Endpoint URL)

        Returns:
            dict: 解析后的JSON数据 (Parsed JSON data)
        """
        response = await self.get_fetch_data(f"{self.base_url}{endpoint}")
        return self.parse_json(response)

    async def fetch_post_json(self, endpoint: str, params: dict = {}, data=None) -> Union[dict, List[Any]]:
        """获取 JSON 数据 (Post JSON data)

        Args:
            endpoint (str): 接口地址 (Endpoint URL)

        Returns:
            dict: 解析后的JSON数据 (Parsed JSON data)
        """
        response = await self.post_fetch_data(f"{self.base_url}{endpoint}", params, data)
        return self.parse_json(response)

    def parse_json(self, response: Response) -> Union[dict, List[Any]]:
        """解析 JSON 数据 (Parse JSON data)"""

        return response.json()

    async def get_fetch_data(self, url: str):
        """
        获取GET端点数据 (Get GET endpoint data)

        Args:
            url (str): 端点URL (Endpoint URL)

        Returns:
            response: 响应内容 (Response content)
        """
        for attempt in range(self._max_retries):
            try:
                response = await self.aclient.get(url, follow_redirects=True)
                if not response.text.strip() or not response.content:
                    error_message = "第 {0} 次响应内容为空, 状态码: {1}, URL:{2}".format(attempt + 1,
                                                                                         response.status_code,
                                                                                         response.url)

                    logger.warning(error_message)

                    if attempt == self._max_retries - 1:
                        raise APIRetryExhaustedError(
                            "获取端点数据失败, 次数达到上限"
                        )

                    await asyncio.sleep(self._timeout)
                    continue

                # logger.info("响应状态码: {0}".format(response.status_code))
                response.raise_for_status()
                return response

            except httpx.RequestError:
                raise APIConnectionError("连接端点失败，检查网络环境或代理：{0} 代理：{1} 类名：{2}"
                                         .format(url, self.proxies, self.__class__.__name__)
                                         )

            except httpx.HTTPStatusError as http_error:
                self.handle_http_status_error(http_error, url, attempt + 1)

            except APIError as e:
                e.display_error()

    async def post_fetch_data(self, url: str, params: dict = {}, data=None):
        """
        获取POST端点数据 (Get POST endpoint data)

        Args:
            url (str): 端点URL (Endpoint URL)
            params (dict): POST请求参数 (POST request parameters)

        Returns:
            response: 响应内容 (Response content)
        """
        for attempt in range(self._max_retries):
            try:
                response = await self.aclient.post(
                    url,
                    json=None if not params else dict(params),
                    data=None if not data else data,
                    follow_redirects=True
                )
                if not response.text.strip() or not response.content:
                    error_message = "第 {0} 次响应内容为空, 状态码: {1}, URL:{2}".format(attempt + 1,
                                                                                         response.status_code,
                                                                                         response.url)

                    logger.warning(error_message)

                    if attempt == self._max_retries - 1:
                        raise APIRetryExhaustedError(
                            "获取端点数据失败, 次数达到上限"
                        )

                    await asyncio.sleep(self._timeout)
                    continue

                # logger.info("响应状态码: {0}".format(response.status_code))
                response.raise_for_status()
                return response

            except httpx.RequestError:
                raise APIConnectionError(
                    "连接端点失败，检查网络环境或代理：{0} 代理：{1} 类名：{2}".format(url, self.proxies,
                                                                                   self.__class__.__name__)
                )

            except httpx.HTTPStatusError as http_error:
                self.handle_http_status_error(http_error, url, attempt + 1)

            except APIError as e:
                e.display_error()

    async def head_fetch_data(self, url: str):
        """
        获取HEAD端点数据 (Get HEAD endpoint data)

        Args:
            url (str): 端点URL (Endpoint URL)

        Returns:
            response: 响应内容 (Response content)
        """
        try:
            response = await self.aclient.head(url)
            # logger.info("响应状态码: {0}".format(response.status_code))
            response.raise_for_status()
            return response

        except httpx.RequestError:
            raise APIConnectionError("连接端点失败，检查网络环境或代理：{0} 代理：{1} 类名：{2}".format(
                url, self.proxies, self.__class__.__name__
            )
            )

        except httpx.HTTPStatusError as http_error:
            self.handle_http_status_error(http_error, url, 1)

        except APIError as e:
            e.display_error()

    def handle_http_status_error(self, http_error, url: str, attempt):
        """
        处理HTTP状态错误 (Handle HTTP status error)

        Args:
            http_error: HTTP状态错误 (HTTP status error)
            url: 端点URL (Endpoint URL)
            attempt: 尝试次数 (Number of attempts)
        Raises:
            APIConnectionError: 连接端点失败 (Failed to connect to endpoint)
            APIResponseError: 响应错误 (Response error)
            APIUnavailableError: 服务不可用 (Service unavailable)
            APINotFoundError: 端点不存在 (Endpoint does not exist)
            APITimeoutError: 连接超时 (Connection timeout)
            APIUnauthorizedError: 未授权 (Unauthorized)
            APIRateLimitError: 请求频率过高 (Request frequency is too high)
            APIRetryExhaustedError: 重试次数达到上限 (The number of retries has reached the upper limit)
        """
        response = getattr(http_error, "response", None)
        response_text = getattr(response, "text", None)
        status_code = getattr(response, "status_code", None)

        if response is None or status_code is None:
            logger.error("HTTP状态错误: {0}, URL: {1}, 尝试次数: {2}".format(
                http_error, url, attempt
            )
            )
            raise APIResponseError(f"处理HTTP错误时遇到意外情况: {http_error}")

        if status_code == 302:
            pass
        elif status_code == 404:
            raise APINotFoundError(f"HTTP Status Code {status_code}, check your URL")
        elif status_code == 503:
            raise APIUnavailableError(f"HTTP Status Code {status_code}")
        elif status_code == 408:
            raise APITimeoutError(f"HTTP Status Code {status_code}")
        elif status_code == 401:
            raise APIUnauthorizedError(f"HTTP Status Code {status_code}, check your API key")
        elif status_code == 429:
            raise APIRateLimitError(f"HTTP Status Code {status_code}")
        else:
            logger.error("HTTP状态错误: {0}, URL: {1}, 尝试次数: {2}".format(
                status_code, url, attempt
            )
            )
            raise APIResponseError(f"\n程序出现异常，请检查错误信息。 | An error occurred in the program, please check the error message."
                                   f"\nHTTP Status Code: {status_code}"
                                   f"\nResponse: {response_text}"
                                   f"\nURL: {url}")

    async def close(self):
        await self.aclient.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclient.aclose()
