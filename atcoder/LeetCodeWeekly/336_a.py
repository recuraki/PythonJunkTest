from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = ["a", "i", "u", "e", "o"]
        ans = 0
        for i in range(left, right+1):
            can = False
            if words[i][0] in vowel and words[i][-1] in vowel: can = True
            if can: ans += 1
        return ans




st = Solution()

print(st.vowelStrings(words = ["are","amy","u"], left = 0, right = 2)==2)
print(st.vowelStrings( words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4)==3)

