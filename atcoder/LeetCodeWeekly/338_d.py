from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:


st = Solution()

print(st.collectTheCoins(coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]])==2)
print(st.collectTheCoins(coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]])==2)

