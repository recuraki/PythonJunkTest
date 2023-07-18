from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for k, v in nums1: d[k] += v
        for k, v in nums2: d[k] += v
        ans = []
        for k in d.keys(): ans.append( [k, d[k]] )
        ans.sort()
        ans = list(ans)
        return ans


st = Solution()

print(st.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]])== [[1,6],[2,3],[3,2],[4,6]])
print(st.mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]])==[[1,3],[2,4],[3,6],[4,3],[5,5]])

