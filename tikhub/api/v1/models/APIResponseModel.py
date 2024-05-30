import datetime
from typing import Any, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# 定义基础响应模型
class ResponseModel(BaseModel):
    code: int = Field(default=200, description="HTTP status code | HTTP状态码")
    router: str = Field(default="", description="The endpoint that generated this response | 生成此响应的端点")
    params: Any = Field(default={}, description="The parameters used in the request | 请求中使用的参数")
    data: Optional[Any] = Field(default=None, description="The response data | 响应数据")


# 定义错误响应模型
class ErrorResponseModel(BaseModel):
    code: int = Field(default=400, description="HTTP status code/HTTP状态码")
    message: str = Field(
        default="An error occurred, your account will not be charged for this request due to the error. | 服务器发生错误，您的帐户不会因此请求而被收费。",
        description="Error message | 错误消息")
    support: str = Field(
        default="Please contact us on Discord: https://discord.gg/aMEAS8Xsvz | 请在Discord上联系我们：https://discord.gg/aMEAS8Xsvz",
        description="Support message | 支持消息")
    time: str = Field(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                      description="The time the error occurred | 发生错误的时间")
    router: str = Field(default="", description="The endpoint that generated this response | 生成此响应的端点")
    params: dict = Field(default={}, description="The parameters used in the request | 请求中使用的参数")


# 定义会话数据模型
class SessionData(BaseModel):
    session_name: str
    scopes: list
    created_at: datetime.datetime
    expires_at: Optional[datetime.datetime]
    status: int


# 定义用户数据模型
class UserData(BaseModel):
    email: str
    balance: float
    free_credit: float
    email_verified: bool
    account_disabled: bool
    is_active: bool


# 定义用户信息响应模型
class UserInfoResponseModel(BaseModel):
    code: int = Field(default=200, description="HTTP status code | HTTP状态码")
    router: str = Field(default="", description="The endpoint that generated this response | 生成此响应的端点")
    session_data: SessionData
    user_data: UserData


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
