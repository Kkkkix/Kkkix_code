# '''0. 编写一个程序，接受用户的输入并保存为新的文件。'''
# def file_write(file_name):
#     f = open(file_name,'w',encoding='utf-8')
#     print('请输入内容【单独输入\':w\'保存退出】')
#
#     while True:
#         write_some = input()
#         if write_some != ":w":
#             f.write('%s\n' % write_some)
#         else:
#             break
#
#     f.close()
#
#
# file_name = input('请输入文件名：')
# file_write(file_name)

# 1. 编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置。
# def file_compare(file1, file2):
#     f1 = open(file1,'r',encoding='utf-8')
#     f2 = open(file2,'r',encoding='utf-8')
#     count = 0 # 统计行数
#     differ = [] # 统计不一样的数量
#
#     for line1 in f1:
#         line2 = f2.readline()
#         count += 1
#         print(line1)
#         print(line2)
#         if line1 != line2:
#             differ.append(count)
#
#     f1.close()
#     f2.close()
#     return differ
#
# file1 = input('请输入需要比较的头一个文件名：')
# file2 = input('请输入需要比较的另一个文件名：')
#
# differ = file_compare(file1, file2)
#
# if len(differ) == 0:
#     print('两个文件完全一样！')
# else:
#     print('两个文件共有【%d】处不同：' % len(differ))
#     for each in differ:
#         print('第 %d 行不一样' % each)

# 2. 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上。
# def file_view(file_name, line_num):
#     print('\n文件%s的前%s的内容如下：\n' % (file_name, line_num))
#     f = open(file_name)
#     for i in range(int(line_num)):
#         print(f.readline(), end= '')
#
#     f.close()
#
# file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
# line_num = input('请输入需要显示该文件前几行：')
# file_view(file_name, line_num)

# 3. 呃，不得不说我们的用户变得越来越刁钻了。
# 要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。
# （如输入13:21打印第13行到第21行，输入:21打印前21行，
# 输入21:则打印从第21行开始到文件结尾所有内容）
# def file_view(file_name, line_num):
#     if line_num.strip() == ':':
#         begin = '1'
#         end = '-1'
#
#     (begin, end) = line_num.split(':')
#
#     if begin == '':
#         begin = '1'
#     if end == '':
#         end = '-1'
#
#     if begin == '1' and end == '-1':
#         prompt = '的全文'
#     elif begin == '1':
#         prompt = '从开始到%s' % end
#     elif end == '-1':
#         prompt = '从%s到结束' % begin
#     else:
#         prompt = '从第%s行到第%s行' % (begin, end)
#
#     print('\n文件%s%s的内容如下：\n' % (file_name, prompt))
#
#     begin = int(begin) - 1
#     end = int(end)
#     lines = end - begin
#
#     f = open(file_name)
#
#     for i in range(begin):  # 用于消耗掉begin之前的内容
#         f.readline()
#
#     if lines < 0:
#         print(f.read())
#     else:
#         for j in range(lines):
#             print(f.readline(), end='')
#
#     f.close()
#
#
# file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
# line_num = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21: 或 : 】：')
# file_view(file_name, line_num)

# 4. 编写一个程序，实现“全部替换”功能。
# def file_replace(file_name, rep_word, new_word):
#     f_read = open(file_name)
#
#     content = []
#     count = 0
#
#     for eachline in f_read:
#         if rep_word in eachline:
#             count = eachline.count(rep_word) #count感觉应该用这个
#             eachline = eachline.replace(rep_word, new_word)
#         content.append(eachline)
#
#     decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
#                    % (file_name, count, rep_word, rep_word, new_word))
#
#     if decide in ['YES', 'Yes', 'yes']:
#         f_write = open(file_name, 'w')
#         f_write.writelines(content)
#         f_write.close()
#
#     f_read.close()
#
#
# file_name = input('请输入文件名：')
# rep_word = input('请输入需要替换的单词或字符：')
# new_word = input('请输入新的单词或字符：')
# file_replace(file_name, rep_word, new_word)
