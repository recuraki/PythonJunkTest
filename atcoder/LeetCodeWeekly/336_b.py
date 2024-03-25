from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        cur = 0
        pre = []
        for i in range(len(nums)):
            cur += nums[i]
            pre.append(cur)
        #print(pre)
        ans = 0
        for x in pre:
            if x > 0: ans += 1
        return ans


st = Solution()

print(st.maxScore(nums = [2,-1,0,1,-3,3,-3])==6)
print(st.maxScore(nums = [-2,-3,0])==0)

