import time
from lxml import etree

from config.headersetting import sc_page_header
from sc_text.sc_utils import sc_util
from utils.request_utils import ResquestSession


class sc_detile_parse():
    def parse_inv(self, content, task_id, filename):
        m = etree.HTML(content)
        dictory = {
            'data': []
        }
        q = len(m.xpath('/html/body/div/div[2]/table/tr'))
        list1 = []
        subconam = 0
        for i in range(2, q + 1):
            dicto = {
                'subId':None,
                'conForm': None,
                'invId': None,
                'lastModifiedTime': None,
            }
            conForm_CN = m.xpath('/html/body/div/div[2]/table/tr[' + str(i) + ']/td[1]/text()')
            subConAm = m.xpath('/html/body/div/div[2]/table/tr[' + str(i) + ']/td[2]/text()')
            conDate = m.xpath('/html/body/div/div[2]/table/tr[' + str(i) + ']/td[3]/text()')
            try:
                dicto['conForm_CN'] = conForm_CN[0].strip()
            except:
                dicto['conForm_CN'] = None
            try:
                subConAm[0]
                try:
                    subConAm_temp = int(subConAm[0].strip())
                    dicto['subConAm'] = subConAm_temp
                except:
                    subConAm_temp = float(subConAm[0].strip())
                    dicto['subConAm'] = subConAm_temp
                subconam += subConAm_temp
            except:
                dicto['subConAm'] = None
                subconam = None
            try:
                dt = conDate[0].strip()
                timeArray = time.strptime(dt, "%Y年%m月%d日")
                # 转换成时间戳
                dicto['conDate'] = int(time.mktime(timeArray) * 1000)
            except:
                dicto['conDate'] = None

            # 后面全是辅助字段
            list1.append(dicto)
        # dictory['data'].append(list1)
        w = len(m.xpath('/html/body/div/div[3]/table/tr'))
        list2 = []
        acconam = 0
        for i in range(2, w + 1):
            dicto = {
                'acId': None,
                'conForm': None,
                'invId': None,
                'lastModifiedTime': None,

            }
            conForm_CN = m.xpath('/html/body/div/div[3]/table/tr[' + str(i) + ']/td[1]/text()')
            acConAm = m.xpath('/html/body/div/div[3]/table/tr[' + str(i) + ']/td[2]/text()')
            conDate = m.xpath('/html/body/div/div[3]/table/tr[' + str(i) + ']/td[3]/text()')
            try:
                dicto['conForm_CN'] = conForm_CN[0].strip()
            except:
                dicto['conForm_CN'] = None
            try:
                acConAm[0]
                try:
                    acConAm_temp = int(acConAm[0].strip())
                    dicto['acConAm'] = acConAm_temp
                except:
                    acConAm_temp = float(acConAm[0].strip())
                    dicto['acConAm'] = acConAm_temp
                acconam += acConAm_temp
            except:
                dicto['acConAm'] = None
                acconam = None
            try:
                dt = conDate[0].strip()

                timeArray = time.strptime(dt, "%Y年%m月%d日")
                # 转换成时间戳
                dicto['conDate'] = int(time.mktime(timeArray) * 1000)

            except:
                dicto['conDate'] = None
            list2.append(dicto)
        dictory['data'].append(list2)
        dictory['data'].append(list1)

        print(dictory)
        print(acconam)
        sc = sc_util()
        sc.write_txt(dictory, task_id, filename)

        return subconam, acconam, dictory


if __name__ == '__main__':
    request_client = ResquestSession()
    inv_detiles = request_client.get_response_content(
        'http://sc.gsxt.gov.cn/notice/notice/view_investor?uuid=ZaLp6yH6zLE=', headers=sc_page_header, cookies=None,
        proxies=None)
    # inv_detile_parese = etree.HTML(inv_detiles)
    inv_sc_detile = sc_detile_parse()
    a, b, c = inv_sc_detile.parse_inv(inv_detiles, 'bbbbb', 'bbbbb')
