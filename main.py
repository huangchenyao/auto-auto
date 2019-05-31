# -*- coding:utf-8 -*-
import cv2
from Adb import Adb
from Liaoliwang import Liaoliwang

if __name__ == '__main__':
    path = './screenshot'
    png_name = 'liao_li_wang'

    Liaoliwang(path, png_name).ad_auto()

    # png_file = Adb.screen_shot(png_name, path)
    # img = cv2.imread(png_file, 0)
    # img = img[120:210, 945:1035]
    # cv2.imwrite('./screenshot/top_right_close_template6.png', img)
