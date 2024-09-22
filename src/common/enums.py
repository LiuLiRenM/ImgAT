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
    FEMALE_GENITALIA_COVERED = (1, 'FEMALE_GENITALIA_COVERED')
    BUTTOCKS_EXPOSED = (2, 'BUTTOCKS_EXPOSED')
    FEMALE_BREAST_EXPOSED = (3, 'FEMALE_BREAST_EXPOSED')
    FEMALE_GENITALIA_EXPOSED = (4, 'FEMALE_GENITALIA_EXPOSED')
    MALE_BREAST_EXPOSED = (5, 'MALE_BREAST_EXPOSED')
    ANUS_EXPOSED = (6, 'ANUS_EXPOSED')
    MALE_GENITALIA_EXPOSED = (7, 'MALE_GENITALIA_EXPOSED')
    ANUS_COVERED = (8, 'ANUS_COVERED')
    FEMALE_BREAST_COVERED = (9, 'FEMALE_BREAST_COVERED')
    BUTTOCKS_COVERED = (10, 'BUTTOCKS_COVERED')

    @classmethod
    def is_exist(cls, name: str) -> bool:
        """
        判断传进来的name是否是这个枚举中的一个元素

        :param name: 枚举名称
        :return:
        """
        return name in cls.__members__
