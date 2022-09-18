from typing import List, Tuple
from pprint import pprint


class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        se = set()
        for i in range(len(s)):
            x = s[i]
            #print(i, x, se)
            if x not in se:
                se.add(x)
                continue
            #print("---")
            ans += 1
            se = set()
            se.add(x)
        #print(se)
        ans += 1
        return ans



st = Solution()

print(st.partitionString(s = "abacaba")==4)
print(st.partitionString(s = "ssssss")==6)
print(st.partitionString(s = "anv")==1)
print(st.partitionString(s = "a")==1)
print(st.partitionString(s = "abab")==2)


