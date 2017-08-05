# -*- coding: utf-8 -*-
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
SearchItemCaptcha_url = 'http://www.gsxt.gov.cn/SearchItemCaptcha?v={}'
gettype_url = 'http://api.geetest.com/gettype.php?gt={}&callback=geetest_{}'
pic_url = 'http://api.geetest.com/get.php?gt={}&challenge={}&product=popup&offline=false&protocol=&type=slide&path=/static/js/geetest.5.10.10.js&callback=geetest_{}'
for_token_url = 'http://www.gsxt.gov.cn/corp-query-custom-geetest-image.gif?v={}'
for_next_url = 'http://www.gsxt.gov.cn/corp-query-geetest-validate-input.html?token={}'
for_validate_url = 'http://api.geetest.com/ajax.php?gt={}&challenge={}&userresponse={}&passtime={}&imgload={}&a={}&callback=geetest_{}'

gsxt_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'www.gsxt.gov.cn',
    'Referer': 'http://www.gsxt.gov.cn/index.html',
    'User-Agent': user_agent,
    'X-Requested-With': 'XMLHttpRequest',
    '___SEEKS_PROXY_USERID': 'newdaas_br',
    '___SEEKS_PROXY_ALLOW_CHANGE_IP': '1',
}

gee_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'api.geetest.com',
    'Referer': 'http://www.gsxt.gov.cn/index.html',
    'User-Agent': user_agent,
    'X-Requested-With': 'XMLHttpRequest',
    '___SEEKS_PROXY_USERID': 'newdaas_br',
    '___SEEKS_PROXY_ALLOW_CHANGE_IP': '0',
}
validate_header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'api.geetest.com',
    'Referer': 'http://www.gsxt.gov.cn/corp-query-homepage.html',
    'User-Agent': user_agent,
    '___SEEKS_PROXY_USERID': 'newdaas_br',
    '___SEEKS_PROXY_ALLOW_CHANGE_IP': '0',
}
pic_headers = {
    'Origin': 'http://www.gsxt.gov.cn',
    'Referer': 'http://www.gsxt.gov.cn/index.html',
    'User-Agent': user_agent,
    '___SEEKS_PROXY_USERID': 'newdaas_br',
    '___SEEKS_PROXY_ALLOW_CHANGE_IP': '0',
}

validate_headers = {
    'Host': 'www.gsxt.gov.cn',
    'Origin': 'http://www.gsxt.gov.cn',
    'Referer': 'http://www.gsxt.gov.cn/index.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': user_agent,
    '___SEEKS_PROXY_USERID': 'newdaas_br',
    '___SEEKS_PROXY_ALLOW_CHANGE_IP': '0',

}

validate_data = {
    'tab': 'ent_tab',
    # 'token': '35785951',
    'searchword': '',
    'geetest_challenge': '',
    'geetest_validate': '',
    'geetest_seccode': '',
}

sc_register = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Host':'sc.gsxt.gov.cn',
    'Referer':'http://sc.gsxt.gov.cn/notice/home',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}


sc_validate = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    #'Content-Length': '274',
    'Content-Type': 'application/x-www-form-urlencoded',
    #'Cookie':'',
    #'Cookie': 'JSESSIONID_NOTICE=XvCB0kB84WuZiwX2WFDSdsGBDMXNP7er8DDRvIBa4KS-72H0wXTr!-1602967906; UM_distinctid=15d736ee13a3ef-0e7d502bd2f0dc-30617408-13c680-15d736ee13b572; BIGipServernotice_liaison=385885120.19487.0000; Hm_lvt_cdb4bc83287f8c1282df45ed61c4eac9=1501049149,1501049705,1501049751,1501068347; Hm_lpvt_cdb4bc83287f8c1282df45ed61c4eac9=1501068347; CNZZDATA1000298231=1026782411-1500879426-http%253A%252F%252Fwww.gsxt.gov.cn%252F%7C1501117171',
    'Host': 'sc.gsxt.gov.cn',
    'Origin': 'http://sc.gsxt.gov.cn',
    'Referer': 'http://sc.gsxt.gov.cn/notice/home',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',

}

sc_page_header = {
    'Cache-Control':'no-cache',
    'Cache-Control':'no-store',
    'Content-Language':'zh-CN',
    'Content-Type':'text/html; charset=UTF-8',
    'Date':'Mon, 31 Jul 2017 03:50:45 GMT',
    'Expires':'Thu, 01 Jan 1970 00:00:00 GMT',
    'Pragma':'no-cache',
    'Transfer-Encoding':'chunked',
    'X-Powered-By':'Servlet/2.5 JSP/2.1',
}