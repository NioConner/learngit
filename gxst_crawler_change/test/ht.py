# -*- coding: utf-8 -*-
from test.html_test import html_text
from lxml import etree
import re

html = etree.HTML(html_text)
dl = html.xpath('//div[@class="overview"]/dl')
d = ''
for d in dl:
    item = re.sub(
        '：', '', str(d.xpath('./dt/text()')[0])
    )
    result = re.sub(
        '\s', '', str(d.xpath('./dd/text()')[0])
    )
    if item == '类型':
        if '个体' in result:
            d = 'gt'
        else:
            d = 'ent'
        break
        # print(item)
        # print(result)
        #     print(True)
        # else:
        #     print(False)
print(d)
