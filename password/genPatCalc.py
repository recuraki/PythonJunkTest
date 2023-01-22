# 大した数じゃないのでnCrは適当にやる
import itertools
from math import factorial
import string
charUpper = set(string.ascii_uppercase)
charLower = set(string.ascii_lowercase)
charDigit = set(string.digits)
charSpecial = set("!#()&<>;@[]|")
ignorechars: set = set("oO01IilL9qQZz2dDgGnmNMbB8pPtT")
for char in ignorechars:
    if char in charUpper: charUpper.remove(char)
    if char in charLower: charLower.remove(char)
    if char in charDigit: charDigit.remove(char)
    if char in charSpecial: charSpecial.remove(char)
print(charUpper, len(charUpper))
print(charLower, len(charLower))
print(charDigit, len(charDigit))
print(charSpecial, len(charDigit))

import random
t = ""
for x in charUpper: t+=x
for x in charLower: t+=x
for x in charDigit: t+=x
for x in charSpecial: t+=x
for i in range(10):
    print("".join(random.choices(t,k=12)))

patdat = [14,14,5,5]
def f(l):
    res = 0
    for pat in itertools.permutations(patdat):
        patnum = 0
        for a in range(1, l + 1 - 3):
            patnum1 = pat[0] ** a
            for b in range(1, l + 1 - 2 - a):
                patnum2 = pat[1] ** b
                for c in range(1, l + 1 - 1 - a - b):
                    patnum3 = pat[2] ** c
                    for d in range(1, l + 1 - 0 - a - b - c):
                        patnum4 = pat[3] ** d
                        res += patnum1 * patnum2 * patnum3 * patnum4
    return res

l = 12
res = f(l)
a = sum([26,26,10,12]) ** l
b = sum(patdat) ** l
c = res
print("full:", "{: >40,d}".format(a))
print("all :", "{: >40,d}".format(b))
print("pat :", "{: >40,d}".format(c))
print(a/b, a/c)

l = 13
res = f(l)
a = sum([26,26,10,12]) ** l
b = sum(patdat) ** l
c = res
print("full:", "{: >40,d}".format(a))
print("all :", "{: >40,d}".format(b))
print("pat :", "{: >40,d}".format(c))
print(a/b, a/c)

l = 13
res = f(l)
a = sum([26,26,10,12]) ** l
b = sum(patdat) ** l
c = res
print("full:", "{: >40,d}".format(a))
print("all :", "{: >40,d}".format(b))
print("pat :", "{: >40,d}".format(c))
print(a/b, a/c)

l = 12
res = f(l)
c = res
print("pat :", "{: >40,d}".format(c))
l = 13
res = f(l)
c = res
print("pat :", "{: >40,d}".format(c))
l = 14
res = f(l)
c = res
print("pat :", "{: >40,d}".format(c))
l = 15
res = f(l)
c = res
print("pat :", "{: >40,d}".format(c))
l = 16
res = f(l)
c = res
print("pat :", "{: >40,d}".format(c))
