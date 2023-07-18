from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n == 1:
            return 1
        return (n-1)



st = Solution()

print(st.distinctIntegers(5)==4)
print(st.distinctIntegers(3)==2)
print(st.distinctIntegers(2)==1)

