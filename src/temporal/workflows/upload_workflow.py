"""
上传图片到OBS的工作流

"""
from datetime import timedelta

from loguru import logger
from temporalio import workflow

from src.models.requests import TemporalParams
from src.temporal.activities.upload_activity import Upload2ObsActivity


@workflow.defn
class Upload2ObsWorkFlow:
    """
    上传图片到OBS的工作流

    """

    @workflow.run
    async def run(self, params: TemporalParams) -> str:
        """

        :param params:
        :return:
        """
        result = await workflow.execute_activity(
            Upload2ObsActivity.upload_to_obs,
            params,
            start_to_close_timeout=timedelta(seconds=10)
        )
        logger.info('Upload result: {}', result)
        return result
