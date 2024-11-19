"""
任务接口类

"""
from fastapi import APIRouter, BackgroundTasks
from loguru import logger

from src.models.requests.tasks import StartTaskParams, CallbackParams
from src.service.tasks import start_analysis

task_router = APIRouter()


@task_router.post('', summary='启动任务')
def start_task(params: StartTaskParams, background_tasks: BackgroundTasks):
    """
    启动任务

    :param background_tasks: fastapi.background.BackgroundTasks
    :param params: 启动入参
    :return:
    """
    logger.info('Turn on background tasks to perform image analysis tasks')
    background_tasks.add_task(start_analysis, params)


@task_router.patch('/test')
def t_test(params: CallbackParams):
    logger.info('Callback params: {}', params.model_dump())
    return dict()
