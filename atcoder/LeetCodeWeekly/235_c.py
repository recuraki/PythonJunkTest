from typing import List, Tuple
import re


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        m = 10**9 + 7
        canreduce = -1
        res = 0
        from copy import deepcopy
        from bisect import bisect_left
        l = list(set(nums1))
        #print(l)

        for i in range(len(nums1)):
            res += abs(nums1[i] - nums2[i])

        for i in range(len(nums1)):
            curdiff = abs(nums1[i] - nums2[i])
            curind = bisect_left(l, nums2[i])
            #print(i, nums1[i], nums2[i], curdiff, curind)
            if curind != 0:
                canval = l[curind - 1]
                candiff = abs(nums2[i] - canval)
                #print(" >", canval, candiff)
                if curdiff > candiff:
                    canreduce = max(canreduce, curdiff - candiff)
            if curind != len(l):
                canval = l[curind]
                candiff = abs(nums2[i] - canval)
                #(" >", canval, candiff)
                if curdiff > candiff:
                    canreduce = max(canreduce, curdiff - candiff)

        #print(canreduce)
        if canreduce == -1:
            return res % m
        else:
            return (res-canreduce) % m


st=Solution()
print(st.minAbsoluteSumDiff(nums1 = [1,7,5], nums2 = [2,3,5]))
print(st.minAbsoluteSumDiff(nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]))
print(st.minAbsoluteSumDiff(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]))


