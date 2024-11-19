"""
图片信息处理的Activity

"""
from loguru import logger
from temporalio import activity

from src.models.requests import TemporalParams


class ImgInfoActivity:

    @activity.defn(name='deal_img_info')
    async def deal_img_info(self, params: TemporalParams) -> str:
        logger.info('Start deal img info, params: {}', params.test_name)
        return 'Deal img info {}'.format(params.test_name)
