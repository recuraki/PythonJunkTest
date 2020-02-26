MOD1 = 1000000007 # 10^9 + 7
MOD2 = 1000000009 # 10^9 + 9
MOD3 = 100000007 # 10^8 + 7
MOD4 = 1234567891
alphabet_low = "abcdefghijklmnopqrstuvwxyz"
alphabet_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 小数の表記
format(z, '.10f')

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
"""
import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)



import unittest
class TestClass(unittest.TestCase):
    def test_nCr_1(self):
        r = nPr(4, 2)
        self.assertEqual(r, 12)

if __name__ == "__main__":
    import math
    print(math.gcd(100,0))