from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        l = [0]
        r = []
        x = sum(nums)
        x -= nums[0]
        r.append(x)
        for i in range(len(nums)- 1):
            l.append(l[-1] + nums[i])
            r.append(r[-1] - nums[1+i])
        ans = []
        for i in range(len(nums)): ans.append(abs(l[i] - r[i]))
        return ans


st = Solution()

print(st.leftRigthDifference(nums = [10,4,8,3])==0)
print(st.leftRigthDifference(nums = [1])==0)

