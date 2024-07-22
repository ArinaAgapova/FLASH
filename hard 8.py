def sum_digit(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s
def digit_root(x):
    if x < 10:
        return x
    return digit_root(sum_digit(x))
from itertools import *
alph = '0123456789'
k = 0
for x in product(alph, repeat = 5):
    s = ''.join(x)
    s = int(s)
    if digit_root(s) == 7:
        k += 1
print(k)