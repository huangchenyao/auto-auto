# -*- coding:utf-8 -*-
from jiaguomeng.Jiaguomeng import Jiaguomeng

if __name__ == '__main__':
    path = './screenshot'
    png_name = 'jia_guo_meng'

    # Jiaguomeng(path, png_name).train_template(True)
    # Jiaguomeng(path, png_name).update(30 * 1000)
    Jiaguomeng(path, png_name, 1).train()
