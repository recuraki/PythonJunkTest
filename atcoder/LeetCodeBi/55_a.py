from typing import List, Tuple
from pprint import pprint


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums)):
            dat = []
            for j in range(len(nums)):
                if i == j:
                    continue
                dat.append(nums[j])
            #print(dat)

            can = True
            for j in range(len(dat) - 1):
                if dat[j] < dat[j+1]:
                    continue
                can = False
            if can:
                return True
        return False






st = Solution()

print(st.canBeIncreasing(nums = [1,2,10,5,7]))
print(st.canBeIncreasing(nums = [2,3,1,2]))
print(st.canBeIncreasing(nums = [1,1,1]))
print(st.canBeIncreasing(nums = [1,2,3]))
print(st.canBeIncreasing(nums = [1,1]))
