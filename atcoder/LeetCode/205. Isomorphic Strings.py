class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        rev = dict()
        for i in range(len(s)):
            ch = s[i]
            if ch not in d:
                d[ch] = t[i]
            if d[ch] != t[i]: return False
            ch = t[i]
            if ch not in rev:
                rev[ch] = s[i]
            if rev[ch] != s[i]: return False
        return True