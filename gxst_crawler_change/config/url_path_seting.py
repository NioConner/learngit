# -*- coding: utf-8 -*-
import os

gsxt_url = 'http://www.gsxt.gov.cn/index.html'
search_item_captcha_url = 'http://www.gsxt.gov.cn/SearchItemCaptcha?v={}'
gettype_url = 'http://api.geetest.com/gettype.php?gt={}&callback=geetest_{}'
pic_url = 'http://api.geetest.com/get.php?gt={}&challenge={}&product=popup&offline=fa' \
          'lse&protocol=&type=slide&path=/static/js/geetest.5.10.10.js&callback=geetest_{}'
for_token_url = 'http://www.gsxt.gov.cn/corp-query-custom-geetest-image.gif?v={}'
open_geetest_url = 'http://www.gsxt.gov.cn/corp-query-geetest-validate-input.html?token={}'
for_validate_url = 'http://api.geetest.com/ajax.php?gt={}&challenge={}&userresponse={}&passtime={}&imgload={}' \
                   '&a={}&callback=geetest_{}'
abs_parent_path = '/Users/nioconner/Desktop/gxst_crawler_change/'
# abs_parent_path = '/Users/chinadaas/Desktop/PY_WORK_SPACE/gxst_crawler_linux/'
# abs_parent_path = '/root/Py_Work_Space/gxst_crawler_linux/'
abs_file_path = '{}resource/content_file/'.format(abs_parent_path)
abs_track_path = '{}resource/track_file/'.format(abs_parent_path)
# abs_post_path = 'http://newdaas.bidata.com.cn/srs/newdaasBRResultService/uploadTaskResult'
abs_result_path = '{}resource/result_temp'.format(abs_parent_path)


if __name__ == '__main__':
    print(os.getcwd())
