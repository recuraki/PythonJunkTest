from typing import List, Tuple
from pprint import pprint


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(1, len(words)+1):
            t = "".join(words[:i])
            #print(s,t)
            if len(t) != len(s): continue
            if t.find(s) == 0:
                return True
        return False


st = Solution()

print(st.isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"]))
print(st.isPrefixString(s = "iloveleetcode", words = ["apples","i","love","leetcode"]))
print(st.isPrefixString("a", ["aa","aaaa","banana"]))
print(st.isPrefixString("z", ["z"]))


