# -*- coding: utf-8 -*-
import json

import requests

from utils.cookies_manager import spider_cookies, get_cookies, temp_cookies


def to_json(content):
    try:
        json_content = json.loads(content)
    except:
        json_content = None
    return json_content


class ResquestSession(object):
    def __init__(self):
        self.session = self.meke_session()
        self.spider_cookies = {}
        self.temp_cookies = {}

    @staticmethod
    def meke_session():
        session = requests.session()
        return session
    #获取page页面同时获取当前页面的cookies
    def get_response_content(self, url, headers, cookies, proxies, validate=False):
        # request_client = self.request_client
        page = self.do_get(url, headers, cookies, proxies)
        try:
            page_content = page.content
        except:
            page_content = None
            return page_content

        if isinstance(page_content, bytes):
            page_content = str(page_content, encoding='utf-8')
            cookies = get_cookies(page)
        if not validate:
            self.spider_cookies.update(cookies)
        else:
            self.temp_cookies = cookies
        return page_content

    # get请求
    def do_get(self, url, headers, cookies, proxies):
        repeat = 0
        while repeat < 3:
            repeat += 1
            try:
                content = self.session.get(url, headers=headers, cookies=cookies, proxies=proxies, timeout=15)
                if len(content.content) > 2:
                    break
            except:
                if repeat == 3:
                    print('the url:{} get failed!'.format(str(url)))
                    content = None
                continue
        return content

    def do_post(self, url, data, headers, cookies, proxies):
        repeat = 0
        while repeat < 3:
            repeat += 1
            try:
                if cookies is None:
                    cookies = self.spider_cookies
                content = self.session.post(url, data=data, headers=headers, cookies=cookies, proxies=proxies,
                                            timeout=15)
                if len(content.content) > 2:
                    break
            except:
                if repeat == 3:
                    print('the url:{} post failed!'.format(str(url)))
                    content = None
                # else:
                continue
        return content

    def get_session(self):
        return self.session
