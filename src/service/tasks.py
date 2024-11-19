"""
任务模块 实际处理逻辑

"""
from pathlib import Path
from typing import List

from loguru import logger

from src.dao.image import image_info_dao
from src.models.db.image import ImageInfo
from src.models.requests.tasks import StartTaskParams
from src.service.image import image_service


class TaskService:
    """
    具体逻辑实现

    """

    @staticmethod
    def analysis_image(image_dir_list: List[str], is_refresh: bool):
        """
        分析图片
        获取其MD5值，长宽，以及是否nsfw等信息

        :return:
        """
        logger.info('Start analysis images.')
        exist_list = image_info_dao.get_list()
        exist_map = {img.full_path: img for img in exist_list}

        for image_dir in image_dir_list:
            path = Path(image_dir)
            # 错误路径则直接跳过
            if not path.is_dir():
                logger.error('The directory {} is not a directory.', image_dir)
                continue
            logger.info('Deal with {}.', image_dir)
            to_add_list, to_update_list = image_service.generate_image_info(dir_path=path, exist_map=exist_map, is_refresh=is_refresh)
            image_info_dao.insert_bulk(models=to_add_list, batch_size=10000)
            image_info_dao.update_bulk(t=ImageInfo, models=to_update_list, batch_size=10000)

        logger.info('Finish analysis images.')


def start_analysis(params: StartTaskParams):
    """
    开启图片分析任务

    :return:
    """
    logger.info('The image sources are: {}', params.image_dir_list)
    TaskService.analysis_image(image_dir_list=params.image_dir_list, is_refresh=params.is_refresh)
