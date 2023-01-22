from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict




# https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
# 素因数分解
"""
>>> factorization(16)
[[2, 4]]
>>> factorization(48)
[[2, 4], [3, 1]]
"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        import collections
        se = defaultdict(int)
        for num in nums:
            l = factorization(num)
            for x, _ in l:
                se[x] += 1
        ans = 0
        for k in se.keys():
            ans += 1
        return ans


st = Solution()

print(st.distinctPrimeFactors(nums = [2,4,3,7,10,6])==4)
print(st.distinctPrimeFactors(nums = [2,4,8,16])==1)

