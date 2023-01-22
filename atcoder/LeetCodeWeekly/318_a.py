from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        print(nums)
        cnt0 = 0
        for x in nums:
            if x == 0: cnt0 += 1
            else: ans.append(x)
        for _ in range(cnt0):
            ans.append(0)
        return ans


st = Solution()

print(st.applyOperations(nums = [1,2,2,1,1,0])==[1,4,2,0,0,0])
print(st.applyOperations(nums = [0,1])==[1,0])

