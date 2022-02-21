from typing import List, Tuple
from pprint import pprint


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        from heapq import heapify, heappop, heappush
        ql = []
        qr = []
        for i in range(len(nums)):
            ql.append( (-nums[i], i) )
            qr.append( )








st = Solution()

print(st.minimumDifference(nums = [3,1,2]))
print(st.minimumDifference(nums = [7,9,5,8,1,3]))

