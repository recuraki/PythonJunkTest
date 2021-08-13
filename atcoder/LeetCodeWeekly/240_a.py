from typing import List, Tuple
from pprint import pprint


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dat = [0] * 3000
        for s, t in logs:
            for i in range(s, t):
                dat[i] += 1
        mind = -1
        mval = -1
        for i in range(3000):
            if mval < dat[i]:
                mval = dat[i]
                mind = i
        return mind


st = Solution()

print(st.maximumPopulation(logs = [[1993,1999],[2000,2010]]))
print(st.maximumPopulation(logs = [[1950,1961],[1960,1971],[1970,1981]]))
