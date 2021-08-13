from typing import List, Tuple
from pprint import pprint


class Solution:
    def minFlips(self, s: str) -> int:
        import itertools
        squery0 = lambda a, b: sdat0[b] - sdat0[a]  # query [a, b)
        squery1 = lambda a, b: sdat1[b] - sdat1[a]  # query [a, b)
        def createSDAT(l):
            return list(itertools.accumulate(itertools.chain([0], l)))

        n = len(s)
        s1 = ("01"*n)[:n]
        s2 = ("10"*n)[:n]
        #print(s1,s2)

        ans0start = [0] * (n)
        ans1start = [0] * (n)

        finalres = 10**18
        c1 = 0
        c2 = 0
        for i in range(n):
            if s[i] != s1[i]: ans0start[i] = 1
            if s[i] != s2[i]: ans1start[i] = 1
        sdat0 = createSDAT(ans0start)
        sdat1 = createSDAT(ans1start)
        #print(ans0start)
        #print(ans1start)
        finalres = 10**18
        for i in range(n):
            # 0 スタート
            res = 0
            res += squery0(i, n) # 自分から最後
            kukan = n - i
            if kukan % 2 == 0:
                if i%2 == 0:
                    res += squery0(0, i)
                else:
                    res += squery1(0, i)
            else:
                if i%2 == 0:
                    res += squery1(0, i)
                else:
                    res += squery0(0, i)

            finalres = min(finalres, res)
            res = 0
            res += squery1(i, n) # 自分から最後
            kukan = n - i
            if kukan % 2 == 0:
                if i%2 == 0:
                    res += squery1(0, i)
                else:
                    res += squery0(0, i)
            else:
                if i%2 == 0:
                    res += squery0(0, i)
                else:
                    res += squery1(0, i)
            finalres = min(finalres, res)

        return finalres




st = Solution()

print(st.minFlips(s = "111000")==2)
print(st.minFlips(s = "010")==0)
print(st.minFlips(s = "1110")==1)
print(st.minFlips(s = "1")==0)
print(st.minFlips(s = "10")==0)
print(st.minFlips(s = "01")==0)
print(st.minFlips("01001001101"))
print(st.minFlips("01001001101")==2)
print(st.minFlips("10001100101000000") == 5)
print(st.minFlips("001000000010") == 4)