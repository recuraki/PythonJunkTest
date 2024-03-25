from typing import List, Tuple
from pprint import pprint


class Solution:
    def removeStars(self, s: str) -> str:
        from collections import deque
        ans = deque([])
        for x in list(s):
            if x == "*": ans.pop()
            else: ans.append(x)
        return "".join(ans)


st = Solution()

print(st.removeStars(s = "leet**cod*e")=="lecoe")
print(st.removeStars(s = "erase*****")=="")

