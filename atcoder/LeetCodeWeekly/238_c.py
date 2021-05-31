from typing import List, Tuple
from pprint import pprint


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        judge = lambda : cnt[0]!=0 and cnt[8]!=0 and cnt[20]!=0 and cnt[4]!=0 and cnt[14]!=0
        chr2int = lambda x: ord(x) - ord("a")
        s,l,r = word,0,0
        s = list(map(chr2int, s))
        cnt = [0] * 26
        res = 0
        p = -1
        while r < len(s):
            cnt[s[r]] += 1
            # 足した文字が条件を達成しているか？
            if s[r] < p:
                l = r
                r += 1
                p = s[r]
                continue
            p = s[r]
            if judge(): # 文字が足りている
                res = max(res, (r-l) + 1)
            r += 1
        return res

st = Solution()
print(st.longestBeautifulSubstring(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"))
print(st.longestBeautifulSubstring(word = "aeeeiiiioooauuuaeiou"))
print(st.longestBeautifulSubstring(word = "a"))

