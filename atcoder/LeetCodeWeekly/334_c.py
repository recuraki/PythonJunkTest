from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        from bisect import bisect_left, bisect_right
        n = len(nums)
        marked = [False] * n
        nums.sort()
        nums = list(nums)
        lind = 0
        for rind in range(n//2, n):
            canpick = nums[rind] // 2 # この数のvalまでは取れる(include)
            if marked[rind]: continue
            while True:
                if lind >= n: break # over
                if marked[lind]:
                    lind += 1
                    continue
                lval = nums[lind]
                if lval > canpick: break # もう取れない
                marked[lind] = True
                marked[rind] = True
                #print("marked", lind, rind, "val=" ,nums[lind], nums[rind])
                lind += 1
                break
        ans = 0
        for i in range(n):
            if marked[i]: ans += 1
        print(ans)
        return ans







st = Solution()

print(st.maxNumOfMarkedIndices(nums = [3,5,2,4])==2)
print(st.maxNumOfMarkedIndices( nums = [9,2,5,4])==4)
print(st.maxNumOfMarkedIndices( nums = [7,6,8])==0)
print(st.maxNumOfMarkedIndices( nums = [7])==0)
print(st.maxNumOfMarkedIndices( nums = [2,2,2])==0)



print(st.maxNumOfMarkedIndices(nums=[57,40,57,51,90,51,68,100,24,39,11,85,2,22,67,29,74,82,10,96,14,35,25,76,26,54,29,44,63,49,73,50,95,89,43,62,24,88,88,36,6,16,14,2,42,42,60,25,4,58,23,22,27,26,3,79,64,20,92])
      == 58)
print(st.maxNumOfMarkedIndices( nums =[42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40])==26)
print()