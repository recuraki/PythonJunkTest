from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a = 0
        s = str(n)
        for i in range(n):
            if (i%2 == 0): a += int(s[i])
            if (i%2 == 1): a -= int(s[i])
        return a



st = Solution()

print(st.alternateDigitSum(512)==4)

