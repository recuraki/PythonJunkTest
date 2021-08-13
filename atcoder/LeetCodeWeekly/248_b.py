from typing import List, Tuple
from pprint import pprint


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        dat = []
        for i in range(len(dist)):
            dat.append(dist[i] / speed[i])
        dat.sort()
        print(dat)
        time = 0
        res = 0
        for teki in dat:
            if teki <= time:
                break
            res += 1
            time += 1
        return res


st = Solution()

print(st.eliminateMaximum(dist = [1,3,4], speed = [1,1,1]))
print(st.eliminateMaximum(dist = [1,1,2,3], speed = [1,1,1,1]))
print(st.eliminateMaximum(dist = [3,2,4], speed = [5,3,2]))
