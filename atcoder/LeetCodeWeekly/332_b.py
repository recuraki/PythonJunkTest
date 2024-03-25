from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        from bisect import bisect_left, bisect_right
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            x = nums[i]
            l = bisect_left(nums, lower - x, i+1)
            r = bisect_right(nums, upper - x, i+1)
            ans += r - l
        return ans



st = Solution()

print(st.countFairPairs(nums = [-5,-7,-5,-7,-5], lower = -12, upper = -12)==6)
print(st.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)==6)
print(st.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11)==1)

