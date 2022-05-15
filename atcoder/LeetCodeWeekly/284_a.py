from typing import List, Tuple
from pprint import pprint


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            can = False
            for j in range(-k, +k+1):
                ind = i + j
                if not(0 <= ind < n): continue
                if nums[ind] == key:
                    can = True
                    break
            if can: ans.append(i)
        return ans




st = Solution()

print(st.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))
print(st.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))

