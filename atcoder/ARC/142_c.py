import sys

def query(u, v):
    print("?",u, v,flush=True)
    ret = int(input())
    if ret == -1: assert False
    return ret

def ans(answer):
    print("!",answer, flush=True)
    sys.exit(0)

n = int(input())

dist1 = [None] * (n+1)
dist2 = [None] * (n+1)

# 偶数計算用
from collections import defaultdict
fromd1 = defaultdict(set)

# 各点までの距離を計算する
for i in range(3, n+1):
    dist1[i] = query(1, i)
for i in range(3, n+1):
    dist2[i] = query(2, i)
samedist = 1 << 60

for i in range(3, n+1):
    # もし、間に奇数の点がある場合はこれ
    if dist1[i] == dist2[i]:
        samedist = min(samedist, dist1[i])
if samedist == 1<<60:
    # この場合は偶数点の可能性が残っている
    candidate = 1 << 60
    for i in range(3, n+1):
        fromd1[dist1[i]].add(dist2[i])
    for i in range(3, n+1):
        a, b = dist1[i], dist2[i]
        if a in fromd1[b]:
            candidate = min(candidate, a+b)
    if candidate == 1 << 60:
        ans(1)
    else:
        ans(candidate)
else:
    ans(samedist * 2)
sys.exit(0)
