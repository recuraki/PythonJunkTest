from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        for x in nums: cnt[x] += 1
        macnt = 0
        manum = None
        for k in cnt.keys():
            if cnt[k] > macnt:
                macnt = cnt[k]
                manum = k
        #print(macnt, manum)
        lexact = 0
        lother = 0
        rexact = macnt
        rother = len(nums) - macnt
        for i in range(len(nums)):
            x = nums[i]
            if x == manum:
                lexact += 1
                rexact -= 1
            else:
                lother += 1
                rother -= 1
            if rother < rexact and lother < lexact:
                return i
            #print(lexact, lother, rexact, rother)
        return -1




st = Solution()

print(st.minimumIndex(nums = [1,2,2,2])==2)
print(st.minimumIndex(nums = [2,1,3,1,1,1,7,1,2,1])==4)

