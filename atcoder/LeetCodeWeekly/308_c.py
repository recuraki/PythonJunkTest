from typing import List, Tuple
from pprint import pprint


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        allM = allP = allG = 0
        for s in garbage:
            for l in list(s):
                if l == "M": allM += 1
                if l == "P": allP += 1
                if l == "G": allG += 1

        M, P, G = 0, 0, 0
        ans = 0
        def f(targetch, targetnum):
            ans = 0
            collected = 0
            collected += garbage[0].count(targetch)
            ans += garbage[0].count(targetch)
            i = 0
            while  collected < targetnum:
                ans += travel[i]
                i += 1
                collected += garbage[i].count(targetch)
                ans += garbage[i].count(targetch)
            return ans
        ans += f("M", allM)
        ans += f("P", allP)
        ans += f("G", allG)
        return ans







st = Solution()

print(st.garbageCollection( garbage = ["G","P","GP","GG"], travel = [2,4,3])==21)
print(st.garbageCollection( garbage = ["MMM","PGM","GP"], travel = [3,10])==37)

