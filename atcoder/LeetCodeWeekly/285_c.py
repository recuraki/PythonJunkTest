
from typing import List, Tuple
from pprint import pprint


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        ans = -1
        anspat = []
        from copy import deepcopy
        for pat in range(2**12):
            need = 0
            bob = [0] * 12
            score = 0
            for i in range(12):
                if ((pat >> i) & 1) == 1: #スコアiがほしい
                    need += aliceArrows[i] + 1
                    bob[i] += aliceArrows[i] + 1
                    score += i
            if need > numArrows: continue # 無理
            if score > ans:
                ans = score
                bob[0] += numArrows - need
                anspat = deepcopy(bob)
        #print(ans, anspat)
        return anspat



st = Solution()

print(st.maximumBobPoints(numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0])==[0,0,0,0,1,1,0,0,1,2,3,1])
print(st.maximumBobPoints(numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2])==[0,0,0,0,0,0,0,0,1,1,1,0])

