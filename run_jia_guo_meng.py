# -*- coding:utf-8 -*-
from jiaguomeng.Jiaguomeng import Jiaguomeng

if __name__ == '__main__':
    path = './screenshot'
    png_name = 'jia_guo_meng'

    # Jiaguomeng(path, png_name).auto_train()
    Jiaguomeng(path, png_name).auto()
