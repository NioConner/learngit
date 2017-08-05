# -*- coding: utf-8 -*-

from sqlalchemy import Integer, Column, create_engine, String
from sqlalchemy.orm import sessionmaker
from db.db_init import Base
from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base()


def model_init():
    # engine = create_engine('mysql+pymysql://root:wangyanyan@192.168.205.41/app_spider?charset=utf8', encoding='utf-8',
    #                        echo=True)
    engine = create_engine('mysql+pymysql://root:123456@localhost/app_spider?charset=utf8', encoding='utf-8', echo=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    sess = session()
    sess.close()


class PcCatchLog(Base):
    __tablename__ = 'PC_CAT_LOG'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    # 抓取关键词
    KEYWORD = Column(String(100))
    # 批次号
    BATCH_ID = Column(String(20))
    # 列表里面公司的名字
    NAME = Column(String(200))
    # 地址链接
    LINK = Column(String(400))
    # 抓取状态
    IS_OK = Column(String(10))
    # 抓取时间
    CATDATE = Column(String(20))
    # 是否已被后台采集
    IS_SYNC = Column(Integer)
    # UUID
    TASK_ID = Column(String(50))


if __name__ == '__main__':
    model_init()
