from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = []
        for _ in range(numOnes): ans.append(1)
        for _ in range(numZeros): ans.append(0)
        for _ in range(numNegOnes): ans.append(-1)
        ans.sort(reverse=True)
        res = 0
        for x in ans[:k]: res += x
        return res



st = Solution()

print(st.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2)==2)
print(st.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4)==3)

