from typing import List, Tuple
from pprint import pprint

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        dat = []
        char2int = lambda x: ord(x) - ord("a")
        for x in word:  dat.append(char2int(x))
        l, r, p, res = 0, 0,-1, 0
        judge = [False] * 5
        for r in range(len(word)):
            if dat[r] < p:
                p = dat[r]
                judge = [False] * 5
                if dat[r] == 0: judge[0] = True  # a
                if dat[r] == 8: judge[1] = True  # i
                if dat[r] == 20: judge[2] = True  # u
                if dat[r] == 4: judge[3] = True  # e
                if dat[r] == 14: judge[4] = True  # o
                l = r
            else:
                if dat[r] == 0: judge[0] = True  # a
                if dat[r] == 8: judge[1] = True  # i
                if dat[r] == 20: judge[2] = True  # u
                if dat[r] == 4: judge[3] = True  # e
                if dat[r] == 14: judge[4] = True  # o
                if all(judge): res = max(res, (r - l) + 1)
                p = dat[r]
        print(res)
        return res


st = Solution()

print(st.longestBeautifulSubstring(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 13)
print(st.longestBeautifulSubstring(word = "aeeeiiiioooauuuaeiou")==5)
print(st.longestBeautifulSubstring(word = "a") == 0)
