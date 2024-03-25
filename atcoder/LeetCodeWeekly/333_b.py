from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict



def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

class Solution:
    def minOperations(self, n: int) -> int:
        ans = 10**18
        for i in range(1<<18):
            cur = popcount(i)
            x = n + i
            b = bin(x)[2:]
            l = countstrs(b)
            for ch, cnt in l:
                ch = int(ch)
                if ch == 0:
                    continue
                if cnt == 1:
                    cur += 1
                    continue
                cur += 2
            ans = min(ans, cur)
        return ans




st = Solution()

print(st.minOperations(n = 39)==3)
print(st.minOperations(n = 54)==3)

