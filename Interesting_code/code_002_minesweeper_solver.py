# -*- coding: utf-8 -*-
# What the code does: Convert pictures to text
# Author: Kkkkix
# Last Modified: 21/05/20

import win32gui, win32api, win32con
import matplotlib.pyplot as plt
import colorsys
import random
import numpy as np
from PIL import ImageGrab


def initiate_para():
    block_x = 16
    block_y = 16
    # block_x = 8     # Beginner
    # block_y = 8
    block_width = 16
    block_height = 16
    return block_x,block_y,block_width,block_height


# Find the minesweeper window and get the mine area
def findMinesweeper():
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

    return (left,top,right,bottom)


# Take a screenshot and select the mine area
def getMineArea(win_pos):
    win_pos_temp = list(win_pos[:])
    win_pos_temp[0] += 15
    win_pos_temp[1] += 104
    win_pos_temp[2] -= 15
    win_pos_temp[3] -= 40
    img = ImageGrab.grab().crop(win_pos_temp)
    # plt.figure('a')
    # plt.imshow(img)
    # plt.show()
    return img


# The color info
def init_colorInfo():
    rgb_0 = [(22, (255, 255, 255)), (110, (192, 192, 192))]
    rgb_1 = [(88, (192, 192, 192)), (11, (128, 128, 128)), (33, (0, 0, 255))]
    rgb_2 = [(66, (192, 192, 192)), (11, (128, 128, 128)), (55, (0, 128, 0))]
    rgb_3 = [(53, (255, 0, 0)), (68, (192, 192, 192)), (11, (128, 128, 128))]
    rgb_4 = [(68, (192, 192, 192)), (11, (128, 128, 128)), (53, (0, 0, 128))]
    rgb_5 = [(61, (128, 0, 0)), (60, (192, 192, 192)), (11, (128, 128, 128))]
    rgb_6 = [(57, (192, 192, 192)), (11, (128, 128, 128)), (64, (0, 128, 128))]
    rgb_7 = [(80, (192, 192, 192)), (11, (128, 128, 128)), (41, (0, 0, 0))]

    rgb_50 = [(22, (255, 255, 255)), (17, (255, 0, 0)), (79, (192, 192, 192)), (14, (0, 0, 0))] # number 50: red flag
    rgb_100 = [(121, (192, 192, 192)), (11, (128, 128, 128))]                   # number 100: opened and empty
    rgb_101 = [(4, (255, 255, 255)), (51, (192, 192, 192)), (11, (128, 128, 128)), (66, (0, 0, 0))] #101: opened and mine
    rgb_102 = [(4, (255, 255, 255)), (51, (255, 0, 0)), (11, (128, 128, 128)), (66, (0, 0, 0))]     #102: clicked mine

    rgb_game_finish = [(61, (255, 255, 0)), (3, (16, 16, 0)), (12, (247, 247, 0)), (11, (239, 239, 0)), (6, (231, 231, 0)), (151, (225, 225, 225)), (2, (49, 49, 24)), (2, (16, 16, 16)), (2, (189, 189, 0)), (1, (181, 181, 0)), (4, (173, 173, 0)), (1, (165, 165, 0)), (5, (123, 123, 132)), (1, (115, 115, 115)), (1, (49, 49, 16)), (6, (107, 107, 115)), (1, (123, 123, 115)), (2, (107, 107, 0)), (4, (99, 99, 99)), (1, (74, 74, 16)), (2, (123, 123, 0)), (2, (57, 57, 57)), (1, (49, 49, 41)), (1, (74, 74, 24)), (1, (41, 41, 41)), (3, (33, 33, 0)), (6, (41, 41, 0)), (2, (57, 57, 16)), (2, (41, 41, 16)), (2, (24, 24, 16)), (1, (74, 74, 57)), (2, (57, 57, 0)), (8, (222, 222, 0)), (4, (24, 24, 0)), (9, (206, 206, 0)), (7, (214, 214, 0)), (8, (198, 198, 198)), (2, (198, 198, 0)), (2, (156, 156, 0)), (1, (140, 140, 0)), (3, (132, 132, 132)), (1, (132, 132, 0)), (4, (90, 90, 0)), (2, (115, 115, 0)), (1, (99, 99, 0)), (1, (82, 82, 0)), (6, (74, 74, 0)), (3, (66, 66, 57)), (1, (66, 66, 0)), (1, (66, 66, 24)), (2, (33, 33, 16)), (5, (49, 49, 0)), (2, (24, 24, 8)), (1, (16, 16, 8)), (2, (8, 8, 0)), (22, (0, 0, 0))]
    rgb_game_running = [(116, (255, 255, 0)), (2, (16, 16, 0)), (7, (247, 247, 0)), (9, (239, 239, 0)), (4, (231, 231, 0)), (151, (225, 225, 225)), (1, (49, 49, 8)), (1, (16, 16, 16)), (3, (189, 189, 0)), (1, (181, 181, 0)), (2, (173, 173, 0)), (2, (165, 165, 0)), (6, (123, 123, 132)), (2, (115, 115, 0)), (2, (49, 49, 16)), (8, (107, 107, 115)), (2, (123, 123, 0)), (4, (99, 99, 99)), (1, (74, 74, 16)), (10, (57, 57, 0)), (1, (49, 49, 41)), (1, (74, 74, 24)), (1, (41, 41, 41)), (1, (33, 33, 16)), (4, (41, 41, 0)), (1, (57, 57, 16)), (3, (41, 41, 16)), (2, (24, 24, 16)), (1, (74, 74, 57)), (6, (222, 222, 0)), (3, (24, 24, 0)), (5, (206, 206, 0)), (1, (214, 214, 0)), (8, (198, 198, 198)), (1, (198, 198, 0)), (2, (49, 49, 0)), (1, (156, 156, 0)), (2, (132, 132, 132)), (1, (132, 132, 0)), (2, (90, 90, 0)), (2, (99, 99, 0)), (2, (82, 82, 0)), (5, (74, 74, 0)), (3, (66, 66, 57)), (1, (66, 66, 24)), (2, (49, 49, 49)), (3, (24, 24, 8)), (1, (16, 16, 8))]
    rgb_game_over = [(95, (255, 255, 0)), (11, (16, 16, 0)), (5, (247, 247, 0)), (3, (239, 239, 0)), (3, (231, 231, 0)), (151, (225, 225, 225)), (2, (49, 49, 16)), (1, (16, 16, 16)), (7, (189, 189, 0)), (10, (181, 181, 0)), (7, (173, 173, 0)), (1, (165, 165, 0)), (6, (123, 123, 132)), (2, (49, 49, 0)), (8, (107, 107, 115)), (2, (123, 123, 0)), (4, (99, 99, 99)), (1, (74, 74, 16)), (2, (57, 57, 57)), (1, (49, 49, 41)), (1, (74, 74, 24)), (1, (41, 41, 41)), (3, (33, 33, 16)), (4, (41, 41, 0)), (2, (57, 57, 0)), (3, (41, 41, 16)), (2, (24, 24, 16)), (1, (74, 74, 57)), (1, (57, 57, 16)), (6, (222, 222, 0)), (2, (24, 24, 0)), (3, (206, 206, 0)), (2, (214, 214, 0)), (8, (198, 198, 198)), (7, (198, 198, 0)), (2, (156, 156, 0)), (3, (148, 148, 0)), (6, (140, 140, 0)), (2, (132, 132, 132)), (3, (132, 132, 0)), (1, (90, 90, 0)), (2, (99, 99, 0)), (1, (82, 82, 0)), (4, (74, 74, 0)), (3, (66, 66, 57)), (1, (66, 66, 24)), (1, (49, 49, 8)), (2, (24, 24, 8)), (1, (16, 16, 8))]

    color_info = {'1':rgb_1, '2':rgb_2, '3':rgb_3, '4':rgb_4, '5':rgb_5, '6': rgb_6, '7':rgb_7,
                  '50':rgb_50, '0':rgb_0,
                  '100':rgb_100, '101':rgb_101, '102':rgb_102,
                  'finish':rgb_game_finish,'running':rgb_game_running,'over':rgb_game_over}
    return color_info


