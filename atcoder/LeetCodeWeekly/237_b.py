from typing import List, Tuple
from pprint import pprint


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        for x in costs:
            if x <= coins:
                coins -= x
                cnt += 1
        return cnt


st = Solution()

print(st.maxIceCream(costs = [1,3,2,4,1], coins = 7))
print(st.maxIceCream(costs = [10,6,8,7,7,8], coins = 5))
print(st.maxIceCream(costs = [1,6,3,1,2,5], coins = 20))

