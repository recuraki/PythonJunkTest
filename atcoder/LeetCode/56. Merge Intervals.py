from typing import List, Tuple
from pprint import pprint

###################################
# https://leetcode.com/problems/merge-intervals/

# (をクロージャカウント+1, )をクロージャカウント-1とする
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        ans = []
        for s,e in intervals:
            events.append( (s, +1) )
            events.append( (e, -1) )
        current = 0 # 今のクロージャのカウント
        events.sort(key=lambda x: (x[0], -x[1]))
        prev = 0 # prev value
        curRangeStart = 0 # 今のソート
        for t, a in events:
            current += a # クロージャの処理
            # 0 -> 1になるなら、外側の一番外側のクロージャ開始
            if prev == 0 and current == 1: curRangeStart = t
            # 1 -> 0になるなら、外側のクロージャが閉じた
            if prev == 1 and current == 0: ans.append([curRangeStart, t])
            prev = current
        return ans

###################################

st = Solution()

print(st.merge([[1,3],[2,6],[8,10],[15,18]]))
print(st.merge([[1,4],[4,5]]))


