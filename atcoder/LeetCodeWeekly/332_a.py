from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        q = deque(nums)
        ans = 0
        while(len(q) > 0):
            s = ""
            if len(q) > 0:
                ss = q.popleft()
                ss = str(ss)
                s += ss
            if len(q) > 0:
                ss = q.pop()
                ss = str(ss)
                s += ss
            ans += int(s)
        return ans





st = Solution()

print(st.findTheArrayConcVal(nums = [7,52,2,4])==596)
print(st.findTheArrayConcVal(nums = [5,14,13,8,12])==673)

