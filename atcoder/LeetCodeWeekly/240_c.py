############################################
from collections import deque
from typing import Deque
from typing import List, Tuple
from pprint import pprint


class Rect:
    def __init__(self, height, pos):
        self.height = height
        self.pos = pos
def solve(h: [int]):
    # 拾い物 の　ヒストグラム最大化 ライブラリ
    stack: Deque[Rect] = deque()
    histogram = h + [0]
    max_area = 0

    # ここに累積和を足す
    import itertools
    def createSDAT(l):
        return list(itertools.accumulate(itertools.chain([0], l)))
    sdat = createSDAT(h)
    squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)

    for idx, height in enumerate(histogram):
        if not stack or stack[-1].height < height:
            stack.append(Rect(height=height, pos=idx))
        elif stack[-1].height > height:
            top = Rect(height=0, pos=0)
            while stack and stack[-1].height > height:
                top = stack.pop()
                # ここは通常、今の位置 - heightのposだが、ここを、その間のブロックの和にする
                #max_area = max(max_area, (idx - top.pos) * top.height)
                max_area = max(max_area, squery(top.pos, idx) * top.height)
            stack.append(Rect(height=height, pos=top.pos))
    return max_area
############################################
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = solve(nums) % (10**9+7)
        return (res)

st = Solution()

print(st.maxSumMinProduct(nums = [1,2,3,2]))
print(st.maxSumMinProduct(nums = [2,3,3,1,2]))
print(st.maxSumMinProduct(nums = [3,1,5,6,4,2]))

