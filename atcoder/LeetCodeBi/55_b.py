from typing import List, Tuple
from pprint import pprint


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            a = len(s)
            s = s.replace(part, "")
            b = len(s)
            if a == b:
                break
        return s

st = Solution()

print(st.removeOccurrences(s = "daabcbaabcbc", part = "abc"))
print(st.removeOccurrences(s = "axxxxyyyyb", part = "xy"))
