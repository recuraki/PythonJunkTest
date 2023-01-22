from typing import List, Tuple
from pprint import pprint


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dat = []
        for i in range(len(names)):
            dat.append( (heights[i], names[i]) )
        dat.sort(reverse=True)
        ans = []
        for _, x in dat: ans.append(x)
        #print(dat)
        return ans
        #print(ans)


st = Solution()

print(st.sortPeople( names = ["Mary","John","Emma"], heights = [180,165,170])==["Mary","Emma","John"])
print(st.sortPeople( names = ["Alice","Bob","Bob"], heights = [155,185,150])== ["Bob","Alice","Bob"])

