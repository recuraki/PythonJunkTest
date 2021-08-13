MOD1 = 1000000007 # 10^9 + 7
MOD2 = 1000000009 # 10^9 + 9
MOD3 = 100000007 # 10^8 + 7
MOD4 = 1234567891
alphabet_low = "abcdefghijklmnopqrstuvwxyz"
alphabet_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



# 小数の表記
# 0.1200000000
print(format(0.12, '.10f'))

# 0010
print(format(10, '04d'))



# n乗
# 基本的にpow
# pow(n, x, mod)

# 約数のリストを表示する(因数分解ではない)
# ソートされていない
"""
make_divisors(16)
# [1, 16, 2, 8, 4\]
"""
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors

# 約数のリストを表示する(1とその数を除く)
# ソートされていない
"""
make_divisors_without_own(16)
[2, 8, 4]
"""
def make_divisors_without_own(n):
    r = make_divisors(n)
    r.remove(1)
    r.remove(n)
    return r

# 最大公約数
"""
>> fractions.gcd(0,6)
6

import fractions
fractions.gcd(x, y)
"""

# 最小公倍数
"""
>> lcm(3,7)
21
>> lcm(1, 7)
7
>> lcm(0, 7)
0
>>> lcmList([1])
1
>>> lcmList([2,3])
6
>>> lcmList([2,3,3])
6
>>> lcmList([2,3,3,5])
30
"""
import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def lcmList(l):
    x = 1
    for i in range(len(l)):
        x = lcm(x, l[i])
    return x

"""
>>> gcdList([3])
3
>>> gcdList([3,6])
3
>>> gcdList([12, 18])
6
>>> gcdList([12, 18, 7])
1"""
def gcdList(l):
    x = 0
    for i in range(len(l)):
        x = math.gcd(x, l[i])
    return x





"""
>> print(sumdigits(12345))
 15
>> print(sumdigits(10000))
 1
>> print(sumdigits(20000))
 2
"""
# 各桁の和を得る 123なら 1+2+3 = 6
def sumdigits(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

"""
>> print(isDiffrentDigits(12345))
 True
>> print(isDiffrentDigits(12341))
 False
>> print(isDiffrentDigits(12344))
 False
>> print(isDiffrentDigits(1))
 True
>> print(isDiffrentDigits(0))
 True
"""
def isDiffrentDigits(n):
    used = 0
    while n > 0:
        x = n % 10
        n //= 10
        if used & (1 << x) != 0:
            return False
        used |= 1 << x
    return True

import math
# nを含むそれまでに、xで割り切れる数は何個ありますか？
def warerukazu(n, x):
    n // x



# 平方数で割れる数
import math
mnum = 10 ** 6 + 1000
mnumsqr = math.ceil(math.sqrt(mnum)) + 10
# mCanDivSqrt[x]  x can div max(sqrt num)
# ex. 80 can be dived 4(2^2) or 16(4^2)
#     this table ret maxnum = 16
mCanDivSqrt = [-1] * (mnum + 10)
for i in range(2, mnumsqr):
    if i ** 2 < mnum + 1:
        cur = i**2
        x = cur
        while x <= mnum:
            mCanDivSqrt[x] = i**2
            x += cur




if __name__ == "__main__":
    import math
    print(isDiffrentDigits(12345))
    print(isDiffrentDigits(12341))
    print(isDiffrentDigits(12344))
    print(isDiffrentDigits(1))
    print(isDiffrentDigits(0))
    print(make_divisors(100000006))