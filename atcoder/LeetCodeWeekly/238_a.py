from typing import List, Tuple
from pprint import pprint


class Solution:
    def base10int(self, value, base):
        if (int(value / base)):
            return self.base10int(int(value / base), base) + str(value % base)
        return str(value % base)
    def sumBase(self, n: int, k: int) -> int:
        x = self.base10int(n, k)
        res = 0
        x = int(x)
        while x != 0:
            res += (x % 10)
            x //= 10
        return res

st = Solution()

print(st.sumBase(n = 34, k = 6))
print(st.sumBase(n = 10, k = 10))

