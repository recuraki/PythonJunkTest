from typing import List, Tuple
import re

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = re.sub("[a-z]+", " ", word)
        ss = set()
        for x in s.split():
            ss.add(int(x))
        print(ss)
        return(len(ss))


st = Solution()
print(st.numDifferentIntegers("a123bc34d8ef34"))
print(st.numDifferentIntegers("leet1234code234"))
print(st.numDifferentIntegers("a1b01c001"))
