# -*- coding:utf-8 -*-
import cv2
import time
from Adb import Adb

path = './screenshot'


# 点击观看广告
def ad_start():
    png_file = Adb.screen_shot(png_name, path)
    img = cv2.imread(png_file, 0)
    threshold = 0.975
    ad_pos = {'x0': 945, 'y0': 255, 'x1': 1045, 'y1': 345}
    ad_template = cv2.imread(path + '/ad_template.png', 0)

    ad = img[ad_pos['y0']:ad_pos['y1'], ad_pos['x0']:ad_pos['x1']]
    match_rate = cv2.matchTemplate(ad, ad_template, cv2.TM_CCOEFF_NORMED)
    # print('start:')
    # print(match_rate)
    if (match_rate > threshold).any():
        Adb.tap_random(ad_pos['x0'] + 20, ad_pos['y0'] + 20, ad_pos['x1'] - 20, ad_pos['y1'] - 20)
        time.sleep(1)
        Adb.tap_random(590, 1450, 960, 1520)


# 关闭广告
def ad_close():
    png_file = Adb.screen_shot(png_name, path)
    img = cv2.imread(png_file, 0)
    is_close = 0
    # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100, maxRadius=50)
    # for circle in circles[0, :]:
    #     print(circle)
    #     tap(circle[0], circle[1])
    #
    top_right_close_pos1 = {'x0': 955, 'y0': 115, 'x1': 1040, 'y1': 200}
    top_right_close_template1 = path + '/top_right_close_template1.png'
    is_close += ad_close_template(img, top_right_close_pos1, top_right_close_template1)

    top_right_close_pos2 = {'x0': 940, 'y0': 115, 'x1': 1040, 'y1': 215}
    top_right_close_template2 = path + '/top_right_close_template2.png'
    is_close += ad_close_template(img, top_right_close_pos2, top_right_close_template2)

    top_right_close_pos3 = {'x0': 950, 'y0': 125, 'x1': 1030, 'y1': 205}
    top_right_close_template3 = path + '/top_right_close_template3.png'
    is_close += ad_close_template(img, top_right_close_pos3, top_right_close_template3)

    return is_close


# 根据模板关闭广告
def ad_close_template(img, close_pos, close_template_name):
    threshold = 0.85
    close_template = cv2.imread(close_template_name, 0)

    close = img[close_pos['y0']:close_pos['y1'], close_pos['x0']:close_pos['x1']]

    match_rate = cv2.matchTemplate(close, close_template, cv2.TM_CCOEFF_NORMED)
    # print(close_template_name)
    # print(match_rate)
    if (match_rate > threshold).any():
        Adb.tap_random(close_pos['x0'] + 20, close_pos['y0'] + 20, close_pos['x1'] - 20, close_pos['y1'] - 20)
        time.sleep(2)
        Adb.tap_random(270, 585, 270 * 3, 585 * 3)
        return 1

    return 0


def force_close():
    Adb.tap(1000, 160)
    time.sleep(2)
    Adb.tap_random(270, 585, 270 * 3, 585 * 3)


# 自动看广告
def ad_auto():
    check_cnt = 0
    while True:
        ad_start()
        if not ad_close():
            check_cnt += 1
        else:
            check_cnt = 0
        if check_cnt > 20:
            force_close()
            check_cnt = 0
            print('force')
        time.sleep(2)


png_name = 'liao_li_wang'

if __name__ == '__main__':
    ad_auto()

    # png_file = screen_shot(png_name)
    # img = cv2.imread(png_file, 0)
    # img = img[120:210, 945:1035]
    # cv2.imwrite('./screenshot/top_right_close_template4.png', img)
    # img = img[100:250, 900:1080]
    # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 1, maxRadius=50)
    # print(circles)
    # for i in circles[0, :]:
    #     print(i)
    #     cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #     cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    # cv2.imshow('click', img)
    # cv2.waitKey(0)