# Convert the mine area image to map
def convertImg2map(img):
    # number 1-8: number of mines around
    # number 0: not opened
    # number 50: red flag
    # number 100: opened and empty
    # number 101: opened and mine
    # number 102: clicked mine
    block_x,block_y,block_width,block_height = initiate_para()
    color_info = init_colorInfo()
    DictLab = color_info.copy()
    mine_map = [[0 for i in range(block_x)] for j in range(block_y)]
    for y in range(block_y):
        for x in range(block_x):
            this_image = img.crop((x*block_width, y*block_height, (x+1)*block_width,(y+1)*block_height))
            this_image = this_image.crop((2,1,13,13))
            # plt.figure('a')
            # plt.imshow(this_image)
            # plt.ion()
            # plt.pause(0.1)
            # plt.close()
            print(this_image.getcolors())

            if this_image.getcolors() == color_info['1']:
                mine_map[y][x] = 1
            elif this_image.getcolors() == color_info['2']:
                mine_map[y][x] = 2
            elif this_image.getcolors() == color_info['3']:
                mine_map[y][x] = 3
            elif this_image.getcolors() == color_info['4']:
                mine_map[y][x] = 4
            elif this_image.getcolors() == color_info['5']:
                mine_map[y][x] = 5
            elif this_image.getcolors() == color_info['6']:
                mine_map[y][x] = 6
            elif this_image.getcolors() == color_info['7']:
                mine_map[y][x] = 7

            elif this_image.getcolors() == color_info['50']:
                mine_map[y][x] = 50
            elif this_image.getcolors() == color_info['100']:
                mine_map[y][x] = 100
            elif this_image.getcolors() == color_info['101']:
                mine_map[y][x] = 101
            elif this_image.getcolors() == color_info['102']:
                mine_map[y][x] = 102
            elif this_image.getcolors() == color_info['0']:
                mine_map[y][x] = 0

            else:
                print('There is one figure which can not be recognized')
                print('x = %d; y = %d' % (x,y))
                input('press Enter button to continue --->>>')

            if this_image.getcolors() not in DictLab.values():
                DictLab["%d;%d" % (x,y)] = this_image.getcolors()
    print('The DictLab is: ',end='')
    print(DictLab)
    # input('press Enter button to continue --->>>')
    return  mine_map


