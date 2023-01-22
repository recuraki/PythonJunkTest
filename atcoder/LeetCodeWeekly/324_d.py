from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ret = []
        for u, v in queries:
            if u > v: u, v = v, u
            # u < vとする
            assert u != v
            ans = 0
            u -= 0
            v -= 0
            su = bin(u)[2:]
            sv = bin(v)[2:]
            #print(su, sv)
            v = v >> (len(sv) - len(su))
            ans += (len(sv) - len(su)) # 高さを揃えた
            sv = bin(v)[2:]
            #print(su, sv)
            while u != v:
                ans += 2
                u >>= 1
                v >>= 1
            ans += 1 # ぐるっと
            ret.append(ans)
        #print(ret)
        return ret


st = Solution()

print(st.cycleLengthQueries(n = 3, queries = [[5,3],[4,7],[2,3]])==[4,5,3])
print(st.cycleLengthQueries(n = 2, queries = [[1,2]])==[2])

