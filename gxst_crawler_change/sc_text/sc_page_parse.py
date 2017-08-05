# -*- coding: utf-8 -*-

import uuid

import time
from lxml import etree
import re

from config.headersetting import sc_page_header
from sc_text.sc_detiles import sc_detile_parse
from sc_text.sc_utils import sc_util
from utils.request_utils import ResquestSession


class SCPageListParse(object):
    def __init__(self, content):
        self.content = content
        self.a_list = []

    def parse(self):
        content_list = self.content
        pattern = re.compile('\w+')
        dic = {}
        if content_list is None:
            print('no html content get')
            return
        html = etree.HTML(content_list)
        sc_url = 'http://sc.gsxt.gov.cn/notice/notice/'
        part_url = html.xpath('//*[@id="wrap1"]/div[3]/div/div/div[1]/@onclick')
        print(part_url)
        par = part_url[0].split('/')[-1].replace('\'','').replace(')','').replace(' ','')
        print(par)

        # 这里是www.gsxt.gov.cn/notice/notice/view?uuid=B3Pw.X3C97hzFxhAIua12.xhRw8WkB0P&tab=01这种格式我们需要中间的uuid的部分
        page_url = sc_url + par
        # 获取到目标到url
        sendRequest = ResquestSession()
        page_detiles = sendRequest.get_response_content(page_url, headers=sc_page_header, cookies=None, proxies=None)
        page_detile_parese = etree.HTML(page_detiles)


        b = page_detile_parese.xpath('//*[@id="layout-01_01_01"]/div/table/tr/td')
        for i in b:
            try:

                key = re.findall('\w+', i.xpath('./text()')[0])[0]
            except:
                continue

            try:

                value = i.xpath('./i/text()')[0]

            except:
                value = None
            dic[key] = value
        print(dic)

        task_Id = str(uuid.uuid1())

        #
        # with open('busilice.json', 'w') as fp:
        #     json.dump(dic, fp, ensure_ascii=False, indent=4)
        sc_inv = sc_util()
        sc_inv.write_txt(dic, task_Id, file_id='busilice')

        #解析人员
        inv_dictory = {}

        inv_list = []
        d = len(page_detile_parese.xpath('//*[@id="layout-01_01_02"]/div[1]/table/tr/td[1]'))
        inv_dictory['recordsTotal'] = d-1

        for i in range(2, d + 1):
            dicto = {
                'cerNo':None,
                'cerType_CN': None,
                'conDate': None,
                'country_CN': None,
                'dom': None,
                'respForm_CN':None,
                'sConForm': None,
                'sConForm_CN': None,
            }
            inv = page_detile_parese.xpath('//*[@id="layout-01_01_02"]/div[1]/table/tr[' + str(i) + ']/td[2]/text()')
            invType_CN = page_detile_parese.xpath('//*[@id="layout-01_01_02"]/div[1]/table/tr[' + str(i) + ']/td[3]/text()')
            bLicNo = page_detile_parese.xpath('//*[@id="layout-01_01_02"]/div[1]/table/tr[' + str(i) + ']/td[4]/text()')
            blicType_CN = page_detile_parese.xpath('//*[@id="layout-01_01_02"]/div[1]/table/tr[' + str(i) + ']/td[5]/text()')
            if (len(page_detile_parese.xpath('//*[@id="layout-01_01_02"]/div[1]/table/tr[' + str(i) + ']/td[6]/a/text()')) > 0):
                invId = str(uuid.uuid1())
                dicto['invId'] = invId
                dicto['detailCheck'] = 'true'
                inv_url1 = page_detile_parese.xpath('//*[@id="layout-01_01_02"]/div[1]/table/tr[' + str(i) + ']/td[6]/a/@onclick')[0].split('\'')[1]
                inv_url0 = 'http://sc.gsxt.gov.cn/notice/notice/view_investor?uuid='
                inv_url = inv_url0+inv_url1
                inv_detiles = sendRequest.get_response_content(inv_url, headers=sc_page_header, cookies=None,proxies=None)
                inv_sc_detile = sc_detile_parse()
                subconam, acconam, inv_detile = inv_sc_detile.parse_inv(inv_detiles,task_Id,invId)

                dicto['liAcConAm'] = acconam

                dicto['liSubConAm'] = subconam


            else:
                dicto['detailCheck'] = 'false'
                dicto['liAcConAm'] = None
                dicto['liSubConAm'] = None

            dicto['inv'] = inv[0].strip()
            dicto['invType_CN'] = invType_CN[0].strip()
            dicto['bLicNo'] = bLicNo[0].strip()
            dicto['blicType_CN'] = blicType_CN[0].strip()


            inv_list.append(dicto)
        inv_dictory['data'] = inv_list
        print(inv_dictory)
        new_list = []
        new_list.append(inv_dictory)
        sc_inv = sc_util()
        sc_inv.write_txt(new_list,task_Id,file_id='inv')

        #解析人员
        people_all_list = page_detile_parese.xpath('//*[@id="layout-01_02_01"]/div/table/tr/td/ul/li/text()')
        peo_len = int(len(people_all_list)/2)
        dictory_peo = {}
        per_dic = {}
        dictory_peo['recordsTotal'] = peo_len
        list_people = []
        img_list = []

        for i in range(1, peo_len+1):
            dic = {}
            dic['name'] = people_all_list[i * 2 - 2]
            dic['position_CN'] = people_all_list[i * 2 - 1]
            if 'img src' in dic['position_CN']:
                dic['perId'] = uuid.uuid1()
                per_dic['position_CN'] = dic['position_CN']
                per_dic['perId'] = dic['perId']
                img_list.append(per_dic)


            else:
                dic['perId'] = None


            dic['pripId'] = None
            list_people.append(dic)
        dictory_peo['data'] = list_people
        print(dictory_peo)
        new_list = []
        new_list.append(dictory_peo)
        sc_inv = sc_util()
        sc_inv.write_txt(new_list, task_Id, file_id='person')


        # content_txt_manager = ContentTxtManger()
        #
        # content_txt_manager.save_person_txt(dictory_peo, 'person', img_list=img_list)



        #解析变更
        len_alter = len(page_detile_parese.xpath('//*[@id="a_alter_table"]/tr/td[1]/text()'))

        dictory_alter = {}
        dictory_alter['recordsTotal'] = len_alter
        list2 = []
        for i in range(2, len_alter+2):
            dicto = {}
            altAf = page_detile_parese.xpath('//*[@id="a_alter_table"]/tr[' + str(i) + ']/td[3]//text()')
            altBe = page_detile_parese.xpath('//*[@id="a_alter_table"]/tr[' + str(i) + ']/td[4]//text()')
            altDate = page_detile_parese.xpath('//*[@id="a_alter_table"]/tr[' + str(i) + ']/td[5]/text()')
            altItem_CN = page_detile_parese.xpath('//*[@id="a_alter_table"]/tr[' + str(i) + ']/td[2]/text()')
            try:
                dicto['altAf'] = altAf[0].strip()
            except:
                dicto['altAf'] = None

            try:
                dicto['altBe'] = altBe[0].strip()
            except:
                dicto['altBe'] = None
            try:
                dt = altDate[0].strip()
                timeArray = time.strptime(dt, "%Y年%m月%d日")
                dicto['altDate'] = int(time.mktime(timeArray) * 1000)
            except:
                dicto['altDate'] = None
            try:
                dicto['altItem_CN'] = altItem_CN[0].strip()
            except:
                dicto['altItem_CN'] = None
            list2.append(dicto)

        dictory_alter['data'] = list2
        print(dictory_alter)
        new_list = []
        new_list.append(dictory_alter)
        sc_inv = sc_util()
        sc_inv.write_txt(new_list, task_Id, file_id='alter')


