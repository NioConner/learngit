# -*- coding: utf-8 -*-

from config.url_path_seting import gsxt_url
from tenacity import retry
from utils.request_utils import *


def get_cookies(cook):
    cook_list = {}
    for c in cook.cookies:
        cook_list[c.name] = c.value
    return cook_list


temp_cookies = None

spider_cookies = {}

