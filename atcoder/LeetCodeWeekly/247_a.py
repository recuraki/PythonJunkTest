
from typing import List, Tuple
from pprint import pprint


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] * nums[-1] - nums[0] * nums[1])


st = Solution()

print(st.maxProductDifference(nums = [5,6,2,7,4]))
print(st.maxProductDifference(nums = [4,2,5,9,7,4,8]))
