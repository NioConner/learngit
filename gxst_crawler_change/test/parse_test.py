# -*- coding: utf-8 -*-
import requests
from config.proxysetting import proxies
import re
import json

# 成华区林自民商贸部
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
page_host = 'http://www.gsxt.gov.cn'
page_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'www.gsxt.gov.cn',
    'Referer': 'http://www.gsxt.gov.cn/corp-query-search-1.html',
    'User-Agent': user_agent,
    'Upgrade-Insecure-Requests': '1',
    # 'X-Requested-With': 'XMLHttpRequest'
}
# 纳小米科技
# page_url = 'http://www.gsxt.gov.cn/%7BqKgt08egk5wlJKKNTD4Q1OPvdwuA5xJNhugShf5vnTEkWYdv-Rm2MjLPCqaJxjVlLtTbUzO5cclIp7md_ZE3D6hRpiHkWbj8FS_dRCzKGnnmGNjSdFh5pjYPXAU1GcDmE2J3EqDPL2c9wof0-DAOzw-1498798873566%7D'
# 91310120MA1HKQ389T
# page_url = 'http://www.gsxt.gov.cn/%7B4LLRPpoLrsW0jYe5M-PmofMfJCexwbG2MDEgi1vRNWlUbnro_QKdh9huY5K-ETCNsG8rtlpeqXgKwwiEAM0-d8ZJtrpG1B-85qTRNQeClzpt09EUVH6iNyTzH3-MvTwjxItdMVNxu29wWkyMGJxPtg-1498799228245%7D'
# 91331023076242794E
# page_url = 'http://www.gsxt.gov.cn/%7BWkmRn1rPhLN-9SNOZA_3-jbzAkSkc3iFooK19VJ9SB8s-Y3CrRm7dt3ifUQJNNVxi1Nnfoz0-iSigct88xqjQVwVo79AFRThC534i8fWutkHvmEu-WXigTE4QAl0SeSriV7Bee7kJFGJQQcohilGMA-1498806600754%7D'
page_url = 'http://www.gsxt.gov.cn/%7BeqrFpXafe1lictzmnU_mzam8UJg8yYnYCzxalxWB5mA4I42mfFW1Nj5mVLpmqZR-saKsnL--Ri2_bCDkpk6pZOrXA3DP09ZeEN_Nujxi2n18_B-zMNqkyj8ctob8_TTZVUFHWPnW8TWDFm-UKHVtrg-1498883274277%7D'
session = requests.session()
# request page url and get page content
content = session.get(page_url, headers=page_headers, proxies=proxies)
# get Inv url
try:
    shareholderUrl = page_host + re.findall('var shareholderUrl = "(.+?)";', content.text)[0]
    print(shareholderUrl)
except:
    raise 'failed!'
# get keyPerson
keyPersonUrl = page_host + re.findall('var keyPersonUrl = "(.+?)";', content.text)[0]
# get change
alterInfoUrl = page_host + re.findall('var alterInfoUrl = "(.+?)";', content.text)[0]

inv_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '23',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.gsxt.gov.cn',
    'Origin': 'http://www.gsxt.gov.cn',
    'Referer': shareholderUrl,
    'User-Agent': user_agent,
    'X-Requested-With': 'XMLHttpRequest',
}
draw = 0
start = 0
totalPage = 1
inv_data = {
    'draw': draw,
    'start': start,
    'length': '5',
}

# "<script>window.location.href='/index/invalidLink'</script>"
# "recordsTotal":6,"start":0,"totalPage":2

invid_list = []
while draw < totalPage:
    draw += 1
    inv_data['draw'] = draw
    inv_data['start'] = 0 + (draw - 1) * 5
    shareholderUrl_content = session.post(shareholderUrl, headers=inv_headers, data=inv_data, proxies=proxies)
    print(shareholderUrl)
    print(inv_headers)
    shareholderUrl_content_text = shareholderUrl_content.text
    print(shareholderUrl_content_text)
    recordsTotal = re.findall('"recordsTotal":([0-9]+),', shareholderUrl_content_text)[0]
    totalPage = int(re.findall('"totalPage":([0-9]+)', shareholderUrl_content_text)[0])
    invid_list += re.findall('"invId":"(.+?)"', shareholderUrl_content_text)

print(invid_list)

inv_detail_url = 'http://www.gsxt.gov.cn/corp-query-entprise-info-shareholderDetail-{}.html'
inv_detail_headers = {
    'Host': 'www.gsxt.gov.cn',
    'Referer': shareholderUrl,
    'User-Agent': user_agent,
    'X-Requested-With': 'XMLHttpRequest',
}
for invid in invid_list:
    detail_url = inv_detail_url.format(invid)
    detail_res = session.get(detail_url, headers=inv_detail_headers, proxies=proxies)
    print(detail_res.text)

# ====== get keyperson data ======
keyPerson_headers = {
    'Host': 'www.gsxt.gov.cn',
    'Referer': shareholderUrl,
    'User-Agent': user_agent,
    'X-Requested-With': 'XMLHttpRequest',
}

keyPerson_res = session.get(keyPersonUrl, headers=keyPerson_headers, proxies=proxies)
try:
    js = json.loads(keyPerson_res.text)
    print(js)
except:
    pass

# ======get change ========

draw = 0
start = 0
totalPage = 1
change_data = {
    'draw': draw,
    'start': start,
    'length': '5',
}

change_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '23',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.gsxt.gov.cn',
    'Origin': 'http://www.gsxt.gov.cn',
    'Referer': alterInfoUrl,
    'User-Agent': user_agent,
    'X-Requested-With': 'XMLHttpRequest',
}

change_list = []
while draw < totalPage:
    draw += 1
    change_data['draw'] = draw
    change_data['start'] = 0 + (draw - 1) * 5
    alterInfoUrl_res = session.post(alterInfoUrl, headers=change_headers, data=change_data, proxies=proxies)
    alterInfoUrl_text = alterInfoUrl_res.text
    print(alterInfoUrl_text)
    recordsTotal = re.findall('"recordsTotal":([0-9]+),', alterInfoUrl_text)[0]
    totalPage = int(re.findall('"totalPage":([0-9]+)', alterInfoUrl_text)[0])
