from typing import List, Tuple
from pprint import pprint


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        dat = [0] * (60000)
        for x in nums:
            dat[x] += 1
        cnt = 0
        res = 0
        for i in range(55000, -1, -1):
            if dat[i] == 0:
                continue
            # なにか数字があるなら
            res += cnt # 全てをその数に落とす
            cnt += dat[i]
        return res




st = Solution()

print(st.reductionOperations(nums = [5,1,3]))
print(st.reductionOperations(nums = [1,1,1]))
print(st.reductionOperations(nums = [1,1,2,2,3]))
print(st.reductionOperations(nums = [100, 200]))
