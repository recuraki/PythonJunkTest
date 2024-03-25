
from typing import List, Tuple
from pprint import pprint

from fractions import Fraction
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if (sum(dist) / speed) > hoursBefore:
            return -1
        hoursBefore = Fraction(hoursBefore)
        hoursBefore -= Fraction(dist[-1] , speed)
        dist = dist[:-1]
        print(dist)
        print(hoursBefore)
        import math
        for i in range(len(dist)):
            dist[i] = Fraction(dist[i], speed)
        res = 0
        while True:
            # check
            total = 0
            for i in range(len(dist)):
                total += math.ceil(dist[i])
            print(total ,"<", hoursBefore)
            if total <= hoursBefore:
                break
            mm = 0
            mmind = -1
            for i in range(len(dist)-1):
                before = math.ceil(dist[i]) + dist[i+1]
                after = dist[i] + dist[i+1]
                if (before - after) > mm:
                    mm = (before-after)
                    mmind = i
            print(dist)
            dist[mmind] = dist[mmind] + dist[mmind+1]
            del dist[mmind+1]
            res += 1

        print(">>> res", res)
        return res



st = Solution()

print(st.minSkips( dist = [1,3,2], speed = 4, hoursBefore = 2))
print(st.minSkips(dist = [7,3,5,5], speed = 2, hoursBefore = 10))
print(st.minSkips(dist = [7,3,5,5], speed = 1, hoursBefore = 10))

