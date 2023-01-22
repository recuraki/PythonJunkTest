from typing import List, Tuple
from pprint import pprint


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        isis = [False] * 26
        for x in sentence:
            x = ord(x) - ord("a")
            isis[x] = True
        return all(isis)


st = Solution()

print(st.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(st.checkIfPangram("leetcode"))

