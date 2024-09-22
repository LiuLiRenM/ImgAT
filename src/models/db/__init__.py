"""
初始化数据库

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:liuyaowen@localhost:3306/img_db?charset=utf8mb4'
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=3600, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

session = SessionLocal()
