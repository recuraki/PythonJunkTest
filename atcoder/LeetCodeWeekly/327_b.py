from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
        from heapq import heappop, heappush, heapify
        q = []
        for x in nums:
            q.append(-x)
        heapify(q)
        ans = 0
        for _ in range(k):
            x = -heappop(q)
            ans += x
            heappush(q, - ceil(x, 3))
        return ans



st = Solution()

print(st.maxKelements(nums = [10,10,10,10,10], k = 5)==50)
print(st.maxKelements(nums = [1,10,3,3,3], k = 3)==17)

