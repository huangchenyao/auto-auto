# -*- coding:utf-8 -*-

import os
import random


class Adb:
    # 模拟点按
    @staticmethod
    def tap(x0, y0):
        tap_cmd = 'adb shell input tap {x0} {y0}'.format(
            x0=x0,
            y0=y0
        )
        print(tap_cmd)
        os.system(tap_cmd)

    # 模拟点按（随机范围，防封）
    @staticmethod
    def tap_random(x0, y0, x1, y1):
        x = random.randint(x0, x1)
        y = random.randint(y0, y1)
        Adb.tap(x, y)

    # 模拟滑动
    @staticmethod
    def swipe(x0, y0, x1, y1, delay):
        cmd = 'adb shell input swipe {x0} {y0} {x1} {y1} {delay}'.format(
            x0=x0,
            y0=y0,
            x1=x1,
            y1=y1,
            delay=delay
        )
        print(cmd)
        os.system(cmd)

    # 截图
    @staticmethod
    def screen_shot(png_name, path):
        screen_cap_cmd = 'adb shell screencap -p /sdcard/{name}.png'.format(name=png_name)
        os.system(screen_cap_cmd)
        pull_cmd = 'adb pull /sdcard/{name}.png {path}'.format(name=png_name, path=path)
        os.system(pull_cmd)
        return '{path}/{name}.png'.format(name=png_name, path=path)
