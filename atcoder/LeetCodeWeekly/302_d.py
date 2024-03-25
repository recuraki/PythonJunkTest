from typing import List, Tuple
from pprint import pprint

###################################
# Paste the template of question
import math
def gcdList(l):
    x = 0
    for i in range(len(l)):
        x = math.gcd(x, l[i])
    return x
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        ans = -1
        #print(sorted(nums))
        numsDivide = list(set(numsDivide))
        numsDivide.sort()
        gval = gcdList(numsDivide)
        mival = min(numsDivide)
        #print("gv", gval)
        #print("mival", mival)
        nums.sort()
        #print(numsDivide)
        #print("--")
        for x in set(nums):
            l = map(lambda y: y % x, numsDivide)
            #print(x, list(l))
        for i in range(len(nums)):
            if nums[i] == gval:
                return i
            if nums[i] > gval:
                break
            if gval % nums[i] == 0:
                return i
        return -1





st = Solution()

print(st.minOperations(nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15])==2)
print(st.minOperations(nums = [4,3,6], numsDivide = [8,2,6,10])==-1)
print(st.minOperations([3,2,6,2,35,5,35,2,5,8,7,3,4], [105,70,70,175,105,105,105]) == 6)
