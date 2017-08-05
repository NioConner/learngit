# -*- coding: utf-8 -*-
import queue
import threading
import multiprocessing
import os
import time
import sched
import requests
import json
from spider_app.gee_spider import GeeSpider


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
    time.sleep(3)


class CrawlerAndHeart(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.schedule = sched.scheduler(time.time, time.sleep)
        self.thread_list = []
        self.name = name
        print('now is the {}'.format(self.name))

    def heart_connect(self, schedule, cmd, inc):
        print('{} ========post to services =============!'.format(self.name))
        schedule.enter(inc, 0, self.heart_connect, (schedule, cmd, inc))

    def heart_thread_func(self, schedule):
        schedule.enter(5, 0, self.heart_connect, (schedule, 'heart_connect', 5))
        schedule.run()

    #
    # def get_task(self):
    #     print('{} crawlering!'.format(self.name))

    def do_task(self, schedule, cmd, inc):
        get_task()
        schedule.enter(inc, 0, self.do_task, (schedule, cmd, inc))

    def crwaler_thread_func(self, schedule):
        schedule.enter(5, 0, self.do_task, (schedule, 'crwaler_connect', 5))
        schedule.run()

    def task_run(self):
        crwaler_thread = threading.Thread(target=self.crwaler_thread_func, args=(self.schedule,))
        self.thread_list.append(crwaler_thread)
        heart_thread = threading.Thread(target=self.heart_thread_func, args=(self.schedule,))
        self.thread_list.append(heart_thread)

        for t in self.thread_list:
            t.setDaemon(False)
            t.start()
        t.join()
