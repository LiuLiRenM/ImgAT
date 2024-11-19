"""
请求入参

"""

from pydantic import BaseModel


class TemporalParams(BaseModel):
    test_name: str
