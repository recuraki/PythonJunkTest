from typing import List, Tuple
from pprint import pprint


###################################
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        from bisect import bisect_right
        event = []
        for p, b in items:
            event.append( (p, 0, b) )
        for p in queries:
            event.append( (p, 1, 0) )
        event.sort()
        ansdict = dict()
        val = 0
        for p, query, b in event:
            if query == 1:
                ansdict[p] = val
                continue
            # update
            val = max(val, b)
        ans = []
        for x in queries: ans.append(ansdict[x])
        return ans






###################################


st = Solution()

print(st.maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))
print(st.maximumBeauty(items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]))
print(st.maximumBeauty(items = [[10,1000]], queries = [5]))


"""
クエリ以下で買える最大の美しさ
"""