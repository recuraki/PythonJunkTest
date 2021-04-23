from typing import List, Tuple


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        for i in range(1, len(nums)):
            p = nums[i-1] + 1
            if nums[i] > p:
                continue
            res += p - nums[i]
            nums[i] = p
        return res



st = Solution()

print(st.minOperations(nums = [1,1,1]))
print(st.minOperations(nums = [1,5,2,4,1]))
print(st.minOperations(nums = [8]))
