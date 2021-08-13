from typing import List, Tuple
from pprint import pprint


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        is1, is2, is3 = False, False, False
        for d in triplets:
            if d[0] > target[0]:
                continue
            if d[1] > target[1]:
                continue
            if d[2] > target[2]:
                continue
            if d[0] == target[0]:
                is1 = True
            if d[1] == target[1]:
                is2 = True
            if d[2] == target[2]:
                is3 = True
        if all([is1, is2, is3]):
            return True
        return False

st = Solution()

print(st.mergeTriplets(triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]))
print(st.mergeTriplets(triplets = [[1,3,4],[2,5,8]], target = [2,5,8]))
print(st.mergeTriplets(triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]))
print(st.mergeTriplets(triplets = [[3,4,5],[4,5,6]], target = [3,2,5]))

