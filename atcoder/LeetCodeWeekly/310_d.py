from typing import List, Tuple
from pprint import pprint



class LIS():
    res = []
    INF = 1 << 61
    longestlen = -1
    def __init__(self):
        pass
    def load(self, l, k):
        self.longestlen = -1
        from bisect import bisect_left
        self.res = [self.INF] * (len(l) + 1)
        for x in l:
            ind = bisect_left(self.res, x)
            print(x, ind)
            if ind == 0:
                self.res[ind] = x
                self.longestlen = max(self.longestlen, ind + 1)
                continue
            if (x - self.res[ind-1]) <= k:
                self.res[ind] = x
                self.longestlen = max(self.longestlen, ind + 1)
                continue
        print(self.res)
        self.res = self.res[:self.longestlen]

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        lis = LIS()
        lis.load(nums, k)
        return lis.longestlen

st = Solution()

#print(st.lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3)==5)
#print(st.lengthOfLIS(nums = [7,4,5,1,8,12,4,7], k = 5)==4)
#print(st.lengthOfLIS(nums = [1,5], k = 1)==1)
print(st.lengthOfLIS(nums = [1,3,3,4], k = 1)==2)


