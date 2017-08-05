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
from multiprocessing import Pool
from utils.task_class import CrawlerAndHeart


def track_generate():
    for i in range(100):
        success_count = 0
        gs = GeeSpider('小米科技', '')
        time.sleep(1)
        success_count += gs.count
        print('current i is ', i)
        print('current successed count is ', str(success_count / 100))
    print('the success count is', success_count)


def main(name):
    ch = CrawlerAndHeart(name)
    ch.task_run()


if __name__ == '__main__':
    """
    制约因素（排除IP影响）：
    1、blacklist 和 invailed
    2、滑块验证失败需要重新重头请求
    """
    # 任务访问地址：http://newdaas.bidata.com.cn/srs/newdaasBRTaskService/getNewTask
    # 主方法

    pool = Pool(5)
    for i in range(5):
        pool.apply_async(main, args=(i,))
    pool.close()
    pool.join()
