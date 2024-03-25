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


primes = prime_list_eratosthenes(1000000 + 10)


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = 10**9
        ansval = [-1, -1]
        for i in range(len(primes) - 1):
            nums1 = primes[i]
            nums2 = primes[i+1]
            if left <= nums1 and nums2 <= right:
                delta = nums2 - nums1
                if delta < ans:
                    ans = delta
                    ansval = [nums1, nums2]

        return ansval


st = Solution()

print(st.closestPrimes(left = 10, right = 19)==[11,13])
print(st.closestPrimes(left = 4, right = 6)==[-1,-1])

