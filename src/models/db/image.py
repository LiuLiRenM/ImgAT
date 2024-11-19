"""
图片相关表的实体类

"""
from sqlalchemy import Column, String, Boolean, DateTime, Integer, BigInteger, SmallInteger, JSON

from src.models.db import Base


class ImageInfo(Base):
    """
    图片信息表实体类

    """
    __tablename__ = 'image_info'

    id = Column(BigInteger, primary_key=True, index=True, comment='主键id')
    full_path = Column(String(500), unique=True, nullable=False, comment='图片所在的绝对路径')
    name = Column(String(500), nullable=False, comment='图片名称')
    is_nsfw = Column(Boolean, default=0, nullable=False, comment='是否是NSFW图片，0：否，1：是')
    nsfw_original_result = Column(JSON, nullable=False, comment='NSFW审查原始结果')
    width = Column(Integer, nullable=False, comment='图片宽度')
    height = Column(Integer, nullable=False, comment='图片长度')
    is_suit_as_wallpaper = Column(Boolean, default=0, comment='是否适合用作壁纸，0：否，1：是')
    hash_value = Column(String(32), nullable=False, comment='图片hash值')
    created_time = Column(DateTime, nullable=False, comment='创建时间')
    updated_time = Column(DateTime, comment='更新时间')
    is_deleted = Column(Boolean, default=0, nullable=False, comment='是否删除，0：否，1：是')


class ImageFeature(Base):
    """
    表image_features对应的SQLAlchemy实体类

    """
    __tablename__ = 'image_feature'

    id = Column(BigInteger, primary_key=True, index=True, comment='主键id')
    image_info_id = Column(BigInteger, comment='image_info表主键id')
    feature = Column(String(500), nullable=False, comment='图片特征值')
    feature_type = Column(SmallInteger, nullable=False, comment='特征值类型 1: MD5')
    created_time = Column(DateTime, nullable=False, comment='创建时间')
    updated_time = Column(DateTime, comment='更新时间')
    is_deleted = Column(Boolean, default='0', nullable=False, comment='是否删除，0：否，1：是')
