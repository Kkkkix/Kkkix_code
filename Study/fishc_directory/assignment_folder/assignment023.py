''' 0. 使用递归编写一个十进制转换为二进制的函数（要求采用“取2取余”的方式，结果与调用bin()一样返回字符串形式）。    '''
n = 545

def dec2bin(dec,list = ''):
    if dec == 1:
        list += str(1)
        list += 'b0'
        return list[::-1]
    else:
        list += str(dec%2)
        return dec2bin(dec//2,list)


print(dec2bin(dec=n))
print(bin(n))

def Dec2bin(n):
    result = ''

    if n:
        result = Dec2bin(n//2)
        return result + str(n%2)

    else:
        return result

n_bin = Dec2bin(n)
print('十进制转换二进制的结果是：%d - > %s'%(n, n_bin))


''' 1. 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345) ==> [1, 2, 3, 4, 5]'''
def get_digits(n,list=[]):
    if n < 10:
        list.append(n)
        list.reverse()
        return list
    else:
        list.append(n%10)
        return get_digits(n//10, list)

print(get_digits(154564))

result = []
def get_digits2(n):
    if n>0:
        result.insert(0,n%10)
        get_digits2(n//10)

print(get_digits(658723,list=[]))


'''2. 还记得求回文字符串那道题吗？现在让你使用递归的方式来求解，亲还能骄傲的说我可以吗？'''
def palindrome(n):
    if n == '':
        return  True
    elif n[0] == n[-1]:
        return  palindrome(n[1:-1])
    else:
        return  False

print(palindrome('1545154611'))

'''
3. 使用递归编程求解以下问题：
有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
'''
def solve_q3(n):
    if n == 1:
        return 10
    else:
        return 2+solve_q3(n-1)

print(solve_q3(5))