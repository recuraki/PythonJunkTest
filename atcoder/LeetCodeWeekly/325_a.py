
from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

###################################
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = 1000000
        for i in range(300):
            if words[(startIndex+i) % len(words)] == target:
                ans = min(ans, i)
            if words[(startIndex-i) % len(words)] == target:
                ans = min(ans, i)
        if ans == 1000000: return -1
        return ans



st = Solution()

print(st.closetTarget( words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1)==1)
print(st.closetTarget(words = ["a","b","leetcode"], target = "leetcode", startIndex = 0)==1)
print(st.closetTarget(words = ["i","eat","leetcode"], target = "ate", startIndex = 0)==-1)

