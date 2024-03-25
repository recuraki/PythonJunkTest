from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

# エトラステネスのふるい
#  https://qiita.com/fantm21/items/5e270dce9f4f1d963c1e
"""
nまでの素数を一覧する。(nを含む)
>> prime_list_eratosthenes(9)
[2, 3, 5, 7, 9]
"""
def prime_list_eratosthenes(n):
    import math
    if n == 1:
        return []
    if n == 2:
        return [2]
    prime = [2]
    limit = math.sqrt(n)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit < p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

"""
n_from以上、n_to以下の素数を一覧する。(fromとtoを含む = [from, to]
>> prime_list_eratosthenes_from(5,9)
[5, 7, 9]
"""
def prime_list_eratosthenes_from(n_from, n_to):
    from bisect import bisect_left
    data = prime_list_eratosthenes(n_to)
    i = bisect_left(data, n_from)
    return data[i:]


#ps = prime_list_eratosthenes(5000000)
#ps = set(ps)


# 素数判定(ミラーラビンテスト)
# https://pashango-p.hatenadiary.org/entry/20090704/1246692091
import random
def is_prime(q, k=50):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q & 1 == 0: return False

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, q - 1)
        t = d
        y = pow(a, t, q)
        while t != q - 1 and y != 1 and y != q - 1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q - 1 and t & 1 == 0:
            return False
    return True



class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = -1
        n = len(nums)
        can = [0]
        for i in range(n):
            if is_prime(nums[i][i]): can.append(nums[i][i])
            if is_prime(nums[i][n - i - 1]) : can.append(nums[i][n-i-1])
        ans = max(can)
        assert ans != -1
        return ans


st = Solution()

print(st.diagonalPrime( nums = [[1,2,3],[5,6,7],[9,10,11]])==11)
print(st.diagonalPrime(nums = [[1,2,3],[5,17,7],[9,11,10]])==17)
print(st.diagonalPrime(nums = [[788,645,309,559],[624,160,435,724],[770,483,95,695],[510,779,984,238]])==0)

