# -*- coding: utf-8 -*-
import re
import time
from db.db_init import db_session
from db.moudle import *
import uuid

first_query = {
    'start': 'select ba.BATCH_ID from C_WB_CM_BATCH ba WHERE ba.KWS_STATUS = 0 ORDER BY ba.BATCH_ID DESC',
    'start_up': 'UPDATE C_WB_CM_BATCH ba SET ba.KWS_STATUS = 1 WHERE ba.BATCH_ID ={}',
    'query': 'select kw.KWS_INFO,kw.KWS_TYPE from C_WB_CM_KEYWORDS kw  WHERE kw.BATCH_ID ={}',
    'end_up': 'UPDATE C_WB_CM_BATCH ba SET ba.KWS_STATUS = 3 WHERE ba.BATCH_ID = {}',
}

second_query = {
    'start': 'select ba.BATCH_ID from C_WB_CM_BATCH ba WHERE ba.KWS_STATUS = 3 and ba.BATCH_ID > {} '
             'ORDER BY ba.BATCH_ID DESC',
    'start_up': 'UPDATE C_WB_CM_BATCH ba SET ba.KWS_STATUS = 1 WHERE ba.BATCH_ID ={}',
    'query': 'select kw.KWS_INFO,kw.KWS_TYPE from C_WB_CM_KEYWORDS kw  WHERE kw.BATCH_ID ={}',
    'end_up': 'UPDATE C_WB_CM_BATCH ba SET ba.KWS_STATUS = 4 WHERE ba.BATCH_ID = {}',
}


def write_failed(kws, batch_id):
    ft = {
        'TASK_ID': str(uuid.uuid1()),
        'KEYWORD': kws,
        'CATDATE': str(time.strftime('%Y-%m-%d %H-%M-%S')),
        'BATCH_ID': batch_id,
        'IS_OK': 'bad'
    }
    data = [ft]
    try:
        db_session.execute(
            PcCatchLog.__table__.insert(), data
        )
        db_session.commit()
    except:
        print('commit failed')


def write_to_sql(data):
    print(type(data))
    # print(db_session)
    if len(data) == 0:
        return
    else:
        try:
            db_session.execute(
                PcCatchLog.__table__.insert(), data
            )
            db_session.commit()
        except:
            print('commit failed')


# 从oralce里面读取新的批次
def load_batch_id_list(orcl_maker):
    orcl_cursor = orcl_maker.get_orcl_cursor()
    test_sql = 'select ba.BATCH_ID from C_WB_CM_BATCH ba WHERE ba.BATCH_ID = {} '.format(
        str(20170629101647))
    # start = first_query['start']
    orcl_cursor.execute(test_sql)
    result = orcl_cursor.fetchall()
    load_l = []
    for r in result:
        temp = re.findall("\'(.+?)\'", str(r))[0]
        print(temp)
        load_l.append(temp)
    return load_l


def set_status(orcl_maker, batch_id, status='start', start_num=0):
    orcl_cursor = orcl_maker.get_orcl_cursor()
    if status == 'start':
        update = first_query['start_up'].format(str(batch_id))
    else:
        update = first_query['end_up'].format(str(batch_id))
    try:
        orcl_cursor.execute(update)
        orcl_cursor.connection.commit()
    except Exception as e:
        time.sleep(1)
        if start_num > 2:
            return
        else:
            time.sleep(1)
            start_num += 1
            print('orcl_cursor first sets C_WB_CM_BATCH failed!')
            set_status(orcl_maker, batch_id, start_num)


def load_keywords(orcl_maker, batch_id, query_num=0):
    orcl_cursor = orcl_maker.get_orcl_cursor()
    query_sql = first_query['query'].format(str(batch_id))
    try:
        kws_list = orcl_cursor.execute(query_sql).fetchall()
    except Exception as e:
        if query_num > 3:
            kws_list = []
            # return kws_list
        else:
            time.sleep(1)
            print('orcl_cursor catchs kws_list failed!')
            query_num += 1
            load_keywords(orcl_maker, batch_id, query_num)
            return
    return kws_list
