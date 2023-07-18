from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:


st = Solution()

print(st.minimizeMax(nums = [10,1,2,7,1,3], p = 2)==1)
print(st.minimizeMax( nums = [4,2,1,2], p = 1)==0)

