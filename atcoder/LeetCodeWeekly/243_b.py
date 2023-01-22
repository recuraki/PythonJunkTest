
from typing import List, Tuple
from pprint import pprint


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        res = ""
        if n[0] != "-":
            i = 0
            while i < len(n):
                if int(n[i]) < x:
                    break
                res += n[i]
                i+= 1
            res += str(x)
            for i in range(i, len(n)):
                res += n[i]
            return(res)
        else:
            res = "-"
            i = 1
            while i < len(n):
                if int(n[i]) > x:
                    break
                res += n[i]
                i+= 1
            res += str(x)
            for i in range(i, len(n)):
                res += n[i]
            return(res)




st = Solution()

print(st.maxValue(n = "99", x = 9) == "999" )
print(st.maxValue(n = "-13", x = 2) == "-123")
print(st.maxValue(n = "-666", x = 6))
print(st.maxValue(n = "-686", x = 6))
print(st.maxValue(n = "-68686", x = 6))
