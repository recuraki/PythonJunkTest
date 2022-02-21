from typing import List, Tuple
from pprint import pprint


class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for s in range(1, num + 1):
            cnt = 0
            ss = list(str(s))
            for x in ss:
                cnt += int(x)
            if cnt % 2 == 0: ans += 1
        return ans


st = Solution()

print(st.countEven(4))
print(st.countEven(30))
