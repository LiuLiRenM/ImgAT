"""
图片相关 数据库操作类

"""
from typing import List

from src.dao import BaseDAO
from src.models.db.image import ImageInfo, ImageFeature


class ImageInfoDAO(BaseDAO[ImageInfo]):
    """
    image_info表 数据库操作类

    """

    def get_list(self) -> List[ImageInfo]:
        """
        获取全库数据

        :return:
        """
        return self.session.query(ImageInfo).all()


class ImageFeatureDAO(BaseDAO[ImageFeature]):
    """
    image_feature表 数据库操作类

    """


image_info_dao = ImageInfoDAO()
image_feature_dao = ImageFeatureDAO()
