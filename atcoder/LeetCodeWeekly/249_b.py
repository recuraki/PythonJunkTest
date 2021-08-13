from typing import List, Tuple
from pprint import pprint


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pos = [[] for _ in range(26)]
        for i in range(len(s)):
            val = ord(s[i]) - ord("a")
            pos[val].append(i)
        #for i in range(26):
        #    print(i, pos[i])
        from bisect import bisect_right
        res = 0
        for alpha in range(26):
            if len(pos[alpha]) < 2: continue
            l, r = pos[alpha][0], pos[alpha][-1]
            for center in range(26):
                ind = bisect_right(pos[center], l)
                if ind >= len(pos[center]) : continue
                #print(alpha, l, r, center, pos[center][ind])
                if pos[center] == r: continue
                if l < pos[center][ind] < r:
                    res += 1
        return res



st = Solution()

print(st.countPalindromicSubsequence( s = "aabca"))
print(st.countPalindromicSubsequence( s = "adc"))
print(st.countPalindromicSubsequence( s = "bbcbaba"))
print(st.countPalindromicSubsequence( s = "baabab"))
