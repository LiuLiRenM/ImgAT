"""
上传文件到OBS的Activity

"""
from loguru import logger
from temporalio import activity

from src.models.requests import TemporalParams


class Upload2ObsActivity:
    """
    上传文件到OBS的Activity

    """

    @activity.defn(name='upload_to_obs')
    async def upload_to_obs(self, params: TemporalParams):
        """
        上传图片到obs

        :param params:
        :return:
        """
        logger.info('Upload img to OBS, params: {}', params.test_name)
        return 'Upload img to OBS {}'.format(params.test_name)
