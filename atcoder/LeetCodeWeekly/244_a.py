from typing import List, Tuple
from pprint import pprint


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def makeRot90(mat: List[List[int]]):
            n = len(mat)
            res = [[0] * n for _ in range(n)]
            for h in range(n):
                for w in range(n):
                    res[w][n-1-h] = mat[h][w]
            return res
        if mat == target:
            return True
        res = makeRot90(mat)
        if res == target:
            return True
        res = makeRot90(res)
        if res == target:
            return True
        res = makeRot90(res)
        if res == target:
            return True
        return False


st = Solution()

print(st.findRotation(mat = [[0,1],[1,0]], target = [[1,0],[0,1]]))
print(st.findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]]))
print(st.findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]))
