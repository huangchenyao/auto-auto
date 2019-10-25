# -*- coding:utf-8 -*-
from jiaguomeng.Jiaguomeng import Jiaguomeng
import tkinter.messagebox

if __name__ == '__main__':
    # Jiaguomeng().update(120 * 1000)
    # Jiaguomeng().train_template(True)
    Jiaguomeng(level=1).train()
    # Jiaguomeng().open('album', 500)

    tkinter.messagebox.showinfo('提示', 'Finish!')
