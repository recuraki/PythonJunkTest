import math
from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts.sort(reverse=True)
            gifts[0] = math.sqrt(gifts[0]) // 1
        return sum(gifts)



st = Solution()

print(st.pickGifts(gifts = [25,64,9,4,100], k = 4)==29)
print(st.pickGifts(gifts = [1,1,1,1], k = 4)==4)

