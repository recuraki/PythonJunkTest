from typing import List, Tuple
import re


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        l = list(range(n))
        for loop in range(1000):
            if loop != 0:
                can = True
                for i in range(n):
                    if i != l[i]:
                        can = False
                        break
                if can:
                    break

            newl = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    newl[i] = l[i//2]
                else:
                    newl[i] = l[n//2 + (i-1)//2]
            l = newl
        return loop



st = Solution()
print(st.reinitializePermutation(2))
print(st.reinitializePermutation(4))
print(st.reinitializePermutation(6))
print(st.reinitializePermutation(8))
print(st.reinitializePermutation(1000))
