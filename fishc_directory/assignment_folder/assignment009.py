# # Practice 0
# times = 3
#
# temp = input('please input your password:')
# password = 'FishC.com'
#
# while True:
#     if '*' in temp:
#         print('the password cannot include "*"! you still have '+str(times) + ' times!',end='')
#         temp = input('please input your password:')
#     elif temp == password:
#         print('the password is correct, entering the program......')
#         break
#
#     else:
#         times = times - 1
#         print('the password is wrong! you still have '+str(times) +' times!',end='')
#         temp = input('please input your password:')

# # Practice 1
# narcissistic_num = []
# for i in range(100,1000):
#     hundred = i//100
#     ten = i%100//10
#     one = i %10
#
#     if i == hundred**3 + ten**3 + one**3:
#         narcissistic_num.append(i)
#
# print('')
# print('shuixianhua is ',end='')
# print(narcissistic_num)

# # Practice 2
# import itertools
#
# balls = list(range(1,13))
# results=[]
# for poss in list(itertools.combinations(balls,8)):
#     red, yellow, green = 0, 0, 0
#     for char in poss:
#         if char >= 7:
#             green += 1
#         elif char <4:
#             red += 1
#         else:
#             yellow += 1
#
#     if (red,yellow,green) not in results:
#         results.append((red,yellow,green))
#
# print(results)

