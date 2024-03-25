from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x: x[k], reverse= True)
        return (score)


st = Solution()

print(st.sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2)==[[7,5,11,2],[10,6,9,1],[4,8,3,15]])
print(st.sortTheStudents( score = [[3,4],[5,6]], k = 0)== [[5,6],[3,4]])

