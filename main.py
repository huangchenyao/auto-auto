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


def ad_start():
    png_file = screen_shot(png_name)
    img = cv2.imread(png_file, 0)
    threshold = 0.85
    ad_pos = {
        'x0': 945,
        'y0': 255,
        'x1': 1045,
        'y1': 345,
    }

    ad_template = cv2.imread('./screenshot/ad_template.png', 0)
    ad = img[ad_pos['y0']:ad_pos['y1'], ad_pos['x0']:ad_pos['x1']]
    match_rate = cv2.matchTemplate(ad, ad_template, cv2.TM_CCOEFF_NORMED)
    if (match_rate > threshold).any():
        tap_random(ad_pos['x0'] + 20, ad_pos['x1'] - 20, ad_pos['y0'] + 20, ad_pos['y1'] - 20)
        time.sleep(2)


def ad_close():
    pass


png_name = 'liao_li_wang'

if __name__ == '__main__':
    ad_start()

    png_file = screen_shot(png_name)
    img = cv2.imread(png_file, 0)
