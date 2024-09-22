"""
初始化路由

"""
from fastapi import APIRouter

from src.api.tasks import task_router

router = APIRouter()

router.include_router(task_router, prefix='/tasks')
