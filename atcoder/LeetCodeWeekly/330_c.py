from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:


st = Solution()

print(st.putMarbles( weights = [1,3,5,1], k = 2)==4)
print(st.putMarbles(weights = [1, 3], k = 2)==0)

