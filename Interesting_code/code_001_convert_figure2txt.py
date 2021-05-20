# -*- coding: utf-8 -*-
# What the code does: Convert pictures to text
# Author: Kkkkix
# Last Modified: 21/05/20

from PIL import Image

codeLib = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. """     #生成字符画所需的字符集
count = len(codeLib)


def transform(image_file):
    image_file = image_file.convert('L')    # 将图片转换为黑白图片
    text_pic = ''
    for h in range(0,image_file.size[1]):
        for w in range(0,image_file.size[0]):
            gray = image_file.getpixel((w,h))   # 获取像素的灰度值
            text_pic = text_pic + codeLib[int(((count+1)*gray)/256)]    # 建立灰度与字符集的映射 gray/(256/len(codeLib))
        text_pic = text_pic+'\r\n'
    return text_pic

if __name__ == '__main__':

    image_file = open(u'a.jpg','rb')
    image_file = Image.open(image_file)
    # image_file = image_file.resize((int(image_file.size[0] * 1), int(image_file.size[1] * 0.13)))  # 调整图片大小
    image_file = image_file.resize((420, 140))  # 调整图片大小
    print(u'Info:', image_file.size[0], ' ', image_file.size[1], ' ', count)

    text_file = open('fig2text.txt','w')
    text_file.write(transform(image_file))
    text_file.close()
