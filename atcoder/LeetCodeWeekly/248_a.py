from typing import List, Tuple
from pprint import pprint


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res



st = Solution()

print(st.buildArray( nums = [0,2,1,5,3,4]))
print(st.buildArray(nums = [5,0,1,2,3,4]))
