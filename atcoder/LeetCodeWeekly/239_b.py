from typing import List, Tuple
from pprint import pprint


class Solution:
    def f(self,s, num):
        #print("f", s, num)
        if num is not None and int(s) == (num - 1):
            return True
        for i in range(1, len(s)):
            curval = s[:i]
            if num is not None and int(curval) != (num-1):
                continue
            res = self.f(s[i:], int(curval))
            if res is True:
                return True
        return False
    def splitString(self, s: str) -> bool:
        return self.f(s, None)


st = Solution()

print(st.splitString(s = "1234"))
print(st.splitString(s = "050043"))
print(st.splitString(s = "9080701"))
print(st.splitString( s = "10009998"))
