# -*- coding: utf-8 -*-
from PIL import Image
from io import BytesIO
from config.headersetting import *
from config.proxysetting import *
import os
from config.url_path_seting import abs_parent_path

pic_coord_list = [[157, -58], [145, -58], [265, -58], [277, -58], [181, -58], [169, -58], [241, -58], [253, -58],
                  [109, -58], [97, -58], [289, -58], [301, -58], [85, -58], [73, -58], [25, -58], [37, -58], [13, -58],
                  [1, -58], [121, -58], [133, -58], [61, -58], [49, -58], [217, -58], [229, -58], [205, -58],
                  [193, -58], [145, 0], [157, 0], [277, 0], [265, 0], [169, 0], [181, 0], [253, 0], [241, 0], [97, 0],
                  [109, 0], [301, 0], [289, 0], [73, 0], [85, 0], [37, 0], [25, 0], [1, 0], [13, 0], [133, 0], [121, 0],
                  [49, 0], [61, 0], [229, 0], [217, 0], [193, 0], [205, 0]]


def distance_judge(pic, pic_new):
    if pic is None or pic_new is None:
        d = 0
        return d
    xlen = pic.size[0]
    ylen = pic.size[1]
    for x in range(0, xlen):
        for y in range(0, ylen):
            p1 = pic.getpixel((x, y))
            p2 = pic_new.getpixel((x, y))
            # 检查rgb的色差
            for i in range(0, 3):
                num = abs(p1[i] - p2[i])
                if num > 100:
                    return x - 6
    d = 0
    return d


def range_pic(pic_list, pic):
    new_pic = Image.new("RGB", (260, 116))
    up_list = []
    down_list = []
    for p_l in pic_list:
        if p_l[1] == -58:
            up_list.append(pic.crop(
                (abs(p_l[0]), 58, abs(p_l[0]) + 10, 116))
            )
        if p_l[1] == 0:
            down_list.append(pic.crop(
                (abs(p_l[0]), 0, abs(p_l[0]) + 10, 58))
            )
    xoffset = 0
    for up in up_list:
        new_pic.paste(up, (xoffset, 0))
        xoffset = xoffset + up.size[0]

    xoffset = 0
    for down in down_list:
        new_pic.paste(down, (xoffset, 58))
        xoffset = xoffset + down.size[0]
    return new_pic


def get_pic(url, session, cookies, num=0):
    try:
        pic_res = session.do_get(url, headers=pic_headers, cookies=cookies, proxies=proxies)
        img1 = BytesIO(pic_res.content)
        pic = Image.open(img1)
        return pic
    except:
        if num < 3:
            num += 1
            get_pic(url, session, cookies)
            return
        else:
            pic = None
            print('can not get pic_res')
            return pic


def generate_distance(bg_url, fullbg_url, session, cookies):
    bg_pic = get_pic(bg_url, session, cookies)
    fullbg_pic = get_pic(fullbg_url, session, cookies)
    try:
        bg_pic_path = '{}/resource/bg_pic.jpg'.format(abs_parent_path)
        fullbg_pic_path = '{}/resource/fullbg_pic.jpg'.format(abs_parent_path)
        # print(bg_pic_path)
        bg_pic.save(bg_pic_path)
        fullbg_pic.save(fullbg_pic_path)
        bg_new = range_pic(pic_coord_list, bg_pic)
        bg_new_path = '{}/resource/bg_new.jpg'.format(abs_parent_path)
        bg_new.save(bg_new_path)

        fullbg_new = range_pic(pic_coord_list, fullbg_pic)
        fullbg_new_path = '{}/resource/fullbg_new.jpg'.format(abs_parent_path)
        fullbg_new.save(fullbg_new_path)
        return distance_judge(fullbg_new, bg_new)
    except:
        return distance_judge(None, None)
