class APIError(Exception):
    """
    基本API异常类，其他API异常都会继承这个类

    Base API exception class, all other API exceptions will inherit this class
    """

    def __init__(self, status_code=None):
        self.status_code = status_code
        print(
            "程序出现异常，请检查错误信息。 | An error occurred in the program, please check the error message."
        )

    def display_error(self):
        """
        显示错误信息和状态码（如果有的话）

        Display the error message and status code (if any)
        """
        return f"Error: {self.args[0]}." + (
            f" Status Code: {self.status_code}." if self.status_code else ""
        )


class APIConnectionError(APIError):
    """
    当与API的连接出现问题时抛出

    Raised when there is a problem connecting to the API
    """

    def display_error(self):
        return f"API Connection Error: {self.args[0]}."


class APIUnavailableError(APIError):
    """
    当API服务不可用时抛出，例如维护或超时

    Raised when the API service is unavailable, such as maintenance or timeout
    """

    def display_error(self):
        return f"API Unavailable Error: {self.args[0]}."


class APINotFoundError(APIError):
    """
    当API端点不存在时抛出

    Raised when the API endpoint does not exist
    """

    def display_error(self):
        return f"API Not Found Error: {self.args[0]}."


class APIResponseError(APIError):
    """
    当API返回的响应与预期不符时抛出

    Raised when the response returned by the API does not match the expected
    """

    def display_error(self):
        return f"API Response Error: {self.args[0]}."


class APIRateLimitError(APIError):
    """
    当达到API的请求速率限制时抛出

    Raised when the request rate limit of the API is reached
    """

    def display_error(self):
        return f"API Rate Limit Error: {self.args[0]}."


class APITimeoutError(APIError):
    """
    当API请求超时时抛出

Raised when the API request times out
    """

    def display_error(self):
        return f"API Timeout Error: {self.args[0]}."


class APIUnauthorizedError(APIError):
    """
    当API请求由于授权失败而被拒绝时抛出

    Raised when an API request is denied due to authorization failure
    """

    def display_error(self):
        return f"API Unauthorized Error: {self.args[0]}."


class APIRetryExhaustedError(APIError):
    """
    当API请求重试次数用尽时抛出

    Raised when the API request retry count is exhausted
    """

    def display_error(self):
        return f"API Retry Exhausted Error: {self.args[0]}."
