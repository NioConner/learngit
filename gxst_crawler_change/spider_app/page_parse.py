# -*- coding: utf-8 -*-
from lxml import etree
import re
import random

class PageListParse(object):
    def __init__(self, content):
        self.content = content
        self.a_list = []

    def parse(self):
        content_list = self.content
        if len(content_list) is None:
            print('no html content get')
            return
        html = etree.HTML(content_list)
        a_list = html.xpath('//div[@class="main-layout fw f14"]/a[@class="search_list_item db"]')
        for a in a_list:
            print(a.attrib['href'])
            href = a.attrib['href']
            href = 'http://www.gsxt.gov.cn{}'.format(href)
            try:
                name = a.xpath('./h1[@class="f20"]/font')[0]
                test_name = name.text + name.tail if name.tail is not None else name.text
            except:
                test_name = a.xpath('./h1[@class="f20"]/text()')[0]
                test_name = re.sub('((\s)+ +)', '', test_name)
            # self.a_list.append({'name': test_name, 'href': href})
            try:
                history_name = a.xpath('./div[@class="f14 g9 pt10"]/div[@class="div-info-circle3"]')[0].xpath(
                    'string(.)')
                history_name = re.sub(
                    '\s', '', history_name
                )
            except:
                history_name = None
            self.a_list.append({'name': test_name, 'href': href, 'history_name': history_name})

        return self.a_list
