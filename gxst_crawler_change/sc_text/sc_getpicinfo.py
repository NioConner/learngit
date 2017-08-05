# -*- coding: utf-8 -*-
import random
import hashlib

class sc_pic(object):
    #这里的c d都是计算过程里都参数无实际意义
    def get_x(self,x_dis):
        if len(x_dis)==5:
            b = 200
            try:
                c = int(x_dis,16)
            except:
                c = 0
            d = c%b
            if d<40:
                d = 40
            return d



    def get_y(self):
        pass

    def get_picture(self):
        #生成随机数
        firs_num = int(random.random()*6)
        sec_num = int(random.random()*300)
        #将生成的随机数进行md5加密
        firs_md5 = hashlib.md5(str(firs_num).encode(encoding='utf-8')).hexdigest()
        sec_md5 = hashlib.md5(str(sec_num).encode(encoding='utf-8')).hexdigest()
        img_file_name = firs_md5[:9]
        img_name = sec_md5[10:19]
        #用两个不同的字符串来拼x距离需要的字符串
        x_dis = img_file_name[4]+img_name[5]+img_file_name[6]+img_name[7]+img_file_name[8]
        x_distance = self.get_x(x_dis)
        #将这三个部分返回
        return img_file_name,img_name,x_distance,firs_num,sec_num
        #这里的firs_num,sec_num在后面是有用到的





# def main():
#     b = sc_pic()
#     c = b.get_picture()
#     print(c)
#
# if __name__ == '__main__':
#     main()