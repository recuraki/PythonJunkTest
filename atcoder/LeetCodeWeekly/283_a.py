
from typing import List, Tuple
from pprint import pprint


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a = s[0]
        b = int(s[1])
        c = s[3]
        d = int(s[4])
        a = ord(a) - ord("A")
        c = ord(c) - ord("A")
        ans = []
        for i in range(a, c+1):
            for j in range(b, d+1):
                s = chr(ord("A") + i) + str(j)
                ans.append(s)
        return ans



st = Solution()

print(st.cellsInRange("K1:L2"))
print(st.cellsInRange("A1:F1"))
