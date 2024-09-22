"""
NSFW元素审查工具类

"""
from typing import Dict, List

from nudenet import NudeDetector
from pydantic import BaseModel

from src.common.enums import NsfwType


class DetectResult(BaseModel):
    """
    探测结果

    """
    is_nsfw: bool
    # 最原始的结果
    original_result: List[Dict]


class NsfwUtil:
    """
    NSFW元素审查工具类

    """

    detector = NudeDetector()

    @staticmethod
    def detect(file_content: bytes) -> DetectResult:
        """
        审查

        :param file_content: 文件内容
        :return:
        """
        detect_result = NsfwUtil.detector.detect(file_content)
        is_nsfw = False
        for result in detect_result:
            is_nsfw = NsfwType.is_exist(name=result.get('class'))
            if is_nsfw:
                break
        return DetectResult(is_nsfw=is_nsfw, original_result=detect_result)
