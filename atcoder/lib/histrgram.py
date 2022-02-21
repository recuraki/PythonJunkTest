from collections import deque
from typing import Deque
############################################

# ヒストグラムの最大面積
# 拾い物コード
class Rect:
    def __init__(self, height, pos):
        self.height = height
        self.pos = pos
def solve(h: [int]):
    stack: Deque[Rect] = deque()
    histogram = h + [0] # これがポイント！最後に清算する (番兵的な考え方)
    max_area = 0
    for idx, height in enumerate(histogram):
        if not stack or stack[-1].height < height:
            stack.append(Rect(height=height, pos=idx))
        elif stack[-1].height > height:
            top = Rect(height=0, pos=0)
            while stack and stack[-1].height > height:
                top = stack.pop()
                max_area = max(max_area, (idx - top.pos) * top.height)
            stack.append(Rect(height=height, pos=top.pos))
    return max_area
############################################

h = [1,2,3,2,1]
print(solve(h = h))
