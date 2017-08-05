import json
import re
import uuid
from requests import Session

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

    def refresh_run(self):
        self.run()

    def get_vilidate(self, x_dis):

        pass

    def get_distance(self):
        cookies = self.request_client.spider_cookies
        timestamp = str(int(time.time() * 1000))
        pic_url_content = self.request_client.get_response_content(
            pic_url.format(self.gt, self.challenge, timestamp),
            gee_headers, cookies, proxies
        )
        print(pic_url_content)
        try:
            pic_dic = re.findall('(\{.*\})', str(pic_url_content))[0]
            pic_dic = to_json(pic_dic)
            bg_url = 'http://static.geetest.com/%s' % str(pic_dic['bg'])
            fullbg_url = 'http://static.geetest.com/%s' % str(pic_dic['fullbg'])
            self.challenge = pic_dic['challenge']
            distance = generate_distance(bg_url, fullbg_url, self.request_client, cookies)
        except:
            if self.distance_refresh_count < 3:
                self.distance_refresh_count += 1
                self.refresh_run()
                return
            else:
                distance = 0
        return distance


    def run_offline(self,token):
        cookies = self.request_client.spider_cookies

        request_client = self.request_client

        # 第一步 得到图片距离
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

        # 第二步 通过距离和challenge来获取validate
        # validate: b.ra(c, e.config.challenge) + "_" + b.ra(a.t("rand0", e.id), e.config.challenge) + "_" + b.ra(
        #     a.t("rand1", e.id), e.config.challenge),
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
            'condition.keyword': '长虹',
        }

        # sc_validate['Cookie'] = cookies
        print(sc_validate)

        content_list1 = request_client.do_post('http://sc.gsxt.gov.cn/notice/search/ent_info_list', data=list_date,
                                               headers=sc_validate, cookies=None, proxies=None)

        print(content_list1.text)

    def run(self):
        cookies = self.request_client.spider_cookies

        # 第一步 访问login页面得到gt、cookies和challenge 需要json content

        # 第一点一步 获取token
        page_sc = self.request_client.get_response_content(get_token_url, gsxt_headers, cookies, proxies)
        pattern = re.compile(r'token": ".*?"')
        # re的findall返回的是list这里取list的第一项然后去掉首位多余的部分剩下的就是token了
        token = (re.findall(pattern, page_sc, ))[0][9:][:-1]
        print(token)

        # 获取challenge
        timestamp = str(int(time.time() * 1000))
        login_url = register_url.format(timestamp)
        print(login_url)
        captcha_content = self.request_client.get_response_content(login_url, gsxt_headers, cookies, proxies)
        print(captcha_content)
        json_captcha = to_json(captcha_content)
        if json_captcha is None or len(json_captcha) == 0:
            print('get captcha_content failed!')
            # 向服务端填写空数据 待填写
            self.save_none_zip()
            return
        self.gt = json_captcha['gt']
        self.challenge = json_captcha['challenge']

        print(len(self.challenge))
        if len(self.challenge)==34:
            self.run_offline(token=token)

        else:
            self.run_online()


    def run_online(self):

        cookies = self.request_client.spider_cookies
        request_client = self.request_client

        # 第一步 访问home页，得到cookies 不需要content
        home_response = self.request_client.get_response_content(gsxt_url, gsxt_headers, cookies, proxies)
        if home_response is None:
            self.save_none_zip()
            return

        # 第二步 访问SearchItemCaptcha_url得到gt、cookies和challenge 需要json content
        timestamp = str(int(time.time() * 1000))
        search_url = search_item_captcha_url.format(timestamp)
        captcha_content = self.request_client.get_response_content(search_url, gsxt_headers, cookies, proxies)

        json_captcha = to_json(captcha_content)
        if json_captcha is None or len(json_captcha) == 0:
            print('get captcha_content failed!')
            # 向服务端填写空数据 待填写
            self.save_none_zip()
            return
        self.gt = json_captcha['gt']
        self.challenge = json_captcha['challenge']


        # 第四步 得到图片地址并计算距离 需要content str
        print('begin to calculate the distance!')
        distance = self.get_distance()
        if distance == 0:
            print('failed to get distance')
            # 向服务端填写空数据 待填写
            self.save_none_zip()
            return

        # 第五步 得到token
        timestamp = time.strftime('%M-%S').split('-')
        v = int(timestamp[0]) + int(timestamp[1])
        for_token_content = self.request_client.get_response_content(
            for_token_url.format(str(v)),
            gsxt_headers, cookies, proxies
        )
        try:
            token_arr = eval(for_token_content)
            token_str = ''.join([chr(int(token_arr[i])) for i in range(len(token_arr))])
            token = re.findall('location_info = (.*?);', token_str)[0]
        except:
            print('can not get the token')
            # 向服务端填写空数据 待填写
            self.save_none_zip()
            return

        # 第六步 访问滑块页面
        self.request_client.get_response_content(
            open_geetest_url.format(token),
            gsxt_headers, cookies, proxies
        )
        time.sleep(3.5)

        # 第七部 生成滑块list、a轨迹、usrres等进行validate页面的请求
        js = self.get_validate(distance)
        if js is None:
            # 向服务端填写空数据 待填写
            self.save_none_zip()
            return
        validate = js['validate']
        geetest_seccode = '{}|jordan'.format(validate)
        validate_data['geetest_validate'] = validate
        validate_data['geetest_challenge'] = self.challenge
        validate_data['searchword'] = self.kws
        validate_data['geetest_seccode'] = geetest_seccode

        content_list = request_client.do_post('http://www.gsxt.gov.cn/corp-query-search-1.html', validate_data,
                                              validate_headers, cookies, proxies)
        try:
            page_content = str(content_list.content, encoding='utf-8')
        except:
            page_content = None
        if page_content is None or len(page_content) < 3:
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
            page_parse = PageListParse(page_content)
            page_list = page_parse.parse()
            print(page_list)
            try:
                tar_list = page_list[0]
                target_url = tar_list['href']
                history_name = tar_list['history_name']
            except:
                target_url = history_name = None
            app = ParsePageApp(target_url, self.kws, self.task_id, history_name)
            app.begin_parse()

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
