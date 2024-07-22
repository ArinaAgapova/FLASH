def is_palindrome_nch(s):
    if s[0] == s[-1] and s[1] == s[-2] and \
    ((s[2] != s[1] and s[2] != s[3]) or (s[2] == s[1] and s[2] == s[3])):
        return True
    return False
from itertools import *
alph = 'ФЛЭШ'
k = 0
for x in product(alph, repeat = 5):
    s = ''.join(x)
    if is_palindrome_nch(s):
        k += 1
print(k)