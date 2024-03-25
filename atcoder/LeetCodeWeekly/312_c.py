from typing import List, Tuple
from pprint import pprint


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        isInc = []
        isDes = []
        n = len(nums)
        p = nums[0]
        for i in range(n):
            x = nums[i]
            isInc.append(True if p >= x else False)
            isDes.append(True if p <= x else False)
            p = x
        #print(isInc)
        #print(isDes)
        lnum = 0 # Trueの数(L)
        rnum = 0 # Trueの数(R)
        ans = []
        if n <= (2*k): return []
        for i in range(k-1):
            if isInc[k - i - 1]: lnum += 1
            if isDes[k + i + 1 + 1]: rnum += 1
        #print(lnum, rnum)
        if lnum == rnum == (k-1): ans.append(k)
        for ind in range(n - (2*k) - 1):
            i = ind + k + 1
            if isInc[i - k]: lnum -= 1
            if isInc[i - 1]: lnum += 1
            if isDes[i + 1]: rnum -= 1
            if isDes[i + k]: rnum += 1
            if lnum == rnum == (k-1): ans.append(i)
            #print(i, lnum, rnum)
        #print(ans)
        return ans




st = Solution()

print(st.goodIndices(nums = [2,1,1,1,3,4,1], k = 2)==[2,3])
print(st.goodIndices(nums = [2,1,1,2], k = 2)==[])
print(st.goodIndices(nums = [2,1,1], k = 2)==[])
print(st.goodIndices(nums = [2,1], k = 2)==[])
print(st.goodIndices(nums = [2], k = 2)==[])
print(st.goodIndices(nums = [1], k = 1)==[])
print(st.goodIndices(nums = [1,2], k = 1)==[])
print(st.goodIndices(nums = [1,2,3], k = 1)==[1])
print(st.goodIndices([478184,863008,716977,921182,182844,350527,541165,881224], 1)==[1,2,3,4,5,6])



