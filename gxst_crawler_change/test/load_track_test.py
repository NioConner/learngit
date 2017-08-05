# -*- coding: utf-8 -*-
import os
import re
import random
import json
from utils.create_track_utils import CreateTracklUtils


class TrackTxtManager(object):
    def __init__(self):
        self.parent_path = '../resource/track_file'
        self.record_path = None

    def load_distance_list(self):
        parent_path = self.parent_path
        distance_list = os.listdir(parent_path)
        return distance_list

    def load_txt(self, distance):
        path = '../resource/track_file/{}'.format(distance)
        path_list = os.listdir(path)
        if len(path_list) == 0:
            distance_track = CreateTracklUtils().create_action(distance)
            return distance_track
        else:
            choice = random.randint(0, len(path_list))
            choice_path = path + '/{}.txt'.format(str(choice))
            self.record_path = choice_path
            with open(choice_path, 'a') as f:
                track = f.read()
            track_list = eval(track)
        return track_list

    def query_distance(self, distance):
        distance_list = self.load_distance_list()
        i = -2
        while i <= 3:
            if str(distance + i) in distance_list:
                distance_track = self.load_txt(str(distance + i))
                break
            else:
                if i < 3:
                    i += 1
                    continue
                distance_track = CreateTracklUtils().create_action(distance)
        return distance_track

    # 创建txt的程序
    @staticmethod
    def write_txt(arr, file_path):
        file_path_list = os.listdir(file_path)
        try:
            f_name = file_path + '/{}.txt'.format(
                str(
                    int(
                        re.findall('[0-9]+', file_path_list[len(file_path_list) - 1])[0]) + 1
                )
            )
            print(f_name)
        except:
            f_name = file_path + '/0.txt'
        with open(f_name, 'a+') as f:
            f.write(str(arr['arr']))

    def create_file(self, dress, t):
        fl = os.listdir(dress)
        path = str(t['distance'])
        tar = '../resource/track_file/{}'.format(path)
        if path not in fl:
            os.mkdir(tar)
            self.write_txt(t, tar)
        else:
            self.write_txt(t, tar)

    def delete_txt(self):
        path = self.record_path
        # path = '../resource/track_file/{}/{}.txt'.format(str(distance), str(file_name))
        try:
            os.remove(path)
        except:
            print('remove path failed!')
        self.record_path = None


'''
track_txt_manager.load_distance_list 得到已有位置的list
track_txt_manager.query 进行位置的查找，有则调用，没有则计算
'''
track_txt_manager = TrackTxtManager()

# if __name__ == '__main__':
#     with open('../resource/train.txt', 'r+') as fi:
#         track = fi.read()
#     print(track)
#     tj = json.loads(track)
#
#     dr = '../resource/track_file'
#     # tj_a = tj[:3]
#
#     # for t in tj:
#     #     create_file(dr, t)


"""
 if str(distance) in distance_list:

            while i < 3:

        distance_track = self.load_txt(str(distance))
            return distance_track
        elif str(distance + 1) in distance_list:

            return distance_track
        elif str(distance + 2) in distance_list:
            distance_track = self.load_txt(str(distance + 2))
            return distance_track
        elif str(distance - 1) in distance_list:
            distance_track = self.load_txt(str(distance - 1))
            return distance_track
        elif str(distance - 2) in distance_list:
            distance_track = self.load_txt(str(distance - 2))
            return distance_track
        else:
"""

'''
track_txt_manager.load_distance_list 得到已有位置的list
track_txt_manager.query 进行位置的查找，有则调用，没有则计算
'''
track_txt_manager = TrackTxtManager()

if __name__ == '__main__':
    # ../resource/track_file/39/0.txt
    t = os.listdir('../resource/track_file')
    print(t)
    # with open('../resource/track_file/', 'r+') as fi:
    #     track = fi.read()
    # print(track)
    # s = eval(track)
    # print(type(s))
    # s = list(track)
    # print(s)
    # print(type(s))

    # print(type(list[track]))
#     tj = json.loads(track)
#
#     dr = '../resource/track_file'
#     # tj_a = tj[:3]
#
#     # for t in tj:
#     #     create_file(dr, t)
