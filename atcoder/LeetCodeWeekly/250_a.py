from typing import List, Tuple
from pprint import pprint


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ng = set(list(brokenLetters))
        res = 0
        for x in text.split(" "):
            can = True
            for ww in ng:
                if ww in x:
                    can = False
            if can: res += 1
        return res



st = Solution()

print(st.canBeTypedWords(text = "hello world", brokenLetters = ""))
print(st.canBeTypedWords(text = "hello world s x", brokenLetters = "ad"))
print(st.canBeTypedWords(text = "leet code", brokenLetters = "lt"))
print(st.canBeTypedWords(text = "leet code", brokenLetters = "e"))
