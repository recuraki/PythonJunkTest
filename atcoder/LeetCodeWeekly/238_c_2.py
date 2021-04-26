from typing import List, Tuple
from pprint import pprint

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        dat = []
        char2int = lambda x: ord(x) - ord("a")
        for x in word:  dat.append(char2int(x))
        buf = []
        l, p = 0, -1
        # 単純増加な区間を[l, r] (閉区間)としてbufに記録
        for i in range(len(word)):
            if dat[i] < p:
                r = i-1
                p = dat[i]
                buf.append((l, r))
                l = i
            else:
                p = dat[i]
        buf.append( ( l, len(word) - 1) )
        res = 0
        # 各l, rに対してa,i,u,e,oが含まれているかを判定
        for l, r in buf:
            judge = [False] * 5
            for i in range(l, r + 1):
                if dat[i] == 0: judge[0] = True # a
                if dat[i] == 8: judge[1] = True # a
                if dat[i] == 20: judge[2] = True # a
                if dat[i] == 4: judge[3] = True # a
                if dat[i] == 14: judge[4] = True # a
            if all(judge): res = max(res, (r-l)+1)
        return res


st = Solution()

print(st.longestBeautifulSubstring(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 13)
print(st.longestBeautifulSubstring(word = "aeeeiiiioooauuuaeiou")==5)
print(st.longestBeautifulSubstring(word = "a") == 0)
