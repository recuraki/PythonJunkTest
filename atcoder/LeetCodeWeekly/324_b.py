from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


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
    def smallestValue(self, n: int) -> int:
        se = set()
        ans = n
        se.add(n)
        while True:
            l = factorization(n)
            nn = 0
            for a, b in l:
                nn += a * b
            ans = min(ans, nn)

            if nn in se: break
            n = nn
            se.add(nn)
        return ans


st = Solution()

print(st.smallestValue(n = 15)==5)
print(st.smallestValue(n = 3)==3)

