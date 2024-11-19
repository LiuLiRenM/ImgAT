"""
storage模块返回值

"""
from typing import Dict

from pydantic import BaseModel

from src.common.enums import PredCategories, SubPredCategories


class DetectorResult(BaseModel):
    """
    image-nsfw-detector-service运行结果

    """
    prediction_category: PredCategories
    prediction_subcategory: SubPredCategories
    scores_dict_cat: Dict[str, float]
    scores_dict_sub_cat: Dict[str, float]
