# -*- coding: utf-8 -*-
import requests
from config.page_headers_setting import *
from config.proxysetting import proxies
import re
import json
from utils.track_and_txt_manager import *
from bs4 import BeautifulSoup
from lxml import etree
from requests.exceptions import ReadTimeout
from utils.request_utils import *


class ParsePageApp(object):
    def __init__(self, url, key_word, task_id, history_name=None):
        self.task_id = task_id
        self.home_url = url
        self.host = 'http://www.gsxt.gov.cn'
        self.key_word = key_word
        self.request_client = ResquestSession()
        self.history_name = history_name
        self.content_txt_manager = ContentTxtManger(self.key_word, self.task_id, self.history_name)
        self.ent_type = ''
        self.black_invaild = 0

    def get_parse(self, url, headers, url_type, num=0):
        cookies = None
        content = self.request_client.get_response_content(
            url, headers, cookies, proxies)

        try:
            # num = 0
            content = json.loads(content)
            print(content)
            img_list = []
            if len(content['data']) != 0:
                for data in content['data']:
                    per_dic = {}
                    if 'img src' in data['position_CN']:
                        per_dic['position_CN'] = re.findall(
                            '<imgsrc="(.+?)"/>', re.sub('\s', '', data['position_CN'])
                        )[0]
                    else:
                        per_dic['position_CN'] = data['position_CN']
                    per_dic['perId'] = data['perId']
                    img_list.append(per_dic)
            self.content_txt_manager.save_person_txt([content], url_type, img_list=img_list)
        except:
            if num < 3:
                num += 1
                self.get_parse(url, headers, url_type, num)
                return
            return

    def yield_post_parse(self, url, headers, url_type='', inv_num=0):
        cookies = None
        content_txt_manager = self.content_txt_manager
        # session = self.session
        draw = 0
        start = 0
        totalp_age = 1
        temp_data = {
            'draw': draw,
            'start': start,
            'length': '5',
        }
        inv_list = []
        detail_list = []
        inv_id_list = []
        while draw < totalp_age:
            draw += 1
            temp_data['draw'] = draw
            temp_data['start'] = 0 + (draw - 1) * 5
            try:
                response = requests.post(url, headers=headers, data=temp_data, proxies=proxies)
                content = response.content.decode('utf-8')
                print(content)
                totalp_age = int(re.findall('"totalPage":([0-9]+)', content)[0])
                inv_id = re.findall('"invId":"(.+?)"', content)
                inv_id_list += inv_id
                content_js = json.loads(content)
                inv_list.append(content_js)
            except:
                if inv_num < 3:
                    inv_num += 1
                    self.yield_post_parse(url, headers, url_type, inv_num)
                    return
                content = None
                # return
        print(inv_list)
        if content is None:
            return
        if url_type == 'inv':
            try:
                detail_check = re.findall('"detailCheck":"(.+?)"', content)[0]
                if detail_check == 'false':
                    detail_check = False
                else:
                    detail_check = True
            except:
                detail_check = False
            if detail_check:
                inv_detail_headers['Referer'] = url
                print(inv_id_list)
                for invid in inv_id_list:
                    detail_url = inv_detail_url.format(invid)
                    invid_num = 0
                    while invid_num < 3:
                        invid_num += 1
                        try:
                            detail_res = requests.get(
                                detail_url, headers=inv_detail_headers, proxies=proxies)
                            break
                        except ReadTimeout as e:
                            detail_res = None
                    if detail_res is None:
                        detail_list = []
                    else:
                        try:
                            detail_js = json.loads(detail_res.text)
                            detail_list.append({
                                'invId': invid, 'detail_js': detail_js
                            })
                        except:
                            pass
        content_txt_manager.save_txt(
            content_list=inv_list, detail_list=detail_list, url_type=url_type)

        print('{}:'.format(url_type), str(inv_list))
        print('detail_list:', str(detail_list))

    def content_parse(self, url_dic):
        if url_dic['url_class'] == 'share_holder_url':
            inv_headers['Referer'] = url_dic['url']
            self.yield_post_parse(url_dic['url'], inv_headers, 'inv')
        elif url_dic['url_class'] == 'key_person_url':
            keyperson_headers['Referer'] = self.home_url
            self.get_parse(url=url_dic['url'], headers=keyperson_headers, url_type='person')
        elif url_dic['url_class'] == 'alter_info_url':
            change_headers['Referer'] = url_dic['url']
            self.yield_post_parse(url_dic['url'], change_headers, 'alter')
        else:
            pass

    def begin_parse(self, count=0):
        # session = self.session
        cookies = None
        home_url = self.home_url
        if home_url is None:
            self.ent_type = None
            self.content_txt_manager.zip_func()
            self.content_txt_manager.data_post(self.ent_type)
            return
        host = self.host
        try:
            content = self.request_client.get_response_content(
                home_url, home_url_headers, cookies, proxies)
            # content = content.decode('utf-8')

            if 'blackList' in content or 'invalidLink' in content:
                if self.black_invaild < 3:
                    self.black_invaild += 1
                    self.begin_parse()
                    return
                else:
                    self.ent_type = None
                    self.content_txt_manager.zip_func()
                    self.content_txt_manager.data_post(self.ent_type)
                    return
            url_list = []
            # try:
            # get inv
            share_holder_url = host + re.findall('var shareholderUrl = "(.+?)";', content)[0]
            # get keyPerson
            key_person_url = host + re.findall('var keyPersonUrl = "(.+?)";', content)[0]
            # get change
            alter_info_url = host + re.findall('var alterInfoUrl = "(.+?)";', content)[0]

            content_html = etree.HTML(content)
            dl = content_html.xpath('//div[@class="overview"]/dl')
            for d in dl:
                item = re.sub('：', '', str(d.xpath('./dt/text()')[0]))
                result = re.sub('\s', '', str(d.xpath('./dd/text()')[0]))
                if item == '类型':
                    if '个体' in result:
                        self.ent_type = 'gt'
                    else:
                        self.ent_type = 'ent'
                    break
            if self.ent_type == 'ent':
                url_list.append({'url': share_holder_url, 'url_class': 'share_holder_url'})
                url_list.append({'url': alter_info_url, 'url_class': 'alter_info_url'})
            url_list.append({'url': key_person_url, 'url_class': 'key_person_url'})
        except:
            if count < 3:
                count += 1
                print('home_url request failed reget!')
                self.begin_parse(count)
                return
            print('home_url changed!')
            return
        self.content_txt_manager.save_html(content)

        for url_dic in url_list:
            self.content_parse(url_dic)

        self.content_txt_manager.zip_func()
        self.content_txt_manager.data_post(self.ent_type)


if __name__ == '__main__':
    page_url = 'http://www.gsxt.gov.cn/%7BZT9ofV0HMsaDRFzaNZpHmzsOpI-X2cvorkRSfaKiVc1MHX8pcRJSPJKrlJy3f1DAkuaXlk62_Kb9lpBMIbuWqO4W5ZnOmrZhZr2daod64xRTkPbKGMYKUs4pWNY1DOWebVu6IKCS5xivVBEBeYJbNg-1498805707835%7D'
    page_app = ParsePageApp(page_url)
    page_app.begin_parse()
