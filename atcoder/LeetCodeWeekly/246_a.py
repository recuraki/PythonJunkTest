from typing import List, Tuple
from pprint import pprint


class Solution:
    def largestOddNumber(self, num: str) -> str:
        lastodd = -1
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                lastodd = i
        if lastodd == -1:
            return ""
        return num[:lastodd+1]




st = Solution()

print(st.largestOddNumber(num = "52"))
print(st.largestOddNumber(num = "4206"))
print(st.largestOddNumber(num = "35427"))



