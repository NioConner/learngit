# -*- coding: utf-8 -*-

from sc_text.sc_getpicinfo import sc_pic

def get_pic_url():
    #img是获取到
    get_img = sc_pic()
    img_info = get_img.get_picture()

    #拼链接地址
    bg = 'http://static.geetest.com/pictures/gt/{}/bg/{}.jpg'.format(img_info[0],img_info[1])
    fullbg = 'http://static.geetest.com/pictures/gt/{}/{}.jpg'.format(img_info[0],img_info[0])
    slic = 'http://static.geetest.com/pictures/gt/{}/slice/{}.png'.format(img_info[0],img_info[1])
    print(bg , fullbg ,slic,img_info[2])





get_pic_url()