def mouse_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def mouse_right_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def luck(mine_map,win_pos):
    block_width,block_height = initiate_para()[2:4]
    mine_map = np.array(mine_map)
    enpty_index = np.where(mine_map == 0)
    empty_index_matrix = np.dstack((enpty_index[0],enpty_index[1]))

    num_empty = empty_index_matrix.shape[1]     # (1, 176, 2)
    ran_int = random.randint(0,num_empty-1)
    click_x, click_y = empty_index_matrix[0][ran_int][1],empty_index_matrix[0][ran_int][0]

    win_pos_temp = list(win_pos[:])
    win_pos_temp[0] += 15
    win_pos_temp[1] += 104
    win_pos_temp[2] -= 15
    win_pos_temp[3] -= 40
    mouse_click(win_pos_temp[0]+(click_x+1)*block_width-int(block_width/2), win_pos_temp[1]+(click_y+1)*block_height-int(block_height/2))
    print('click %d %d' % (click_x,click_y))


def num_around(mine_map,posi):
    # This function is used to count the surround situation
    # posi format is (row = y,column = x)
    block_x,block_y = initiate_para()[0:2]
    num_num = -1
    num_empty = 0
    num_closed = 0
    num_flag = 0
    closed_posi = []
    if posi[0] == 0:    # the first row
        start_y = 0
        end_y = 2
    elif posi[0] == block_y-1: # the last row
        start_y = block_y-2
        end_y = block_y
    else:   # the other row
        start_y = posi[0] -1
        end_y = posi[0] +2

    if posi[1] == 0:    # the first column
        start_x = 0
        end_x = 2
    elif posi[1] == block_x-1:  # the last column
        start_x = block_x-2
        end_x = block_x
    else:  # the other column
        start_x = posi[1] - 1
        end_x = posi[1] + 2

    for x in range(start_x,end_x):
        for y in range(start_y,end_y):
            if (mine_map[y][x] <= 8) & (mine_map[y][x] != 0):
                num_num += 1
            elif (mine_map[y][x] == 0):
                num_closed += 1
                closed_posi.append((y,x))
            elif (mine_map[y][x] == 50):
                num_flag += 1
            elif (mine_map[y][x] == 100):
                num_empty += 1

    return [num_num,num_empty,num_closed,num_flag,closed_posi]


