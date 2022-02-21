from typing import List, Tuple
from pprint import pprint

###################################
class Solution:
    def defdef(self):
        passfrom typing import List, Tuple
from pprint import pprint


class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        s = list(s)
        s.sort()
        print(s)
        from random import shuffle
        ans = 100000
        for i in range(10000):
            shuffle(s)
            x = int(s[0] + s[1]) + int(s[2] + s[3])
            ans = min(ans,x)
        return ans



st = Solution()

print(st.minimumSum(2932))
print(st.minimumSum(2009))

###################################


st = Solution()

print(st.defdef())
