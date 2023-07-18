from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ans = 0
        event = []
        for x in nums:
            event.append( (x-k, 0) ) # 追加
            event.append( (x+k, 1) ) # 抜ける
        event.sort()
        cur = 0
        for t, ty in event:
            if ty == 0: cur += 1
            if ty == 1: cur -= 1
            ans = max(ans, cur)
        return ans



st = Solution()

print(st.maximumBeauty(nums = [4,6,1,2], k = 2)==3)
print(st.maximumBeauty(nums = [1,1,1,1], k = 10)==4)

