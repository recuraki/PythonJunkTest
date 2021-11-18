from typing import List, Tuple
from pprint import pprint

###################################
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import defaultdict
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        ss = set()
        for x in word1: d1[x] += 1
        for x in word2: d2[x] += 1
        for x in word1: ss.add(x)
        for x in word2: ss.add(x)
        for x in ss:
            if abs(d1[x] - d2[x]) > 3: return False
        return True



###################################


st = Solution()

print(st.checkAlmostEquivalent(word1 = "aaaa", word2 = "bccb"))
print(st.checkAlmostEquivalent(word1 = "abcdeef", word2 = "abaaacc"))
print(st.checkAlmostEquivalent(word1 = "cccddabba", word2 = "babababab"))