def flagandclick(mine_map,win_pos):
    win_pos_temp = list(win_pos[:])
    win_pos_temp[0] += 15
    win_pos_temp[1] += 104
    win_pos_temp[2] -= 15
    win_pos_temp[3] -= 40
    block_width, block_height = initiate_para()[2:4]
    mine_map = np.array(mine_map)
    print(mine_map)
    clicked_num_index = np.where((mine_map <=8) & (mine_map != 0))
    clicked_num_index_matrix = np.dstack((clicked_num_index[0], clicked_num_index[1]))

    print(clicked_num_index_matrix)

    for each_num in clicked_num_index_matrix[0]:
        print(each_num)
        ar_det = num_around(mine_map,each_num)     # around details of this position
        print('around details: ', end='')
        print(ar_det)
        if ar_det[2] == 0:
            continue
        elif mine_map[each_num[0]][each_num[1]] - ar_det[3] == ar_det[2]:   # number of mines - flags = closed
            print('each_num: ',end='')
            print(each_num)
            for each in ar_det[4]:
                print(each)
                y = win_pos_temp[1] + (each[0] + 1) * block_height - int(block_height / 2)
                x = win_pos_temp[0] + (each[1] + 1) * block_width - int(block_width / 2)
                print('click',end='')
                print(x,y)
                mouse_right_click(x,y)
            break
        elif mine_map[each_num[0]][each_num[1]] - ar_det[3] == 0:   # number of mines = flags
            for each in ar_det[4]:
                y = win_pos_temp[1] + (each[0] + 1) * block_height - int(block_height / 2)
                x = win_pos_temp[0] + (each[1] + 1) * block_width - int(block_width / 2)
                print('click',end='')
                print(x,y)
                mouse_click(x,y)
            break




def checkGameStatus(win_pos):
    color_info = init_colorInfo()
    win_pos_temp = list(win_pos[:])
    win_pos_temp[0] += 132
    win_pos_temp[1] += 67
    win_pos_temp[2] = win_pos_temp[0] + 20
    win_pos_temp[3] = win_pos_temp[1] + 20
    img = ImageGrab.grab().crop(win_pos_temp)
    if img.getcolors() == color_info['running']:
        return True
    elif img.getcolors() == color_info['over']:
        print('Game Over. Too Sad...')
        return False
    elif img.getcolors() == color_info['finish']:
        print('Game is finish!!!')
        return False
    else:
        print('nothin detected')
        return True




def Solver():
    game_status = True
    times = 0
    while game_status:
        win_pos = findMinesweeper()
        mine_area_img = getMineArea(win_pos)
        mine_map = convertImg2map(img=mine_area_img)

        # luck(mine_map, win_pos)
        flagandclick(mine_map,win_pos)
        game_status = checkGameStatus(win_pos)

        times += 1
        if times == 1000:
            break
        # break
        # if


if __name__ == '__main__':
    # win_pos = findMinesweeper()
    # mine_area_img = getMineArea(win_pos)
    # mine_map = convertImg2map(img=mine_area_img,block_x=16,block_y=16,block_width=16,block_height=16)
    # print(mine_map)
    Solver()

