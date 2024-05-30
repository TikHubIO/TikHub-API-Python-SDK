from fastapi import APIRouter, Query, Request, HTTPException  # 导入FastAPI组件
from app.api.v1.models.APIResponseModel import ResponseModel, ErrorResponseModel  # 导入响应模型

from crawlers.xiaohongshu.web_crawler import *

router = APIRouter()


@router.get("/test", response_model=ResponseModel, summary="测试接口")
async def test(request: Request):
    # 测试函数
    data = {"message": "即将上线，敬请期待 | Coming soon, stay tuned"}
    return ResponseModel(code=200,
                         router=request.url.path,
                         params=dict(request.query_params),
                         data=data)