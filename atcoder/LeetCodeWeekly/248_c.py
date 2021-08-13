from typing import List, Tuple
from pprint import pprint


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        res = 1
        res *= pow(5, n//2, mod)
        res *= pow(4, n//2, mod)
        if n % 2 == 1:
            res *= 5
        return res % mod







st = Solution()

print(st.countGoodNumbers(1))
print(st.countGoodNumbers(4))
print(st.countGoodNumbers(50))
print(st.countGoodNumbers(806166225460393))
