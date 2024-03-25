from typing import List, Tuple
from pprint import pprint


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        event = []
        for l, r in intervals:
            event.append( (l, 0) )
            event.append( (r, 1) )
        cnt = 0
        ans = -1
        event.sort()
        for _, e in event:
            if e == 0:
                cnt += 1
            elif e == 1:
                cnt -= 1
            ans = max(ans, cnt)
        return ans


st = Solution()

print(st.minGroups(intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]])==3)
print(st.minGroups(intervals = [[1,3],[5,6],[8,10],[11,13]])==1)

