import os

#   0. 编写一个程序，统计当前目录下每个文件类型的文件数。
# all_files = os.listdir(os.curdir) # 使用os.curdir表示当前目录更标准
# type_dict = dict()
#
# for each_file in all_files:
#     if os.path.isdir(each_file):
#         type_dict.setdefault('文件夹', 0)
#         type_dict['文件夹'] += 1
#     else:
#         ext = os.path.splitext(each_file)[1]
#         type_dict.setdefault(ext, 0)
#         type_dict[ext] += 1
#
# for each_type in type_dict.keys():
#     print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))

#   1. 编写一个程序，计算当前文件夹下所有文件的大小。  