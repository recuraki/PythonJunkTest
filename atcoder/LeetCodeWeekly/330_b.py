from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def monkeyMove(self, n: int) -> int:
        ans = pow(2, n, 10**9+7) - 2
        return ans % (10**9+7)


st = Solution()

print(st.monkeyMove(3)==6)
print(st.monkeyMove(4)==14)
print(st.monkeyMove(500000003)==1000000006)

