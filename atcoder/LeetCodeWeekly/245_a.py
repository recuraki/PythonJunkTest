from typing import List, Tuple
from pprint import pprint


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter
        C = Counter()
        for s in words:
            C += Counter(s)
        for k in C.keys():
            if C[k] % len(words):
                return False

        return True



st = Solution()

print(st.makeEqual(words = ["abc","aabc","bc"]))
print(st.makeEqual( words = ["ab","a"]))
