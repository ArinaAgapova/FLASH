from itertools import *
alph = '0123456'
max10 = 0
for x in product(alph, repeat = 5):
    s = ''.join(x)
    if s.count('6') <= 2 and s[0] != '0':
        save_s = s
        s = s.replace('2', '0').replace('4', '0').replace('6', '0')
        s = s.replace('3', '1').replace('5', '1')
        if '11' not in s and '00' not in s:
            max10 = int(save_s, 7)
summa = 0
while max10 > 0:
    summa += max10 % 10
    max10 //= 10
print(summa)