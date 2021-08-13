from typing import List, Tuple
import re


class Solution:
    def maxNiceDivisors(self, n: int) -> int:
        if n == 1:
            return 1
        num2 = n // 2
        num3 = n % 2
        #print(num2, num3)
        if num3 == 1:
            num2 -= 1
        #print(num2, num3)
        can3 = num2 // 3
        num3 += can3 * 2
        num2 %= 3
        #print(num2, num3)
        m = 10**9 + 7
        return ((pow(2,num2, m) * pow(3,num3,m) )% m)


st = Solution()
print(st.maxNiceDivisors(5))
print(st.maxNiceDivisors(8))
#print(st.maxNiceDivisors(2000))
