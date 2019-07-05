# -*- coding:utf-8 -*-
import cv2
import time
from Adb import Adb
import numpy as np


class Liaoliwang:
    __screenshot_path = ''
    __png_name = ''
    __ad_template_path = './template/ad'

    def __init__(self, screenshot_path, png_name):
        self.__screenshot_path = screenshot_path
        self.__png_name = png_name

    # 点击观看广告
    def __ad_start(self):
        png_file = Adb.screen_shot(self.__png_name, self.__screenshot_path)
        img = cv2.imread(png_file, 0)
        threshold = 0.975
        ad_pos = {'x0': 945, 'y0': 255, 'x1': 1045, 'y1': 345}
        ad_template = cv2.imread(self.__ad_template_path + '/ad_template.png', 0)

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
        png_file = Adb.screen_shot(self.__png_name, self.__screenshot_path)
        img = cv2.imread(png_file, 0)
        is_close = 0
        # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100, maxRadius=50)
        # for circle in circles[0, :]:
        #     print(circle)
        #     tap(circle[0], circle[1])
        #
        top_right_close_pos1 = {'x0': 955, 'y0': 115, 'x1': 1040, 'y1': 200}
        top_right_close_template1 = self.__ad_template_path + '/top_right_close_template1.png'
        is_close += self.__ad_close_template(img, top_right_close_pos1, top_right_close_template1)

        top_right_close_pos2 = {'x0': 940, 'y0': 115, 'x1': 1040, 'y1': 215}
        top_right_close_template2 = self.__ad_template_path + '/top_right_close_template2.png'
        is_close += self.__ad_close_template(img, top_right_close_pos2, top_right_close_template2)

        top_right_close_pos3 = {'x0': 950, 'y0': 125, 'x1': 1030, 'y1': 205}
        top_right_close_template3 = self.__ad_template_path + '/top_right_close_template3.png'
        is_close += self.__ad_close_template(img, top_right_close_pos3, top_right_close_template3)

        top_right_close_pos4 = {'x0': 945, 'y0': 120, 'x1': 1035, 'y1': 210}
        top_right_close_template4 = self.__ad_template_path + '/top_right_close_template4.png'
        is_close += self.__ad_close_template(img, top_right_close_pos4, top_right_close_template4)

        top_right_close_pos5 = {'x0': 945, 'y0': 120, 'x1': 1035, 'y1': 210}
        top_right_close_template5 = self.__ad_template_path + '/top_right_close_template5.png'
        is_close += self.__ad_close_template(img, top_right_close_pos5, top_right_close_template5)

        top_left_close_pos1 = {'x0': 60, 'y0': 120, 'x1': 150, 'y1': 210}
        top_left_close_template1 = self.__ad_template_path + '/top_left_close_template1.png'
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

    def __find_hanhan_pos(self, img):
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        hanhan = cv2.imread('./template/adventure/hanhan.png', 0)
        hanhan_flip = cv2.flip(hanhan, 1, dst=None)  # 水平镜像

        threshold = 0.75
        w, h = hanhan.shape[::-1]
        pts = [(0, 0)]

        res = cv2.matchTemplate(img_grey, hanhan, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            like_cnt = 0
            for _pt in pts:
                if _pt[0] - 5 <= pt[0] <= _pt[0] + 5 and _pt[1] - 5 <= pt[1] <= _pt[1] + 5:
                    like_cnt += 1
            if like_cnt == 0:
                pts.append(pt)
        res = cv2.matchTemplate(img_grey, hanhan_flip, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            like_cnt = 0
            for _pt in pts:
                if _pt[0] - 5 <= pt[0] <= _pt[0] + 5 and _pt[1] - 5 <= pt[1] <= _pt[1] + 5:
                    like_cnt += 1
            if like_cnt == 0:
                pts.append(pt)

        del (pts[0])
        pts_mid = []
        for pt in pts:
            pts_mid.append((pt[0] + w / 2, pt[1] + h / 2))

        return pts_mid

    def __find_reachable_pos(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array([35, 160, 160])
        upper = np.array([45, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(img, img, mask=mask)
        res_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(res_gray, 127, 255, 0)
        cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        pos = []
        for cnt in cnts:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)
            if 15 < radius < 20:
                pos.append(center)
        return pos

    def __find_side_hanhan_pos(self, img):
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(img_grey, cv2.HOUGH_GRADIENT, 1, 20,
                                   param1=50, param2=30, minRadius=30, maxRadius=35)
        pos = []
        for i in circles[0, :]:
            pos.append((int(i[0]), int(i[1])))
        return pos

    def __adventure_one_step(self):
        png_file = Adb.screen_shot(self.__png_name, self.__screenshot_path)
        img = cv2.imread(png_file)

        hanhan_pos = self.__find_hanhan_pos(img)
        if len(hanhan_pos) == 0:
            hanhan_pos = self.__find_side_hanhan_pos(img)
        reachable_pos = self.__find_reachable_pos(img)

        near_pos = (0, 0)
        min = float('inf')
        for i in reachable_pos:
            dist = (i[0] - hanhan_pos[0][0]) ** 2 + (i[1] - hanhan_pos[0][1]) ** 2
            if dist < min:
                min = dist
                near_pos = i
        Adb.tap(near_pos[0], near_pos[1])

    def adventure_auto(self):
        for i in range(15):
            self.__adventure_one_step()
