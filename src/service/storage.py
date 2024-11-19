"""
S3功能
使用minio实现

"""
import json
from pathlib import Path
from typing import TypeVar

from loguru import logger
from minio import Minio

from src.models.responses.storage import DetectorResult

T = TypeVar('T')


class StorageService:
    """
    文件存储服务-minio

    """

    def __init__(self):
        self.region_name: str = 'eu-central-2'
        self.access_key_id: str = 'minio'
        self.secret_access_key: str = 'minio123'
        self.bucket_name: str = 'engine'
        self.endpoint_url: str = 'localhost:9000'

        self.client = Minio(
            self.endpoint_url,
            access_key=self.access_key_id,
            secret_key=self.secret_access_key,
            region=self.region_name,
            secure=False
        )

        self._init_bucket()

    def _init_bucket(self):
        """
        初始化桶

        :return:
        """
        if not self.client.bucket_exists(self.bucket_name):
            logger.info('Created bucket: {}', self.bucket_name)
            self.client.make_bucket(self.bucket_name)
        else:
            logger.info('Bucket already exists: {}', self.bucket_name)

    def upload(self, upload_file: Path, object_name: str):
        """
        上传文件

        :param object_name: S3对象名称
        :param upload_file: 要上传的文件
        :return:
        """
        obj_name = object_name + upload_file.suffix
        self.client.fput_object(bucket_name=self.bucket_name, object_name=obj_name,
                                file_path=upload_file.as_posix())
        logger.info('{} successfully uploaded as object to bucket {}, object name: {}',
                    upload_file.as_posix(), self.bucket_name, obj_name)

    def get_obj_content(self, obj_name: str) -> bytes:
        """
        获取S3文件对象内容

        :param obj_name: 对象名称
        :return:
        """
        with self.client.get_object(bucket_name=self.bucket_name, object_name=obj_name) as response:
            logger.info('Get object {} from bucket {}.', obj_name, self.bucket_name)
            return response.data

    def bytes_to_obj(self, t: T, obj_name: str) -> T:
        """
        将S3文件内容转为自定义对象

        :param obj_name:
        :param t:
        :return:
        """
        try:
            obj_content = self.get_obj_content(obj_name=obj_name)
            obj_str = obj_content.decode('utf8')
            return t(**json.loads(obj_str))
        except Exception as e:
            logger.error('Failed, error: {}', e)


storage_service = StorageService()

if __name__ == '__main__':
    # storage.upload(Path(r'D:\Data\Wallpaper\20201017141840276.jpg'))
    logger.info('Started')
    s = storage_service.bytes_to_obj(obj_name='1faf4685-3a69-4d5c-a74c-21a10d1e0e63.jpg', t=DetectorResult)
    print(s)
