from typing import List, Tuple
from pprint import pprint


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i +1 , n):
                for k in range(j+1, n):
                    a,b,c = nums[i], nums[j], nums[k]
                    if nums[j] - nums[i] == diff:
                        if nums[k] - nums[j] == diff:
                            ans += 1
        return ans


st = Solution()

print(st.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3)==2)
print(st.arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2)==2)

