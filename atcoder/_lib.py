MOD1 = 1000000007 # 10^9 + 7
MOD2 = 1000000009 # 10^9 + 9
MOD3 = 100000007 # 10^8 + 7
MOD4 = 1234567891
def factorial_mod(n, mod):
    import math
    return math.factorial(n) % mod

# 組み合わせ
def nCr(n, r):
    import math
    return math.factorial(n) //  ( (math.factorial(n - r) * math.factorial(r)) )


def nCr_with_replacement(n, r):
    # 重複を許容するくみあわせ　
    return nCr(n + r - 1, r)

# 並び変えるときの組み合わせ
def nPr(n, r):
    import math
    return math.factorial(n) // math.factorial(n - r)

# 最小公倍数
# x,yに0が入ると0になるので、適当に初期値を入れましょう。(最悪1でいいと思います)
def lcm(x, y):
    import fractions
    return (x * y) // fractions.gcd(x, y)

# https://docs.python.org/ja/3/library/bisect.html#searching-sorted-lists
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

import unittest

class TestClass(unittest.TestCase):
    def test_nCr_1(self):
        r = nPr(4, 2)
        self.assertEqual(r, 12)

if __name__ == "__main__":
    pass
