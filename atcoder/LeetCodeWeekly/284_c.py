from typing import List, Tuple
from pprint import pprint


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0: return nums[0]
        if n == 1:
            if k % 2 == 1:
                return -1
            else:
                return nums[0]
        if k == 1:
            return nums[1]
        if k > n:
            return max(nums)
        if k == n:
            return max(nums[:-1])
        if k < n:
            ans = max(nums[:k-1])
            ans = max(ans , nums[k])
            return ans


st = Solution()

print(st.maximumTop(nums = [5,2,2,4,0,6], k = 4))
print(st.maximumTop(nums = [2], k = 1))
print(st.maximumTop(nums=[4,6,1,0,6,2,4], k=0)==4)