from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

# main()

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
print(f"sssssssssssssssssss{s}")
n = int(s)
logging.info('n = %d' % n)
print(10 / n)