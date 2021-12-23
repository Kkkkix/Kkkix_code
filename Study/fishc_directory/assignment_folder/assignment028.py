import os

cwd = os.getcwd()

# 0. 尝试将文件（OpenMe.mp3）打印到屏幕上
f = open(cwd + '\\assignment_source\\A028_OpenMe.mp3','r')
for each_line in f:
        print(each_line, end='')
f.close()

# 1. 编写代码，将上一题中的文件（OpenMe.mp3）保存为新文件（OpenMe.txt）
f1 = open(cwd + '\\assignment_source\\A028_OpenMe.mp3')
f2 = open(cwd + '\\assignment_source\\A028_OpenMe.txt', 'w')        # 使用”x”打开更安全
f2.write(f1.read())
f2.close()
f1.close()
