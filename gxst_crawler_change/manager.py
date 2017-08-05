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
    try:
        text = requests.get(task_url).text
        content = json.loads(text)
    except:
        print('newdaas get failed!')
        return
        # content = json.loads(
    # requests.get(task_url).text
    # )
    if content['IsNull']:
        print('IsNull is True')
        return
    keyword = content['DATA']['KEY_WORD']
    task_id = content['DATA']['TASK_ID']
    print('the keyword is', keyword)
    gs = GeeSpider(keyword, task_id)
    gs.run()
    time.sleep(3)


def track_generate():
    for i in range(100):
        success_count = 0
        gs = GeeSpider('小米科技', '')
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
    """
    制约因素（排除IP影响）：
    1、blacklist 和 invailed
    2、滑块验证失败需要重新重头请求
    """
    # 任务访问地址：http://newdaas.bidata.com.cn/srs/newdaasBRTaskService/getNewTask
    # 主方法
    schedule = sched.scheduler(time.time, time.sleep)
    # 主程序
    thread_list = []
    heart_thread = threading.Thread(target=heart_thread_func)
    thread_list.append(heart_thread)
    crwaler_thread = threading.Thread(target=crwaler_thread_func)
    thread_list.append(crwaler_thread)

    for t in thread_list:
        t.setDaemon(True)
        t.start()
    t.join()
