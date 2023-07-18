from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

###################################
# Paste the template of question
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = [-1] * n
        ans[0] = 0
        for i in range(n):
            if ans[i] == -1: continue
            for j in range(i+1, n):
                dist = abs(nums[i] - nums[j])
                if dist <= target:
                    ans[j] = max(ans[j], ans[i] + 1)


        return ans[-1]


st = Solution()

print(st.maximumJumps(nums = [1,3,6,4,1,2], target = 2)==3)
print(st.maximumJumps(nums = [1,3,6,4,1,2], target = 3)==5)
print(st.maximumJumps(nums = [1,3,6,4,1,2], target = 0)==-1)
#print(st.maximumJumps(nums = [1,3], target = 1)==1)
print(st.maximumJumps(nums = [0,2,1,3], target = 1)==-1)


