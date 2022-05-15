from typing import List, Tuple
from pprint import pprint


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        l = []
        p = None
        for x in nums:
            if x == p: continue
            l.append(x)
            p = x
        nums = l
        n = len(nums)
        for i in range(1, len(nums) - 1):
            lval = None
            rval = None
            for j in range(i+1, n):
                if nums[j] != nums[i]:
                    rval = nums[j]
                    break
            for j in range(i-1, -1, -1):
                if nums[j] != nums[i]:
                    lval = nums[j]
                    break
            if lval is None: continue
            if rval is None: continue
            if lval < nums[i] and nums[i] > rval: ans += 1
            if lval > nums[i] and nums[i] < rval: ans += 1
        print(ans)
        return ans

st = Solution()

print(st.countHillValley(nums = [2,4,1,1,6,5])==3)
print(st.countHillValley( nums = [6,6,5,5,4,1])==0)

