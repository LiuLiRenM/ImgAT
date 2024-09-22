"""
数据库操作类

"""
from typing import TypeVar, Generic, List

from loguru import logger

from src.models.db import Base, session
from src.utils.date_util import DateUtil
from src.utils.id_util import IdUtil

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    """
    基类

    """

    def __init__(self):
        self.session = session

        self.create_time_field: str = 'created_time'
        self.update_time_field: str = 'updated_time'

    def _set_default_field(self, model: T):
        """
        设置默认字段值

        :param model:
        :return:
        """
        primary_key = model.__table__.primary_key.columns.values()[0].name
        # 生成主键id
        setattr(model, primary_key, IdUtil.get_id())
        # 有创建时间字段的话 写入当前时间
        if hasattr(model, self.create_time_field):
            setattr(model, self.create_time_field, DateUtil.get_now())

    @staticmethod
    def chunks(lst: List[T], n: int) -> List[T]:
        """
        按照指定的步长n来产生子列表

        :return:
        """
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def insert_one(self, model: T) -> T:
        """
        保存一条数据到数据库

        :param model:
        :return:
        """
        self._set_default_field(model=model)
        try:
            self.session.add(model)
            self.session.commit()
            return model
        except Exception as e:
            logger.error('Save error: {}', e)
            self.session.rollback()

    def insert_bulk(self, models: List[T], batch_size: int = 1000) -> List[T]:
        """
        批量保存

        :param models: 要保持的数据列表
        :param batch_size: 每次保存的数量
        :return:
        """
        for model in models:
            self._set_default_field(model=model)
        try:
            if len(models) < batch_size:
                self.session.add_all(models)
            else:
                for sub_list in self.chunks(lst=models, n=batch_size):
                    self.session.add_all(sub_list)
            self.session.commit()
            return models
        except Exception as e:
            logger.error('Bulk save error: {}', e)
            self.session.rollback()
