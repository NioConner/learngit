import json
import re

from config.url_path_seting import *
from spider_app.page_parse import *
from spider_app.parse_page_app import ParsePageApp
# from utils.cookies_manager import temp_cookies, spider_cookies
from utils.create_track_utils import *
from utils.js_utils import *
from utils.pic_utils import *
from utils.request_utils import *
from utils.track_and_txt_manager import track_txt_manager


class GeeSpider(object):
    def __init__(self, kws, task_id):
        self.kws = kws
        self.task_id = task_id
        self.request_client = ResquestSession()#自己写的模块
        # self.cookies = self.request_client.sipder_cookies
        self.gt = None
        self.challenge = None
        self.total_count = 0
        # self.temp_cookies = self.request_client.temp_cookies
        self.black_list = 0
        self.invalid_link = 0
        self.distance_refresh_count = 0
        self.refresh_validate = 0

    def refresh_run(self):
        self.run()

    def get_validate(self, distance):
        if distance != 0 and distance is not None:
            move_list = track_txt_manager.query_distance(distance)
        else:
            js = None
            return js

        # print(move_list)
        validate_url = for_validate_url.format(
            self.gt, self.challenge,
            UsrResponseGenerate(distance, self.challenge).userresponse_generate(),  # userresponse
            str(move_list[len(move_list) - 1][2]),  # passtime
            str(random.randint(0, 100) + 50),  # imgload
            ATrackGenerate(move_list).start_gen(),  # a_track
            str(int(time.time() * 1000)),  # timestamp
        )
        validate_content = self.request_client.get_response_content(
            validate_url, validate_header, self.request_client.spider_cookies, proxies, validate=True
        )
        try:
            print(validate_content)
            sv = re.findall('\((.+?)\)', validate_content)[0]
            js = json.loads(sv)

        except:
            print('validate_content catch failed!')
            if self.refresh_validate < 3:
                self.refresh_validate += 1
                print('load validate json failed!')
                time.sleep(random.randint(4, 6))
                self.refresh_run()
                return
            js = None
            return js
        if 'success' in js.keys():
            # 如果success为0时，则重新组装轨迹进行请求
            if js['success'] == 0:
                if self.refresh_validate < 3:
                    self.refresh_validate += 1
                    if track_txt_manager.use_track and track_txt_manager.record_path is not None:
                        print('record_path is not None,begin to delete!')
                        track_txt_manager.delete_txt()
                    time.sleep(random.randint(4, 6))
                    self.refresh_run()
                    return
                else:
                    js = None
                    return js
            elif js['success'] == 1:
                self.request_client.spider_cookies.update(
                    self.request_client.temp_cookies
                )
                # self.count = 1
                if not track_txt_manager.use_track and track_txt_manager.record_path is not None:
                    print('begin to save the new track!')
                    track_txt_manager.create_file(distance, move_list)
                return js
            else:
                pass
        else:
            if self.refresh_validate < 3:
                self.refresh_validate += 1
                time.sleep(random.randint(1, 2))
                print('can not get the key of success!')
                self.refresh_run()
                return
            js = None
            return js

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

    def run(self):
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

        # 第三步 加载js 不需要content
        timestamp = str(int(time.time() * 1000))
        self.request_client.get_response_content(
            gettype_url.format(self.gt, timestamp),
            gee_headers, cookies, proxies
        )
        time.sleep(0.5)

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
    bg_url = 'http://static.geetest.com/pictures/gt/c81e728d9/bg/0d78c5e59.jpg'
    fullbg_url = 'http://static.geetest.com/pictures/gt/c81e728d9/c81e728d9.jpg'
    request_client = ResquestSession()
    cookies = request_client.spider_cookies
    distance = generate_distance(bg_url, fullbg_url, request_client,cookies)
    print(distance)