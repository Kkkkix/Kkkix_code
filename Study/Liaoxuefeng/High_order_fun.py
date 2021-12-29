import time, functools, inspect
from functools import reduce


def normalize(name):
    return name.capitalize()
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


def product(x,y):
    return x*y


def prod(L):
    return reduce(lambda x,y:x*y,L)
# # 测试：
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')


dict1 = {'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'0': 0}

def str2int(s):
    return dict1[s]

def fun1(ten,one):
    return 10*ten + one

def fun2(tenth, one):
    return one+tenth/10

def str2float(s):
    integer_num = reduce(fun1, list(map(str2int, s.split('.')[0])))
    decimal_num = reduce(fun2, list(map(str2int, s.split('.')[1]))[::-1]) / 10

    return integer_num + decimal_num
# # 测试
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')


def not_empty(s):
    return s and s.strip()

# print(list(filter(not_empty, ['   A', '', 'B', None, 'C', '  '])))


# 求质数的生成器，埃氏筛法

def _prime_guess():
    n = 1
    while True:
        n += 1
        yield n


def _not_divisible(n):
    return lambda x: x%n != 0


def prime():
    guess_range = _prime_guess()
    while True:
        n = next(guess_range)
        yield n
        guess_range = filter(_not_divisible(n), guess_range)

# # 测试 打印1000以内的质数
# for n in prime():
#     if n < 1000:
#         print(n)
#     else:
#         break


def is_palindrome(n):
    return str(n) == str(n)[::-1]

# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]

# # 测试，按名字排序
# L2 = sorted(L, key=by_name)
# print(L2)


def by_score(t):
    return -t[1]

# # 测试，按成绩排序
# L2 = sorted(L, key=by_score)
# print(L2)


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x+1
        return x
    return counter

# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1
# # 测试
# L = list(filter(is_odd, range(1, 20)))
# print(L)

# 匿名函数
# L = list(filter(lambda x: x%2 == 1, range(1,20)))
# print(L)

# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        fn_return_value = fn(*args, **kw)
        end_time = time.time()
        print(f"{fn.__name__} executed in {end_time-start_time} s")
        return fn_return_value
    return wrapper

# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0002)
#     return x + y;
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


def log(text = None):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print(f'text: {text}, function name: {func.__name__}')
                return func(*args, **kw)
            return wrapper
        return decorator
    elif inspect.isfunction(text):
        func = text

        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f'call {func.__name__}:')
            return func(*args, **kw)
        return wrapper
    elif text == None:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print(f'function name: {func.__name__}')
                return func(*args, **kw)
            return wrapper
        return decorator

# # 测试
# @log
# def now():
#     print('2015-3-25')
#
# now()



