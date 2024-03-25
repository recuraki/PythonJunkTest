from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        s = str(num)
        for i in range(len(s)):
            x = int(s[i])
            if num % x == 0: ans += 1
        return ans


st = Solution()

print(st.countDigits(7)==1)
print(st.countDigits(121)==2)
print(st.countDigits(1248)==4)

