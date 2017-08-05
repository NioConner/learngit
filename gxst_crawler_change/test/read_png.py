# -*- coding: utf-8 -*-
# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image, ImageFont, ImageDraw
import os
import requests
from config.proxysetting import proxies

# class GetImageDate(object):
#     def getresults(self):
#         """
#         Parameters
#         ----------
#         resultFolder: results directory
#         imgFolder: image directory
#         """
#         # Windows
#         # cmd = 'cmd.exe /k tesseract.exe ' + img + 'result -l chi_sim+eng'
#
#         # OS X
#         # cmd = 'tesseract ' + img + ' result -l chi_sim'
#
#         # cmd = 'tesseract ' + imgList[i] + resultFile + ' -l chi_sim'
#         cmd = 'tesseract ' + 'ttt.jpg' + 'result -l chi_sim'
#         os.popen(cmd)
#
#     def m(self):
#         image = Image.open('ttttt.png')
#         image.load()
#         print(image.size)
#
#         background = Image.new("RGB", (29, 14), (255, 255, 255))
#         background.paste(image, mask=image.split()[3])
#
#         background.show()
#         background.save('sss.jpg')
#
#         text = pytesseract.image_to_string(background)
#         return text
#
#     def SaveResultToDocument(self):
#         text = self.m()
#         # f = open()
#         print(text)
#         # f.write(str(text))
#         # f.close()
#
#     def make_img(self):
#         background = Image.new("RGB", (29, 14), (255, 255, 255))
#         dr = ImageDraw.Draw(background)
#         text = '理'
#         font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 14)
#         dr.text((0, 0), text, font=font)
#         background.show()
#         # background.paste(chr)
#         # background.convert('L')
#         # background.save('jingli.jpg')
#
#
# g = GetImageDate()
# g.make_img()
# g.SaveResultToDocument()
# g.getresults()
if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

    inv_headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.gsxt.gov.cn',
        'Origin': 'http://www.gsxt.gov.cn',
        'Referer': '',
        'User-Agent': user_agent,
        'X-Requested-With': 'XMLHttpRequest',
        '___SEEKS_PROXY_USERID': 'newdaas_br',
        '___SEEKS_PROXY_ALLOW_CHANGE_IP': '0',
    }
    url = 'http://www.gsxt.gov.cn/%7B9NnuIHRRDUg550Eap5s5dJi9A-FcNQz64HcbmoE5UAdU96kKKcH4wGZ2zGup_ULFr-MfwMrkethvEJeNYmEcgJXeToAhYyXZp8TEkxThCbANwE0UP23zxlw4I0YoyAYy-1500862442613%7D'
    draw = 0
    start = 0
    temp_data = {
        'draw': draw,
        'start': start,
        'length': '5',
    }
    cookies = None
    content = requests.post(url, headers=inv_headers, cookies = cookies,data=temp_data, proxies=proxies)
    print(content.content.decode('utf-8'))
