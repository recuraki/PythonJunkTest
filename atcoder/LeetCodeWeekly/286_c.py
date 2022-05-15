
from typing import List, Tuple
from pprint import pprint


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        import math
        needlen = math.ceil(intLength/2)
        #print(needlen)
        base = 10**(needlen-1) # 10
        dontreach = 10**(needlen) # 100
        #print(base,dontreach)
        ans = []
        for que in queries:
            x = base + (que - 1)
            if not(base <= x < dontreach):
                ans.append(-1)
                continue
            a = str(x)
            b = str(x)[::-1]
            if intLength % 2 == 1:
                b = b[1:]
            ans.append( int(str(a) + str(b)) )
        #print(ans)
        return ans



st = Solution()

print(st.kthPalindrome(queries = [1,2,3,4,5,90], intLength = 3)== [101,111,121,131,141,999])
print(st.kthPalindrome(queries = [1,2,3,4,5,91], intLength = 3)== [101,111,121,131,141,-1])
print(st.kthPalindrome(queries = [1,2,3,4,5,6,7,8,9,10], intLength = 1)== [1,2,3,4,5,6,7,8,9,-1])
print(st.kthPalindrome(queries = [1,2,3,4,5,6,7,8,9,10,100], intLength = 2)== [11,22,33,44,55,66,77,88,99,-1,-1])
print(st.kthPalindrome(queries = [2,4,6], intLength = 4)==[1111,1331,1551])

