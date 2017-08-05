# -*- coding: utf-8 -*-
from spider_app.gee_spider import GeeSpider
import time
import json
import requests
import os
import sched
import threading
import uuid
import re


def get_task():
    task_url = 'http://newdaas.bidata.com.cn/srs/newdaasBRTaskService/getNewTask'
    content = json.loads(
        requests.get(task_url).text
    )
    if content['IsNull']:
        print('IsNull is True')
        return
    keyword = content['DATA']['KEY_WORD']
    task_id = content['DATA']['TASK_ID']
    print('the keyword is', keyword)
    gs = GeeSpider(keyword, task_id)
    gs.run()


def get_default_test():
    # keyword = '北京中数智汇科技股份有限公司'深圳市华银澳捷科技有限公司 911100007693890511 厦门喵小米生态科技有限公司
    # keyword = '北京中数智汇科技股份有限公司' 天柱县凤城街道新和村种养殖专业合作社 91330201316970505F
    for i in range(1):
        keyword = '91130605MA07WGLR6D'
        task_id = str(uuid.uuid1())
        gs = GeeSpider(keyword, task_id)
        gs.run()


def get_task_txt_test():
    load_txt = []
    with open('/Users/chinadaas/Desktop/C_WB_20170619.txt') as f:
        for line in f:
            line = re.sub('\n', '', line)
            load_txt.append(line)

    for load in load_txt:
        keyword = load
        task_id = str(uuid.uuid1())
        gs = GeeSpider(keyword, task_id)
        gs.run()
        time.sleep(5)


def track_generate():
    for i in range(100):
        success_count = 0
        gs = GeeSpider('小米科技', '')
        # content_dic = gs.run()
        time.sleep(1)
        success_count += gs.count
        print('current i is ', i)
        print('current successed count is ', str(success_count / 100))
    print('the success count is', success_count)


def heart_connect(cmd, inc):
    print('========post to services =============!')
    schedule.enter(inc, 0, heart_connect, (cmd, inc))


def do_task(cmd, inc):
    get_task()
    schedule.enter(inc, 0, do_task, (cmd, inc))


def crwaler_thread_func():
    schedule.enter(5, 0, do_task, ('crwaler_connect', 5))
    schedule.run()


def heart_thread_func():
    schedule.enter(5, 0, heart_connect, ('heart_connect', 5))
    schedule.run()


if __name__ == '__main__':
    # 任务访问地址：http://newdaas.bidata.com.cn/srs/newdaasBRTaskService/getNewTask
    # 主方法
    schedule = sched.scheduler(time.time, time.sleep)

    '''
    # 主程序
    thread_list = []
    heart_thread = threading.Thread(target=heart_thread_func)
    thread_list.append(heart_thread)
    crwaler_thread = threading.Thread(target=crwaler_thread_func)
    thread_list.append(crwaler_thread)

    for t in thread_list:
        t.setDaemon(True)
        t.start()
    t.join()  # success_count = 0
    '''
    # 正式测试
    # get_task()
    # 循环测试
    # get_task_txt_test()
    # 指定测试
    get_default_test()
