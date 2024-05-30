from pydantic import BaseModel, Field
from typing import List


# 列表作品
class URL_List(BaseModel):
    urls: List[str] = [
        "https://test.example.com/xxxxx/",
        "https://test.example.com/yyyyy/",
        "https://test.example.com/zzzzz/"
    ]


# abogus API响应模型
class A_Bogus_Parameters(BaseModel):
    url: str = Field("https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&enable_history=1&keyword=%E4%B8%AD%E5%8D%8E%E5%A8%98&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=7346905902554844468&offset=0&count=15&need_filter_settings=1&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platform=Win32&browser_name=Firefox&browser_version=124.0&browser_online=true&engine_name=Gecko&engine_version=124.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=&platform=PC&webid=7348962975497324070&msToken=YCTVM6YGmjFdIpQAN9ykXLBXiSiuHdZkOkEQWTeqVOHBEPmOcM0lNwE0Kd9vgHPMPigSndZDHfAq9k-6lDmH3Jqz6mHHxmn-BzQjmLMIfLIPgirgnOixM9x4PwgcNQ%3D%3D",
                     description='url，需要使用urlencode(data, safe="*")进行编码')

    data: str = Field("", description='body，需要使用urlencode(data, safe="*")进行编码')

    user_agent: str = Field(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        description='user-agent')
    index_0: int = Field(0, description='加密明文列表的第一个值，无特殊要求，默认为0')
    index_1: int = Field(1, description='加密明文列表的第一个值，无特殊要求，默认为1')
    index_2: int = Field(14, description='加密明文列表的第一个值，无特殊要求，默认为14')




