# -*- coding:utf-8 -*-
import cv2
from Adb import Adb
from Liaoliwang import Liaoliwang
import numpy as np

if __name__ == '__main__':
    path = './screenshot'
    png_name = 'liao_li_wang'

    Liaoliwang(path, png_name).ad_auto()
    # Liaoliwang(path, png_name).adventure_auto()

    # img = cv2.imread('./screenshot/tmp.png', 0)
    #
    # treasure = img[1275:1330, 902:967]
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    # circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 20,
    #                            param1=50, param2=30, minRadius=30, maxRadius=35)
    #
    # for i in circles[0, :]:
    #     print((int(i[0]), int(i[1])))

    # cv2.imwrite('./screenshot/box.png', treasure)
