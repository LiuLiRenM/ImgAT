"""
图片信息处理工作流

"""
from datetime import timedelta

from loguru import logger
from temporalio import workflow
from temporalio.workflow import ParentClosePolicy

from src.models.requests import TemporalParams
from src.temporal.activities.img_info_activity import ImgInfoActivity
from src.temporal.workflows.upload_workflow import Upload2ObsWorkFlow


@workflow.defn
class ImgInfoWorkflow:
    """
    图片信息处理工作流

    """

    @workflow.run
    async def run(self, params: TemporalParams) -> str:
        result = await workflow.execute_activity(
            ImgInfoActivity.deal_img_info,
            params,
            start_to_close_timeout=timedelta(minutes=10)
        )
        logger.info('Deal img info result: {}', result)
        upload_result = await workflow.execute_child_workflow(Upload2ObsWorkFlow.run, params,
                                                              id='upload_to_obs',
                                                              parent_close_policy=ParentClosePolicy.ABANDON)
        logger.info('Upload img info result: {}', upload_result)
        return upload_result
