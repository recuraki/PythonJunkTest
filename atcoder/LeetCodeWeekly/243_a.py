from typing import List, Tuple
from pprint import pprint


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = ""
        b = ""
        c = ""
        for x in firstWord:
            a += str(ord(x) - ord("a"))
        for x in secondWord:
            b += str(ord(x) - ord("a"))
        for x in targetWord:
            c += str(ord(x) - ord("a"))
        if int(a) + int(b) == int(c):
            return True
        return False



st = Solution()

print(st.isSumEqual(firstWord = "acb", secondWord = "cba", targetWord = "cdb"))
print(st.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aab"))
print(st.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aaaa"))
