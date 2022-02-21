from typing import List, Tuple
from pprint import pprint


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0: return []
        x = num //3
        return [x-1, x, x+1]


st = Solution()

print(st.sumOfThree(num = 0))
print(st.sumOfThree(num = 33))
print(st.sumOfThree(num = 4))

