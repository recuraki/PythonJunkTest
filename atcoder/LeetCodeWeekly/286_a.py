
from typing import List, Tuple
from pprint import pprint


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set()
        ans2 = set()
        nums1s = set()
        nums2s = set()
        for x in nums1:
            if x not in nums2:
                ans1.add(x)
        for x in nums2:
            if x not in nums1:
                ans2.add(x)
        return [list(ans1), list(ans2)]


st = Solution()

print(st.findDifference(nums1 = [1,2,3], nums2 = [2,4,6])==[[1,3],[4,6]])
print(st.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2])==[[3],[]])

