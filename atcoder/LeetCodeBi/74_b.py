from typing import List, Tuple
from pprint import pprint


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        def f(s, t):
            a = t[0]
            b = t[1]
            cnta = 0
            cntb = 0
            ans = 0
            for x in s:
                if x == b:
                    ans += cnta
                if x == a:
                    cnta += 1
            return(ans)
        ans = 0
        s = pattern[0] + text
        t = f(s, pattern)
        ans = max(ans, t)

        s = text + pattern[1]
        t = f(s, pattern)
        ans = max(ans, t)


        s = pattern[1] + text
        t = f(s, pattern)
        ans = max(ans, t)

        s = text + pattern[0]
        t = f(s, pattern)
        ans = max(ans, t)


        return ans




st = Solution()

print(st.maximumSubsequenceCount(text = "abdcdbc", pattern = "ac")==4)
print(st.maximumSubsequenceCount(text = "aabb", pattern = "ab")==6)

