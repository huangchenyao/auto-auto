# -*- coding:utf-8 -*-
import cv2
import time
from Adb import Adb


class Liaoliwang:
    __path = ''
    __png_name = ''

    def __init__(self, path, png_name):
        self.__path = path
        self.__png_name = png_name

    # 点击观看广告
    def __ad_start(self):
        png_file = Adb.screen_shot(self.__png_name, self.__path)
        img = cv2.imread(png_file, 0)
        threshold = 0.975
        ad_pos = {'x0': 945, 'y0': 255, 'x1': 1045, 'y1': 345}
        ad_template = cv2.imread(self.__path + '/ad_template.png', 0)

        ad = img[ad_pos['y0']:ad_pos['y1'], ad_pos['x0']:ad_pos['x1']]
        match_rate = cv2.matchTemplate(ad, ad_template, cv2.TM_CCOEFF_NORMED)
        # print('start:')
        # print(match_rate)
        if (match_rate > threshold).any():
            Adb.tap_random(ad_pos['x0'] + 20, ad_pos['y0'] + 20, ad_pos['x1'] - 20, ad_pos['y1'] - 20)
            time.sleep(1)
            Adb.tap_random(590, 1450, 960, 1520)

    # 关闭广告
    def __ad_close(self):
        png_file = Adb.screen_shot(self.__png_name, self.__path)
        img = cv2.imread(png_file, 0)
        is_close = 0
        # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100, maxRadius=50)
        # for circle in circles[0, :]:
        #     print(circle)
        #     tap(circle[0], circle[1])
        #
        top_right_close_pos1 = {'x0': 955, 'y0': 115, 'x1': 1040, 'y1': 200}
        top_right_close_template1 = self.__path + '/top_right_close_template1.png'
        is_close += self.__ad_close_template(img, top_right_close_pos1, top_right_close_template1)

        top_right_close_pos2 = {'x0': 940, 'y0': 115, 'x1': 1040, 'y1': 215}
        top_right_close_template2 = self.__path + '/top_right_close_template2.png'
        is_close += self.__ad_close_template(img, top_right_close_pos2, top_right_close_template2)

        top_right_close_pos3 = {'x0': 950, 'y0': 125, 'x1': 1030, 'y1': 205}
        top_right_close_template3 = self.__path + '/top_right_close_template3.png'
        is_close += self.__ad_close_template(img, top_right_close_pos3, top_right_close_template3)

        top_right_close_pos4 = {'x0': 945, 'y0': 120, 'x1': 1035, 'y1': 210}
        top_right_close_template4 = self.__path + '/top_right_close_template4.png'
        is_close += self.__ad_close_template(img, top_right_close_pos4, top_right_close_template4)

        top_left_close_pos1 = {'x0': 60, 'y0': 120, 'x1': 150, 'y1': 210}
        top_left_close_template1 = self.__path + '/top_left_close_template1.png'
        is_close += self.__ad_close_template(img, top_left_close_pos1, top_left_close_template1)

        return is_close

    # 根据模板关闭广告
    def __ad_close_template(self, img, close_pos, close_template_name):
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

    # 强行关闭广告
    def __force_close(self):
        Adb.tap(1000, 160)
        time.sleep(2)
        Adb.tap_random(270, 585, 270 * 3, 585 * 3)

    # 自动看广告
    def ad_auto(self):
        check_cnt = 0
        while True:
            self.__ad_start()
            if not self.__ad_close():
                check_cnt += 1
            else:
                check_cnt = 0
            if check_cnt > 20:
                self.__force_close()
                check_cnt = 0
                print('force')
            time.sleep(2)

    # 自动送酱油
    def oil_auto(self):
        pass
