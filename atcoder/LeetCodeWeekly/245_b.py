from typing import List, Tuple
from pprint import pprint


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def makestr(removable):
            removable = set(removable)
            alldel = ""
            for i in range(len(s)):
                if i in removable:
                    continue
                alldel += s[i]
            return alldel

        def canmake(s):
            j = 0
            for i in range(len(s)):
                if s[i] == p[j]:
                    j += 1
                if j == len(p):
                    return True
            return False

        l = 0
        h = len(removable)
        while l <= h:
            mid = (l + h) // 2
            news = makestr(removable[:mid])
            if canmake(news):  # 買うことができるなら
                l = mid + 1  # 買えるのでそれ以上の数
            else:  # 買えないなら
                h = mid - 1  # 買えないのでそれ以下の数をトライ
        news = makestr(removable[:min(l, h)])
        if canmake(news):  # 買うことができるなら
            return min(l, h)
        else:
            return max(l, h)

st = Solution()

print(st.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0]))
print(st.maximumRemovals(s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]))
print(st.maximumRemovals(s = "abcab", p = "abc", removable = [0,1,2,3,4]))
print(st.maximumRemovals("qlevcvgzfpryiqlwy", "qlecfqlw", [12,5])==2)
