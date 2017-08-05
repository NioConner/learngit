# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import cx_Oracle
import os

'''
将数据库通信单独提取，用于规避运行时候的循环import
'''


def write_to_sql(arr):
    pass


class OrclConnection(object):
    def __init__(self, usr, pwd, host, port, sid):
        self.usr = usr
        self.pwd = pwd
        self.host = host
        self.port = port
        self.sid = sid
        self.dsn = self.dsn()
        self.con = self.connection()

    def dsn(self):
        dsn = cx_Oracle.makedsn(self.host, self.port, self.sid)
        return dsn

    def connection(self):
        con = cx_Oracle.connect(self.usr, self.pwd, self.dsn)
        return con

    def get_orcl_cursor(self):
        orcl_c = self.con.cursor()
        return orcl_c

    def re_get_cursor(self):
        self.con.close()
        orcl_c = self.get_orcl_cursor()
        orcl_c.close()
        self.dsn = self.dsn()
        self.con = self.connection()
        orcl_c = self.get_orcl_cursor()
        return orcl_c


Base = declarative_base()
engine = create_engine('mysql+pymysql://root:123456@localhost/app_spider?charset=utf8', encoding='utf-8', echo=True)
# engine = create_engine('mysql+pymysql://root:wangyanyan@192.168.205.41/app_spider?charset=utf8', encoding='utf-8',
#                        echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
usr = 'NEWDAAS'
pwd = 'NEWDAAS2017'
host = '192.168.205.30'
port = '1521'
sid = 'orcl'

orcl_maker = OrclConnection(usr, pwd, host, port, sid)
