
from typing import List, Tuple
from pprint import pprint

import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        prev = -1
        new = None
        while prev != new:
            ans = self.replaceNonCoprimesCo(nums)
            prev = new
            new = len(ans)
        return ans
    def replaceNonCoprimesCo(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        cur = nums[0]
        def f():
            while len(ans) >= 2:
                isDo = False
                if math.gcd(ans[-1], ans[-2]) != 1:
                    isDo = True
                    x = lcm(ans[-1], ans[-2])
                    ans.pop()
                    ans.pop()
                    ans.append(x)
                if isDo is False: break

        for i in range(1, n):
            x = nums[i]
            if math.gcd(cur, x) == 1:
                ans.append(cur)
                f()
                cur = x
                continue
            # else
            cur = lcm(cur, x)
        ans.append(cur)
        f()
        return ans


st = Solution()


print(st.replaceNonCoprimes(nums = [6,4,3,2,7,6,2]))
print(st.replaceNonCoprimes(nums = [2,2,1,1,3,3,3]))
print(st.replaceNonCoprimes(nums = [287,41,49,287,899,23,23,20677,5,825]) == [2009,20677,825])
print(st.replaceNonCoprimes(nums= [2009, 899, 20677, 825]))
print(lcm(899,20677))
print(st.replaceNonCoprimes(nums=[8303,361,8303,361,437,361,8303,8303,8303,6859,19,19,361,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,1271,31,961,31,7,2009,7,2009,2009,49,7,7,8897,1519,31,1519,217]) == [157757,70121,1930649])
print(st.replaceNonCoprimes(nums=[8303,361,8303,361,437,361,8303,8303,8303,6859,19,19,361,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,70121,1271,31,961,31,7,2009,7,2009,2009,49,7,7,8897,1519,31,1519,217]) )
print(st.replaceNonCoprimes([157757, 70121, 39401, 62279]))