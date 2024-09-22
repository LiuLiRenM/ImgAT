"""
时间工具类

"""
from datetime import datetime

import pytz


class DateUtil:
    """
    时间工具类

    """
    # 时区定义
    timezone_str: str = 'Asia/Shanghai'

    @staticmethod
    def get_now() -> datetime:
        """
        获取带有时区信息的当前时间

        :return:
        """
        return datetime.now(tz=pytz.timezone(DateUtil.timezone_str))
