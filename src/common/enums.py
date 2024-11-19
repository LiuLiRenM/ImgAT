"""
枚举类定义

"""
from enum import Enum


class FeatureType(Enum):
    """
    特征值类型（使用什么方法生成的特征值）

    """
    MD5 = 1


class NsfwType(Enum):
    """
    识别到的NSFW类型

    """
    BUTTOCKS_EXPOSED = (1, 'BUTTOCKS_EXPOSED')
    FEMALE_BREAST_EXPOSED = (2, 'FEMALE_BREAST_EXPOSED')
    FEMALE_GENITALIA_EXPOSED = (3, 'FEMALE_GENITALIA_EXPOSED')
    MALE_BREAST_EXPOSED = (4, 'MALE_BREAST_EXPOSED')
    ANUS_EXPOSED = (5, 'ANUS_EXPOSED')
    MALE_GENITALIA_EXPOSED = (6, 'MALE_GENITALIA_EXPOSED')

    @classmethod
    def is_exist(cls, name: str) -> bool:
        """
        判断传进来的name是否是这个枚举中的一个元素

        :param name: 枚举名称
        :return:
        """
        return name in cls.__members__


class TaskStatus(str, Enum):
    """
    任务状态类型

    """
    PENDING = "pending"
    FETCHING = "fetching"
    PROCESSING = "processing"
    SAVING = "saving"
    FINISHED = "finished"
    ERROR = "error"
    SCHEDULED = "scheduled"
    SKIPPED = "skipped"
    UNAVAILABLE = "unavailable"


class PredCategories(str, Enum):
    """
    预测类别

    """
    NSFW = 'nsfw'
    SAFE = 'safe'


class SubPredCategories(str, Enum):
    """
    预测类别的子类

    """
    NSFW_CARTOON = 'nsfw_cartoon'
    NSFW_NUDITY = 'nsfw_nudity'
    NSFW_PORN = 'nsfw_porn'
    NSFW_SUGGESTIVE = 'nsfw_suggestive'
    SAFE_CARTOON = 'safe_cartoon'
    SAFE_GENERAL = 'safe_general'
    SAFE_PERSON = 'safe_person'
