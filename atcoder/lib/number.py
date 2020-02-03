MOD1 = 1000000007 # 10^9 + 7
MOD2 = 1000000009 # 10^9 + 9
MOD3 = 100000007 # 10^8 + 7
MOD4 = 1234567891
alphabet_low = "abcdefghijklmnopqrstuvwxyz"
alphabet_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 小数の表記
format(z, '.10f')

def factorial_mod(n, mod):
    import math
    return math.factorial(n) % mod

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

"""
>> each_prime([2,3])
True
>> each_prime([3, 63, 7])
False
"""
# リスト内の数が互いに素かを確認する
def each_prime(l):
    f = True
    import fractions
    for i in range(len(l)):
        #print("try {0}", l[i])
        for j in range(1, len(l)- i):
            #print(" div {0}", l[i + j])
            if fractions.gcd(l[i], l[i+j]) != 1:
                f = False
                break
        if f is False:
            break
    return f

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

# エトラステネスのふるい
#  https://qiita.com/fantm21/items/5e270dce9f4f1d963c1e
"""
nまでの素数を一覧する。(nを含む)
>> prime_list_eratosthenes(9)
[2, 3, 5, 7, 9]
"""
def prime_list_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

"""
n_from以上、n_to以下の素数を一覧する。(fromとtoを含む
>> prime_list_eratosthenes_from(5,9)
[5, 7, 9]
"""
def prime_list_eratosthenes_from(n_from, n_to):
    from bisect import bisect_left
    data = prime_list_eratosthenes(n_to)
    i = bisect_left(data, n_from)
    return data[i:]



import unittest
class TestClass(unittest.TestCase):
    def test_nCr_1(self):
        r = nPr(4, 2)
        self.assertEqual(r, 12)

if __name__ == "__main__":
    import math
    print(math.gcd(100,0))