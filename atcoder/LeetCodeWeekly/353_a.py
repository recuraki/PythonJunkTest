from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t*2)


st = Solution()

print(st.theMaximumAchievableX(num = 4, t = 1)==6)
print(st.theMaximumAchievableX(num = 3, t = 2)==7)

