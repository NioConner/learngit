import json
import re
import uuid
from requests import Session

from sc_text.sc_page_parse import SCPageListParse
from sc_text.sc_urls import *
from sc_text.sc_getpicinfo import sc_pic
from config.url_path_seting import *
from spider_app.page_parse import PageListParse
from spider_app.parse_page_app import ParsePageApp
# from utils.cookies_manager import temp_cookies, spider_cookies
from utils.create_track_utils import *
from utils.js_utils import *
from utils.pic_utils import *
from utils.request_utils import *
from utils.track_and_txt_manager import track_txt_manager


class SCSpider(object):
    def __init__(self, kws, task_id):
        self.kws = kws
        self.task_id = task_id
        self.request_client = ResquestSession()  # 自己写的模块
        # self.cookies = self.request_client.sipder_cookies
        self.gt = None
        self.challenge = ''
        self.total_count = 0
        # self.temp_cookies = self.request_client.temp_cookies
        self.black_list = 0
        self.invalid_link = 0
        self.distance_refresh_count = 0
        self.refresh_validate = 0



    def run(self):
        cookies = self.request_client.spider_cookies
        request_client = self.request_client
        #返回类型有32位的chanllenge和34位的challenge，34位的直接执行offline的部分，如果是32位则重新提交需求
        try:
            page_sc = self.request_client.get_response_content(get_token_url, sc_register, cookies, proxies)
            pattern = re.compile(r'token": ".*?"')
            # re的findall返回的是list这里取list的第一项然后去掉首位多余的部分剩下的就是token了
            token = (re.findall(pattern, page_sc, ))[0][9:][:-1]
            print(token)

            # 获取challenge
            timestamp = str(int(time.time() * 1000))
            login_url = register_url.format(timestamp)
            print(login_url)
            captcha_content = self.request_client.get_response_content(login_url, sc_register, cookies, proxies)
            print(captcha_content)
            json_captcha = to_json(captcha_content)
            if json_captcha is None or len(json_captcha) == 0:
                print('get captcha_content failed!')
                # 向服务端填写空数据 待填写
                self.save_none_zip()
                return
            self.gt = json_captcha['gt']
            self.challenge = json_captcha['challenge']
            self.challenge[33]
            print(len(self.challenge))
        except:
            #如果返回出错则重新实例化这个方法来运行
            b = SCSpider(keyword, task_id)
            b.run()
            return

        print('begin to calculate the distance!')
        get_img = sc_pic()
        img_info = get_img.get_picture()
        # 实例化获取图片的内容

        distance = img_info[2]
        # 取回的距离 后面生成validate1有用
        val2 = img_info[3]
        # 取回的随机数一 后面生成validate2有用
        val3 = img_info[4]
        # 取回的随机数二 后面生成validate3有用
        if distance == 0:
            print('failed to get distance')
            # 向服务端填写空数据 待填写
            self.save_none_zip()
            return

        # 第三步 通过距离和challenge来获取validate
        validate1 = UsrResponseGenerate(distance, self.challenge).userresponse_generate()

        validate2 = UsrResponseGenerate(val2, self.challenge).userresponse_generate()

        validate3 = UsrResponseGenerate(val3, self.challenge).userresponse_generate()

        validate = validate1 + '_' + validate2 + '_' + validate3

        validate_data = {

            'geetest_challenge': self.challenge,
            'geetest_validate': validate,
            'geetest_seccode': validate + '|jordan',

        }
        content_list = request_client.do_post('http://sc.gsxt.gov.cn/notice/pc-geetest/validate', data=validate_data,
                                              headers=sc_validate, cookies=cookies, proxies=proxies)

        print(content_list)

        list_date = {
            'condition.searchType': '1',
            'captcha': '',
            'geetest_challenge': self.challenge,
            'geetest_validate': validate,
            'geetest_seccode': validate + '|jordan',
            'session.token': token,
            'condition.keyword': '四川剑南春(集团)',
        }

        print(sc_validate)

        page_content = request_client.do_post('http://sc.gsxt.gov.cn/notice/search/ent_info_list', data=list_date,
                                              headers=sc_validate, cookies=None, proxies=None)

        #print(page_content.text)
        if page_content is None:
            # 向服务端填写空数据 待填写
            self.save_none_zip()
            return

        if 'blackList' in page_content:
            self.black_list += 1
            if self.total_count < 3:
                self.total_count += 1
                print('blackList page and refresh!')
                self.refresh_run()
        elif 'invalidLink' in page_content:
            self.invalid_link += 1
            if self.total_count < 3:
                self.total_count += 1
                print('invalidLink page and refresh!')
                self.refresh_run()
        else:
            page_parse = SCPageListParse(page_content.text)
            page_list = page_parse.parse()
            print(page_list)
            # try:
            #     tar_list = page_list[0]
            #     target_url = tar_list['href']
            #     history_name = tar_list['history_name']
            # except:
            #     target_url = history_name = None
            # app = ParsePageApp(target_url, self.kws, self.task_id, history_name)
            # app.begin_parse()

    def save_none_zip(self):
        target_url = None
        app = ParsePageApp(target_url, self.kws, self.task_id)
        app.begin_parse()


if __name__ == '__main__':
    # bg_url = 'http://static.geetest.com/pictures/gt/c81e728d9/bg/0d78c5e59.jpg'
    # fullbg_url = 'http://static.geetest.com/pictures/gt/c81e728d9/c81e728d9.jpg'
    # request_client = ResquestSession()
    # cookies = request_client.spider_cookies
    # distance = generate_distance(bg_url, fullbg_url, request_client,cookies)
    # print(distance)
    keyword = '91130605MA07WGLR6D'
    task_id = str(uuid.uuid1())
    a = SCSpider(keyword, task_id)
    a.run()
