# -*- coding:utf-8 -*-
import cv2
import time
from tools.Adb import Adb
import numpy as np


class Jiaguomeng(object):
    __screenshot_path = ''
    __png_name = ''
    __template_path = './template/jiaguomeng'
    __pos = {
        'gangtiechang': [300, 950, 1],  # 钢铁厂0
        'lingjianchang': [550, 850, 0],  # 零件厂0
        'qiejixie': [800, 750, 1],  # 企鹅机械
        'bianlidian': [300, 1200, 1],  # 便利店
        'wujindian': [550, 1100, 1],  # 五金店
        'minshizhai': [800, 1000, 1],  # 民食斋
        'juminlou': [300, 1450, 1],  # 居民楼
        'pingfang': [550, 1350, 0],  # 平房
        'gangjiegoufang': [800, 1250, 1],  # 钢结构房
    }
    __houses = []

    def __init__(self, screenshot_path, png_name):
        self.__screenshot_path = screenshot_path
        self.__png_name = png_name
        for k in self.__pos:
            if self.__pos[k][2]:
                self.__houses.append(k)
        print(self.__houses)

    def auto(self):
        while True:
            has_train = self.auto_train()
            if not has_train:
                time.sleep(2)
                self.__auto_tap()

    def __auto_tap(self):
        for k in self.__pos:
            Adb.tap_random(self.__pos[k][0] - 25,
                           self.__pos[k][1] - 25,
                           self.__pos[k][1] + 25)
            time.sleep(0.25)

    def auto_train(self):
        template = False
        if template:
            img = cv2.imread('./screenshot/jia_guo_meng.png')[1850:1920, 620:700]  # 1
            # img = cv2.imread('./screenshot/jia_guo_meng.png')[1775:1835, 780:860]  # 2
            # img = cv2.imread('./screenshot/jia_guo_meng.png')[1690:1750, 930:1010] # 3
            cv2.imwrite('./template/jiaguomeng/juminlou.png', img)
            return

        png_file = Adb.screen_shot(self.__png_name, self.__screenshot_path)
        img = cv2.imread(png_file, 0)
        for house in self.__houses:
            center = self.__find_center(img, house)
            if center:
                Adb.swipe(center[0], center[1], self.__pos[house][0], self.__pos[house][1], 250)
                return True
        return False

    def __find_center(self, img, template_name):
        center = ()
        template = cv2.imread('./template/jiaguomeng/' + template_name + '.png', 0)
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.8:
            center = (max_loc[0] + 30, max_loc[1] + 30)
        return center
