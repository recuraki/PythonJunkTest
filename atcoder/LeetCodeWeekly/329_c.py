from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target: return True
        if target.count("1") == 0: return False # 0を消せない
        if s.count("1") == 0: return False # 1を創れない
        return True



st = Solution()

print(st.makeStringsEqual( s = "1010", target = "0110")==True)
print(st.makeStringsEqual(s = "11", target = "00")==False)

