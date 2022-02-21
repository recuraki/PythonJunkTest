from typing import List, Tuple
from pprint import pprint


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i*j) % k == 0: ans += 1
        return ans


st = Solution()

print(st.countPairs(nums = [3,1,2,2,2,1,3], k = 2))
print(st.countPairs(nums = [1,2,3,4], k = 1))
