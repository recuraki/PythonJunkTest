from typing import List, Tuple, Optional, Set
from pprint import pprint
from collections import deque, defaultdict


mod = 10**9 + 7
import math
sqs = []
for i in range(2, 32): sqs.append(i**2)
class Solution:

    def squareFreeSubsets(self, nums: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for x in nums: cnt[x] += 1
        candidate = [2,3,5,6,7,10,11,13,14,15,17,19,21,22,23,26,27,29,30]
        for pat in range(1, 1<<len(candidate)): # bit全探索
            cur = 1
            num = 1
            for i in range(len(candidate)):
                if (pat >> i) & 1 == 1:
                    cur *= candidate[i]
                    num *= cnt[candidate[i]]
                    num %= mod
            can = True
            for sq in sqs:
                if cur % sq == 0: can = False
            if can is False: continue
            ans += num
            ans %= mod
        c1 = nums.count(1)
        ans *= pow(2, c1, mod)
        ans += pow(2, c1, mod) - 1
        print(ans)
        return ans





st = Solution()

#print(st.squareFreeSubsets(nums = [3,4,4,5])==3)
#print(st.squareFreeSubsets(nums = [1])==1)
#print(st.squareFreeSubsets([11,2,19,7,9,27])== 15)
print(st.squareFreeSubsets([1,2,6,15,7,19,6,29,28,24,21,25,25,18,9,6,20,21,8,24,14,19,24,28,30,27,13,21,1,23,13,29,24,29,18,7])== 9215)
