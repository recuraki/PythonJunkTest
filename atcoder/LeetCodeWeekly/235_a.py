from typing import List, Tuple
import re


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return (" ".join(s.split(" ")[:k]))

st=Solution()
print(st.truncateSentence(s = "Hello how are you Contestant", k = 4))
print(st.truncateSentence(s = "Hello how are you Contestant", k = 4))
print(st.truncateSentence( s = "chopper is not a tanuki", k = 5))

