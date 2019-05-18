# -*- coding:utf-8 -*-
import os
import cv2
import random
import time


# 模拟点按
def tap(x0, y0):
    tap_cmd = 'adb shell input tap {x0} {y0}'.format(
        x0=x0,
        y0=y0
    )
    print(tap_cmd)
    os.system(tap_cmd)


# 模拟点按
def tap_random(x0, y0, x1, y1):
    x = random.randint(x0, x1)
    y = random.randint(y0, y1)
    tap(x, y)


# 截图
def screen_shot(png_name):
    screen_cap_cmd = 'adb shell screencap -p /sdcard/{name}.png'.format(name=png_name)
    os.system(screen_cap_cmd)
    pull_cmd = 'adb pull /sdcard/{name}.png ./screenshot'.format(name=png_name)
    os.system(pull_cmd)
    return './screenshot/{name}.png'.format(name=png_name)


# 点击观看广告
def ad_start():
    png_file = screen_shot(png_name)
    img = cv2.imread(png_file, 0)
    threshold = 0.99
    ad_pos = {'x0': 945, 'y0': 255, 'x1': 1045, 'y1': 345}
    ad_template = cv2.imread('./screenshot/ad_template.png', 0)

    ad = img[ad_pos['y0']:ad_pos['y1'], ad_pos['x0']:ad_pos['x1']]
    match_rate = cv2.matchTemplate(ad, ad_template, cv2.TM_CCOEFF_NORMED)
    # print('start:')
    # print(match_rate)
    if (match_rate > threshold).any():
        tap_random(ad_pos['x0'] + 20, ad_pos['y0'] + 20, ad_pos['x1'] - 20, ad_pos['y1'] - 20)
        time.sleep(1)
        tap_random(590, 1450, 960, 1520)


# 关闭广告
def ad_close():
    png_file = screen_shot(png_name)
    img = cv2.imread(png_file, 0)

    top_right_close_pos1 = {'x0': 950, 'y0': 110, 'x1': 1050, 'y1': 210}
    top_right_close_template1 = './screenshot/top_right_close_template1.png'
    ad_close_template(img, top_right_close_pos1, top_right_close_template1)

    top_right_close_pos2 = {'x0': 940, 'y0': 115, 'x1': 1040, 'y1': 215}
    top_right_close_template2 = './screenshot/top_right_close_template2.png'

    ad_close_template(img, top_right_close_pos2, top_right_close_template2)


# 根据模板关闭广告
def ad_close_template(img, close_pos, close_template_name):
    threshold = 0.85
    close_template = cv2.imread(close_template_name, 0)

    close = img[close_pos['y0']:close_pos['y1'], close_pos['x0']:close_pos['x1']]

    match_rate = cv2.matchTemplate(close, close_template, cv2.TM_CCOEFF_NORMED)
    # print(close_template_name)
    # print(match_rate)
    if (match_rate > threshold).any():
        tap_random(close_pos['x0'] + 20, close_pos['y0'] + 20, close_pos['x1'] - 20, close_pos['y1'] - 20)
        time.sleep(2)
        tap_random(270, 585, 270 * 3, 585 * 3)


# 自动看广告
def ad_auto():
    while True:
        ad_start()
        ad_close()
        time.sleep(2)


png_name = 'liao_li_wang'

if __name__ == '__main__':
    ad_auto()

    # png_file = screen_shot(png_name)
    # img = cv2.imread(png_file, 0)
    # click = img[115:215, 940:1040]
    # cv2.imwrite('top_right_close_template2.png', click)
    # cv2.imshow('click', click)
    # cv2.waitKey(0)
