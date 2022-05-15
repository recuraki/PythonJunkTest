
from typing import List, Tuple
from pprint import pprint


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        l = [None, None]
        i = 0 # こたえ
        j = 0 # ポインタ
        for x in nums:
            if i % 2 == 0:
                l.append(x)
                i += 1
                continue
            else:
                if x == l[-1]:
                    continue
                l.append(x)
                i += 1
                continue
        l = l[2:]
        if len(l)%2 != 0: l = l[:-1]
        return len(nums) - len(l)


st = Solution()

print(st.minDeletion(nums = [1,1,2,3,5])==1)
print(st.minDeletion(nums = [1,1,2,2,3,3])==2)

