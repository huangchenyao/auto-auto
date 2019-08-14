# -*- coding:utf-8 -*-
from liaoliwang.Liaoliwang import Liaoliwang

if __name__ == '__main__':
    path = './screenshot'
    png_name = 'liao_li_wang'

    Liaoliwang(path, png_name).ad_auto()
    # Liaoliwang(path, png_name).adventure_auto()

    # cv2.imwrite('./screenshot/tmp2.png', img1)

    # adventure_map = [
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    # ]
    # shape = [[1, 1, 1]]
    # find(adventure_map, shape)
