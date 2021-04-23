from typing import List, Tuple

class Solution:
    def makeStringSorted(self, s: str) -> int:
        m = 10**9 + 7
        n = len(s)
        res = 0
        os = list(s)
        s = list(s)
        s.sort()
        for i in range(n):
            targetchar = os[i]
            if s[i] == targetchar:
                continue
            cnt = 1
            for j in range(i, n):
                if s[j] == targetchar:
                    cnt *= (n - j + 1)
                    s[i], s[j] = s[j], s[i]
                    cnt %= m
                    break
                if s[j] < targetchar:
                    cnt *= (n - j + 1)
                    cnt %= m
            res += cnt
            res %= m
        return res



st = Solution()

print(st.makeStringSorted(s = "cba"))
print(st.makeStringSorted(s = "aabaa"))
print(st.makeStringSorted(s = "cdbea"))
print(st.makeStringSorted(s = "leetcodeleetcodeleetcode"))
