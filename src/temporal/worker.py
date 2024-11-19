"""
启动Worker

"""
import asyncio

from loguru import logger
from temporalio.client import Client
from temporalio.worker import Worker

from src.models.requests import TemporalParams
from src.temporal.workflows.img_info_workflow import ImgInfoWorkflow
from src.temporal.workflows.upload_workflow import Upload2ObsWorkFlow


async def main():
    client = await Client.connect('localhost:7233')
    async with Worker(client, task_queue='img_task_queue',
                      workflows=[ImgInfoWorkflow, Upload2ObsWorkFlow]):
        params = TemporalParams(test_name='lyo')
        result = await client.execute_workflow(
            ImgInfoWorkflow.run,
            params,
            id='deal_img_info',
            task_queue='img_task_queue',
        )
        logger.info('Finished. Result: {}', result)


if __name__ == '__main__':
    asyncio.run(main())
