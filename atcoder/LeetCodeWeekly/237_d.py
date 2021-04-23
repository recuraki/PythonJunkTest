from typing import List, Tuple
from pprint import pprint


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        a=b=0
        for x in arr1:
            a ^= x
        for y in arr2:
            b ^= y
        return a & b


st = Solution()

print(st.getXORSum(arr1 = [1,2,3], arr2 = [6,5]))
print(st.getXORSum(arr1 = [12], arr2 = [4]))


