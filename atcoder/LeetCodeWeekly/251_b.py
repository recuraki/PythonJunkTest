from typing import List, Tuple
from pprint import pprint


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        res = ""
        first = False
        did = False
        for x in num:
            a = int(x)
            b = change[a]
            #print(a, b, did, first)

            if did:
                res += x
                continue

            if first is False:
                if int(a) >= int(b):
                    res += str(a)
                else:
                    first = True
                    res += str(b)
            else: # first is True
                if int(a) > int(b):
                    did = True
                    res += str(a)
                else:
                    res += str(b)

        #print(res)
        return res


st = Solution()

print(st.maximumNumber(num = "132", change = [9,8,5,0,3,6,4,2,6,8]))
print(st.maximumNumber(num = "021", change = [9,4,3,5,7,2,1,9,0,6]))
print(st.maximumNumber(num = "5", change = [1,4,7,5,3,2,5,6,9,4]))
print(st.maximumNumber("334111", [0,9,2,3,3,2,5,5,5,5]) == "334999")
