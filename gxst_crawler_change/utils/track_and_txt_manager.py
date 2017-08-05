# -*- coding: utf-8 -*-
import os, zipfile, tarfile
import requests
import re
import random
import json
from utils.create_track_utils import CreateTracklUtils
import base64
import subprocess
import shutil
from config.url_path_seting import abs_file_path, abs_track_path, abs_result_path


class TrackTxtManager(object):
    def __init__(self):
        self.parent_path = abs_track_path
        self.record_path = None
        self.use_track = False

    def load_distance_list(self):
        parent_path = self.parent_path
        distance_list = os.listdir(parent_path)
        return distance_list

    def load_txt(self, distance):
        path = self.parent_path + str(distance)
        path_list = os.listdir(path)
        if len(path_list) == 0:
            distance_track = CreateTracklUtils().create_action(distance)
            return distance_track
        else:
            choice = random.randint(0, len(path_list) - 1)
            choice_path = path + '/{}.txt'.format(str(choice))
            abspath = os.path.abspath(choice_path)
            self.record_path = choice_path
            with open(abspath, 'r') as f:
                track = f.read()
            track_list = eval(track)
        return track_list

    def query_distance(self, distance):
        if self.use_track:
            self.use_track = False
            distance_track = CreateTracklUtils().create_action(distance)
            return distance_track

        distance_list = self.load_distance_list()
        i = -1
        while i <= 2:
            if str(distance + i) in distance_list:
                try:
                    distance_track = self.load_txt(str(distance + i))
                    self.use_track = True
                    break
                except:
                    i += 1
                    continue
            else:
                if i < 2:
                    i += 1
                    continue
                self.use_track = False
                distance_track = CreateTracklUtils().create_action(distance)
        return distance_track

    # 创建txt的程序
    @staticmethod
    def write_txt(abs_p, move_list):
        file_path_list = os.listdir(abs_p)
        try:
            f_name = abs_p + '/{}.txt'.format(
                str(
                    int(
                        re.findall('[0-9]+', file_path_list[len(file_path_list) - 1])[0]) + 1
                )
            )
            print(f_name)
        except:
            f_name = abs_p + '/0.txt'
        abs_f_name = os.path.abspath(f_name)
        with open(abs_f_name, 'a+') as f:
            f.write(str(move_list))

    def create_file(self, distance, move_list):
        fl = os.listdir(self.parent_path)
        distance_path = str(distance)
        abs_p = os.path.abspath(self.parent_path + distance_path)

        if distance_path not in fl:
            os.mkdir(abs_p)
            self.write_txt(abs_p, move_list)
        else:
            self.write_txt(abs_p, move_list)

    def delete_txt(self):
        if self.record_path is not None:
            abs_path = os.path.abspath(self.record_path)
        else:
            return
        try:
            os.remove(abs_path)
            self.use_track = False
        except:
            print('remove path failed!')
        self.record_path = None


'''
track_txt_manager.load_distance_list 得到已有位置的list
track_txt_manager.query 进行位置的查找，有则调用，没有则计算
'''


