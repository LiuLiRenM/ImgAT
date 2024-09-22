"""
图片相关 数据库操作类

"""
from src.dao import BaseDAO
from src.models.db.image import ImageInfo, ImageFeature


class ImageInfoDAO(BaseDAO[ImageInfo]):
    """
    image_info表 数据库操作类

    """

    def get_full_path_list(self):
        """
        获取已入库的所有文件的文件路径

        :return:
        """
        result = self.session.query(ImageInfo.full_path).all()
        exist_full_path_list = list()
        for item in result:
            exist_full_path_list.append(item[0])
        return exist_full_path_list


class ImageFeatureDAO(BaseDAO[ImageFeature]):
    """
    image_feature表 数据库操作类

    """


image_info_dao = ImageInfoDAO()
image_feature_dao = ImageFeatureDAO()
