from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cur = 0
        ans = 0
        for x in s:
            x = int(x)
            # ok ?
            if (cur * 10 + x) <= k: # "yes"
                cur = cur * 10 + x
                continue
            # else
            cur = x
            ans += 1
            if cur > k: return -1
        return ans + 1


st = Solution()

print(st.minimumPartition( s = "165462", k = 60)==4)
print(st.minimumPartition(s = "238182", k = 5)==-1)
print(st.minimumPartition(s = "1", k = 5)==1)
print(st.minimumPartition(s = "5555", k = 5)==4)
print(st.minimumPartition(s = "5", k = 5)==1)


