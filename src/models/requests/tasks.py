"""
任务模块 相关入参类

"""
from typing import List

from pydantic import BaseModel


class StartTaskParams(BaseModel):
    """
    启动任务入参

    """
    # 图片目录列表 支持多个目录
    image_dir_list: List[str]
