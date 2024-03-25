from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


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

ps = prime_list_eratosthenes(1000)

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        nums.reverse()
        nums = list(nums)
        #print(nums)
        from bisect import bisect_left
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i+1]
            if a > b: continue
            diff = (b - a) + 1
            ind = bisect_left(ps, diff)
            if ind == len(ps): return False
            can = ps[ind]
            if can >= b: return False
            nums[i+1] -= can
        nums.reverse()
        nums = list(nums)
        #print(nums)
        return True





st = Solution()

print(st.primeSubOperation( nums = [4,9,6,10])==True)
print(st.primeSubOperation(nums = [6,8,11,12])==True)
print(st.primeSubOperation(nums = [5,8,3])==False)
print(st.primeSubOperation(nums = [1])==True)
print(st.primeSubOperation(nums = [1000,1])==False)

