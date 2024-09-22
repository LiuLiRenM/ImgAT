"""
初始化FastAPI

"""

from fastapi import FastAPI

from src.api import router
from src.models.db import engine, Base
from src.utils.log_util import init_logging

# 创建表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 初始化日志
init_logging()

app.include_router(router=router, prefix='/img/backend/v1')
