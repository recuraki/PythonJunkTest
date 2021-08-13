from typing import List, Tuple
from pprint import pprint


class Solution:
    def minStoneSum(self, qq: List[int], k: int) -> int:
        from heapq import heappop, heappush, heapify
        import math
        q = []
        for x in qq:
            heappush(q, -x)
        heapify(q)
        for _ in range(k):
            x = -heappop(q)
            #print(x)
            x = x - (x//2)
            #print("->", x)
            heappush(q, -x)

        res = 0
        while(len(q) > 0):
            res += heappop(q)
        return -res




st = Solution()

print(st.minStoneSum(qq = [5,4,9], k = 2))
print(st.minStoneSum(qq = [4,3,6,7], k = 3))
