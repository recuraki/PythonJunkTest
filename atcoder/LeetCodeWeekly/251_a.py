from typing import List, Tuple
from pprint import pprint


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t = ""
        for x in s:
            a = ord(x) - ord("a") + 1
            t += str(a)
        for _ in range(k):
            tmp = 0
            for x in t:
                tmp += int(x)
            t = str(tmp)
        return(int(t))




st = Solution()

print(st.getLucky( s = "iiii", k = 1))
print(st.getLucky(  s = "leetcode", k = 2))
print(st.getLucky(  s = "zbax", k = 2))