class ContentTxtManger(object):
    # def __init__(self, task_id):
    #     self.uuid = task_id

    # 创建txt的程序
    @staticmethod
    def write_txt(abs_p, target):
        print(type(target))
        with open(abs_p, 'a+') as f:
            json.dump(target, f, ensure_ascii=False, indent=4)

    def write_inv_detaile(self, child_file_path, detail_list):
        if detail_list is None:
            return
        for detail in detail_list:
            d_path = os.path.abspath(
                child_file_path + '/{}.json'.format(str(detail['invId']))
            )
            print(detail['detail_js'])
            print(type(detail['detail_js']))
            self.write_txt(d_path, detail['detail_js'])

    @staticmethod
    def check_position(new_position):
        new_position = re.sub('\s', '', new_position)
        if new_position == '经一理':
            new_position = '经理'
        elif new_position == '主理事长':
            new_position = '理事长'
        else:
            pass
        return new_position

    def write_person_img(self, child_file_path, img_list):
        if len(img_list) == 0:
            return
        name_list = []
        for img in img_list:
            name = img['perId']
            img_data = img['position_CN']
            if 'data' not in img_data:
                continue
            head, data = img_data.split(',', 1)
            file_ext = head.split(';')[0].split('/')[1]
            img_path = os.path.abspath(
                child_file_path + '/' + name + '.{}'.format(file_ext)
            )
            name_list.append(img_path)
            plain_data = base64.b64decode(data)

            f = open(img_path, 'wb')
            f.write(plain_data)
            f.close()

            abs_path = os.path.abspath(img_path)
            result_path = abs_result_path
            cmd = 'tesseract ' + abs_path + ' {} -l fontyp -psm 7'.format(result_path)
            subprocess.run(cmd, shell=True)
            with open(result_path + '.txt', 'r') as f:
                new_position = f.read()
            new_position = self.check_position(new_position)
            print('new_position is', new_position)
            img['position_CN'] = new_position
        return img_list

    def save_html(self, content):
        if len(content) == 0:
            return
        html_path = os.path.abspath(self.save_path + '/busilice.html')
        self.write_txt(html_path, content)

    def save_person_txt(self, content_list, url_type, img_list=None):
        if img_list is None:
            img_list = []
        if len(content_list) == 0:
            return
        child_path = '/{}'.format(url_type)
        child_file_path = os.path.abspath(
            self.save_path + child_path
        )
        os.mkdir(child_file_path)
        child_txt_path = os.path.abspath(
            child_file_path + '/{}.json'.format(url_type)
        )
        if len(img_list) != 0:
            img_list = self.write_person_img(child_file_path, img_list)
            content_list = self.update_content_list(content_list, img_list)
        self.write_txt(child_txt_path, content_list)

    def save_txt(self, content_list, url_type, detail_list=None):
        if detail_list is None:
            detail_list = []
        if len(content_list) == 0:
            return
        child_path = '/{}'.format(url_type)
        if url_type == 'inv' or url_type == 'person':
            child_file_path = os.path.abspath(
                self.save_path + child_path
            )
            os.mkdir(child_file_path)
            child_txt_path = os.path.abspath(
                child_file_path + '/{}.json'.format(url_type)
            )
        else:
            child_txt_path = os.path.abspath(
                self.save_path + child_path + '.json'
            )
        self.write_txt(child_txt_path, content_list)
        if len(detail_list) != 0:
            self.write_inv_detaile(child_file_path, detail_list)

    def zip_func(self):
        child_file_path = self.save_path
        zip_name = child_file_path + '.zip'
        zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        pre_len = len(os.path.dirname(child_file_path))
        for parent, dirnames, filenames in os.walk(child_file_path):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
        zipf.close()
        os.chdir(child_file_path)

    def make_zip(source_dir, output_filename):
        zipf = zipfile.ZipFile(output_filename, 'w')
        pre_len = len(os.path.dirname(source_dir))
        for parent, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
        zipf.close()

    def gzip_func(self, path):
        child_file_path = path
        zip_name = child_file_path + '.gz'
        self.out_put_path = zip_name
        with tarfile.open(zip_name, "w:gz") as tar:
            tar.add(child_file_path, arcname=os.path.basename(child_file_path))
        os.chdir(child_file_path)

    def delete_file_zip(self):
        file_path = self.save_path
        zip_path = file_path + '.zip'
        if os.path.exists(file_path):
            shutil.rmtree(file_path)
        if os.path.exists(zip_path):
            os.remove(zip_path)

    def data_post(self, ent_type):
        # post_url = 'http://newdaas.bidata.com.cn/srs/newdaasBRResultService/uploadTaskResult'
        post_url = 'http://192.168.205.41/srs/newdaasBRResultService/uploadTaskResult'
        # post_url = abs_post_path
        print(self.save_path)
        path = os.path.abspath(self.save_path + '.zip')

        task_id = self.uuid
        name = task_id + '.zip'
        files = {
            'file': open(path, 'rb')
            # 'file': open(path, 'rb')
        }
        if ent_type is None:
            ent_type = 'Null'
        data = {'FILE_NAME': name, 'TASK_ID': task_id, 'ENT_TYPE': ent_type, 'KEY_WORD': self.key_word}
        print('ent_type is', ent_type)
        # try:
        #     r = requests.post(post_url, data=data, files=files)
        #     print(r)
        # except:
        #     print('========服务器挂了吧？==========')
        # self.delete_file_zip()

    def create_file(self, history_name=None):
        abs_path = abs_file_path
        file_name = abs_path + self.uuid
        self.save_path = file_name
        judge = os.path.exists(file_name)
        print('judge is', judge)
        if judge:
            shutil.rmtree(file_name)
        os.mkdir(file_name)
        if history_name is not None:
            history_name_path = abs_path + self.uuid + '/history_name.txt'
            with open(history_name_path, 'w') as f:
                f.write(history_name)

    @staticmethod
    def update_content_list(content_list, img_list):
        for content in content_list[0]['data']:
            for img in img_list:
                if content['perId'] == img['perId']:
                    content['position_CN'] = img['position_CN']
                    continue
        print(content_list)
        return content_list

    def __init__(self, key_word, task_id, history_name=None):
        # self.parent_path = './resource/content_file/'
        self.save_path = ''
        self.out_put_path = ''
        self.uuid = task_id
        self.key_word = key_word
        self.history_name = history_name
        self.create_file(self.history_name)
        # zip_path = os.path.abspath(
        #     './resource/content_file/zip_test'
        # )


track_txt_manager = TrackTxtManager()

if __name__ == '__main__':
    t = ContentTxtManger()
