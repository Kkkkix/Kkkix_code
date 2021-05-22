# -*- coding: utf-8 -*-
# What the code does: Convert pictures to text
# Author: Kkkkix
# Last Modified: 21/05/20

import win32gui
import matplotlib.pyplot as plt
from PIL import ImageGrab



# Find the minesweeper window and get the mine area
def find_minesweeper():
    title_name = 'Minesweeper Clone 2007'
    ms_win = win32gui.FindWindow(None, title_name)

    # window coordinates
    left,top,right,bottom = 0,0,0,0

    if ms_win:
        print("找到窗口：%s" % title_name)
        left, top, right, bottom = win32gui.GetWindowRect(ms_win)
        win32gui.SetForegroundWindow(ms_win)
        print("窗口的坐标是：left:%d; top:%d; right:%d; bottom:%d" % (left,top,right,bottom))
    else:
        print("未找到窗口")

    return [left,top,right,bottom]


# Take a screenshot and select the mine area
def getMineArea(win_pos):
    win_pos[0] += 15
    win_pos[1] += 104
    win_pos[2] -= 15
    win_pos[3] -= 40
    img = ImageGrab.grab().crop(win_pos)
    plt.figure('a')
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    win_pos = find_minesweeper()
    getMineArea(win_pos)
