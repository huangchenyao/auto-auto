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
        'gangtiechang': [300, 950, 1],  # 钢铁厂
        'lingjianchang': [550, 850, 1],  # 零件厂
        'qiejixie': [800, 750, 1],  # 企鹅机械
        'bianlidian': [300, 1200, 1],  # 便利店
        'wujindian': [550, 1100, 1],  # 五金店
        'minshizhai': [800, 1000, 1],  # 民食斋
        'juminlou': [300, 1450, 1],  # 居民楼
        'pingfang': [550, 1350, 0],  # 平房
        'gangjiegoufang': [800, 1250, 1],  # 钢结构房
    }
    __houses: list = []

    def __init__(self, screenshot_path: str, png_name: str, screens_x: float = 1080.0, screens_y: int = 2340):
        self.__zoom_x = screens_x / 1080.0
        self.__zoom_x = screens_y / 2034.0

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
                           self.__pos[k][0] + 25,
                           self.__pos[k][1] + 25)
            time.sleep(0.25)

    def auto_train(self) -> bool:
        template = False
        if template:
            # img = cv2.imread('./screenshot/jia_guo_meng.png')[1850:1920, 620:700]  # 1
            img = cv2.imread('./screenshot/jia_guo_meng.png')[1775:1835, 780:860]  # 2
            # img = cv2.imread('./screenshot/jia_guo_meng.png')[1690:1750, 930:1010] # 3
            cv2.imwrite('./template/jiaguomeng/lingjianchang.png', img)
            return

        png_file: str = Adb.screen_shot(self.__png_name, self.__screenshot_path)
        img = cv2.imread(png_file, 0)
        for house in self.__houses:
            center: tuple = self.__find_center(img, house)
            if center:
                Adb.swipe(center[0], center[1], self.__pos[house][0], self.__pos[house][1], 250)
                return True
        return False

    def __find_center(self, img, template_name):
        center: tuple = ()
        template = cv2.imread('./template/jiaguomeng/' + template_name + '.png', 0)
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.8:
            center = (max_loc[0] + 30, max_loc[1] + 30)
        return center
