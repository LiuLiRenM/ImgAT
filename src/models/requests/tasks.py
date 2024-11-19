"""
任务模块 相关入参类

"""
from typing import List, Optional

from pydantic import BaseModel

from src.common.enums import TaskStatus


class StartTaskParams(BaseModel):
    """
    启动任务入参

    """
    # 图片目录列表 支持多个目录
    image_dir_list: List[str]
    # 是否更新图片信息
    is_refresh: bool


class CallbackParams(BaseModel):
    """
    回调接口入参

    """
    service: Optional[str] = None
    url: Optional[str] = None
    data_out: List[str]
    status: TaskStatus
