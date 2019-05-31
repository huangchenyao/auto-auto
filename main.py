# -*- coding:utf-8 -*-
import cv2
from Liaoliwang import Liaoliwang

if __name__ == '__main__':
    path = './screenshot'
    png_name = 'liao_li_wang'

    Liaoliwang(path, png_name).ad_auto()

    # png_file = Adb.screen_shot(png_name, path)
    # img = cv2.imread(png_file, 0)
    # img = img[120:210, 60:150]
    # cv2.imwrite('./screenshot/top_left_close_template2.png', img)
    # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 1, maxRadius=50)
    # print(circles)
    # for i in circles[0, :]:
    #     print(i)
    #     cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #     cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    # cv2.imshow('click', img)
    # cv2.waitKey(0)
