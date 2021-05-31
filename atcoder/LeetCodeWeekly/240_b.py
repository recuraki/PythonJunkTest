from typing import List, Tuple
from pprint import pprint


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        from bisect import bisect_left, bisect_right
        for i in range(len(nums1)):
            nums1[i] = -nums1[i]
        for i in range(len(nums2)):
            nums2[i] = -nums2[i]
        #print(nums1)
        #print(nums2)
        finalres = 0
        for i in range(len(nums1)):
            x = nums1[i]
            ind = bisect_right(nums2, x)
            #print(i, x, ind)
            resind = ind - 1
            if resind >= i:
                resres = resind - i
                #print(">", i, finalres, resres)
                finalres = max(finalres,resres)
                #print("fff", finalres)
        #print(finalres)
        return finalres




st = Solution()

print(st.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))
print(st.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))
print(st.maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]))
print(st.maxDistance(nums1 = [5,4], nums2 = [3,2]))

