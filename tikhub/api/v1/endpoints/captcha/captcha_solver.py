# 导入API SDK Client
from tikhub.client.api_client import APIClient

@router.get("/test", response_model=ResponseModel, summary="测试接口")
async def test(request: Request):
    # 测试函数
    data = {"message": "即将上线，敬请期待 | Coming soon, stay tuned"}
    return ResponseModel(code=200,
                         router=request.url.path,
                         params=dict(request.query_params),
                         data=data)

