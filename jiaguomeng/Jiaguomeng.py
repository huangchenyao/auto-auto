# -*- coding:utf-8 -*-
import cv2
import time
from tools.Adb import Adb


class Jiaguomeng(object):
    __zoom_x: float = 1
    __zoom_y: float = 1

    __screenshot_path: str = ''
    __png_name: str = ''
    __template_path: str = './template/jiaguomeng'
    __pos: dict = {
        '企鹅机械': [300, 950, 3],  # 橙色
        '零件厂': [550, 850, 2 - 2],  # 紫色
        '人民石油': [550, 850, 3],  # 橙色
        '电厂': [800, 750, 1],  # 蓝色
        '商贸中心': [300, 1200, 2],  # 紫色
        '民食斋': [550, 1100, 3],  # 橙色
        '五金店': [800, 1000, 1 - 1],  # 蓝色
        '媒体之声': [800, 1000, 3],  # 橙色
        '复兴公馆': [300, 1450, 3],  # 橙色
        '花园洋房': [550, 1350, 2],  # 紫色
        '小型公寓': [800, 1250, 1],  # 蓝色
    }
    __houses: list = []

    def __init__(self, screenshot_path: str, png_name: str, level: int = 1):
        self.__screenshot_path = screenshot_path
        self.__png_name = png_name
        for k in self.__pos:
            if self.__pos[k][2] >= level:
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
                           self.__pos[k][0] + 25,
                           self.__pos[k][1] + 25)
            time.sleep(0.25)

    def auto_train(self, template=False) -> bool:
        # template = False
        if template:
            img1 = cv2.imread('./screenshot/jia_guo_meng.png')[1855:1920, 625:695]  # 1
            img2 = cv2.imread('./screenshot/jia_guo_meng.png')[1770:1850, 785:850]  # 2
            img3 = cv2.imread('./screenshot/jia_guo_meng.png')[1690:1750, 930:1005]  # 3
            cv2.imwrite('./template/jiaguomeng/1.png', img1)
            cv2.imwrite('./template/jiaguomeng/2.png', img2)
            cv2.imwrite('./template/jiaguomeng/3.png', img3)
            return

        png_file: str = Adb.screen_shot(self.__png_name, self.__screenshot_path)
        img = cv2.imread(png_file)
        for house in self.__houses:
            center: tuple = self.__find_center(img, house)
            if center:
                Adb.swipe(center[0], center[1], self.__pos[house][0], self.__pos[house][1], 250)
                return True
        return False

    def __find_center(self, img, template_name):
        center: tuple = ()
        template = cv2.imread('./template/jiaguomeng/' + template_name + '.png')
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print('%s: %.2f' % (template_name, max_val))
        print(max_loc)
        if max_val >= 0.85:
            # print('%s: %.2f' % (template_name, max_val))
            center = (max_loc[0] + 30, max_loc[1] + 30)
        return center
