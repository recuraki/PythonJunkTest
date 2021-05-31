from typing import List, Tuple
from pprint import pprint


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        from fractions import Fraction
        import math
        def do(spped):
            if spped == 0:
                return 10**18
            total = 0
            for x in dist:
                y = math.ceil(x / spped)
                total += y
            total -= y
            total += x / spped
            return total

        INF = 10 ** 18
        l = 0
        h = INF
        while l <= h:
            mid = (l + h) // 2
            if do(mid) > hour:  # 買うことができるなら
                l = mid + 1  # 買えるのでそれ以上の数
            else:  # 買えないなら
                h = mid - 1  # 買えないのでそれ以下の数をトライ
        res = h if (do(h) <= hour) else l
        if res >= INF:
            return -1
        return res


st = Solution()

print(st.minSpeedOnTime(dist = [1,3,2], hour = 6))
print(st.minSpeedOnTime(dist = [1,3,2], hour = 2.7))
print(st.minSpeedOnTime(dist = [1,3,2], hour = 1.9))
