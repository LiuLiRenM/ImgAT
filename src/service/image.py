"""
图片 具体逻辑实现处

"""
import warnings
from pathlib import Path
from typing import Optional, List

from PIL import Image
from PIL.Image import DecompressionBombWarning
from PIL.ImageFile import ImageFile
from loguru import logger
from tqdm import tqdm

from src.models.db.image import ImageInfo
from src.utils.file_util import FileUtil
from src.utils.nsfw_util import NsfwUtil

# 忽略DecompressionBombWarning警告
warnings.filterwarnings("ignore", category=DecompressionBombWarning)


class ImageService:
    """
    具体逻辑实现处

    """

    def __init__(self):
        self.tqdm_log_path: Path = Path(__file__).parent.parent / 'logs' / 'tqdm.log'

    @staticmethod
    def is_image(file_path: Path) -> ImageFile:
        """
        判断是否是图片

        :param file_path: 文件路径
        :return: 不是的话返回None
        """
        image = None
        try:
            image = Image.open(fp=file_path)
            return image
        except IOError:
            logger.error('The file {} not a image.', file_path.as_posix())
            return image

    def create_image_info(self, file_path: Path) -> Optional[ImageInfo]:
        """
        创建image_info记录

        :param file_path: 图片路径
        :return:
        """
        # 读取文件内容
        content = FileUtil.get_file_content(file_path=file_path)
        image_info_record = None
        image_file = self.is_image(file_path=file_path)
        # 判断是否是图片
        if image_file is None:
            logger.warning('The file is not an image. Path: {}', file_path.as_posix())
            return image_info_record
        image_info_record = ImageInfo()
        image_info_record.full_path = file_path.as_posix()
        image_info_record.name = file_path.name
        # 获取图片的长宽
        width, height = image_file.size
        image_info_record.width = width
        image_info_record.height = height
        # 生成MD5值
        image_info_record.hash_value = FileUtil.get_file_md5(file_content=content)
        detect_result = NsfwUtil.detect(file_content=content)
        image_info_record.is_nsfw = detect_result.is_nsfw
        image_info_record.nsfw_original_result = detect_result.original_result
        return image_info_record

    def generate_image_info(self, dir_path: Path, exist_full_path_list) -> List[ImageInfo]:
        """
        生成图片信息，MD5值，长宽等信息

        :param exist_full_path_list:
        :param dir_path: 图片所在路径
        :return:
        """
        record_list = list()
        pbar = tqdm(list(dir_path.rglob('*')), file=open(self.tqdm_log_path, 'a', encoding='utf-8'))
        for file_path in pbar:
            pbar.set_description('Processing file: {}'.format(file_path.as_posix()))
            if file_path.as_posix() in exist_full_path_list:
                logger.info('The file {} has been stored.', file_path.as_posix())
                continue
            record = self.create_image_info(file_path=file_path)
            if record is None:
                continue
            record_list.append(record)
        return record_list


image_service = ImageService()
