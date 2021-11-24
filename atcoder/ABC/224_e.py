import sys

input = sys.stdin.readline
from pprint import pprint

import math

INF = 1 << 63


def do():
    m = int(input())
    g = [[] for _ in range(9)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    dat = list(map(lambda x: int(x) - 1, input().split()))
    maze = [8] * 9
    for i in range(8):
        maze[dat[i]] = i
    aki = maze.index(8)

    def h(l):
        ans = 0
        for i in range(8, -1, -1):
            ans <<= 4
            ans += l[i]
        return ans

    targetans = h([0, 1, 2, 3, 4, 5, 6, 7, 8])
    ha = h(maze)
    if ha == targetans:
        print(0)
        return
    # print(bin(targetans))

    from collections import deque
    q = deque()
    res = 2 ** 31
    q.append((ha, aki, 0))  # map, akiの位置, Round
    known = set()

    from copy import deepcopy
    # DFS?
    while len(q) > 0:
        curha, aki, round = q.popleft()
        known.add(curha)
        if round > 100: continue
        # 空きのつながっているノードを検出

        for candidatenode in g[aki]:
            nextmaze = deepcopy(maze)  # 次のノード
            # その場所からakiに移すので、
            akinum = 0b1000
            cannum = (curha >> (4 * candidatenode)) & 0b1111

            nextha = curha
            nextha &= 2 ** (4 * 10) - 1 ^ (0b1111 << (4 * candidatenode))
            nextha &= 2 ** (4 * 10) - 1 ^ (0b1111 << (4 * aki))
            nextha |= (akinum << (4 * candidatenode))
            nextha |= (cannum << (4 * aki))

            if nextha in known: continue
            known.add(ha)
            if nextha == targetans:
                res = min(res, round + 1)

            q.append((nextha, candidatenode, round + 1))

    if res == 2 ** 31: res = -1
    print(res)


do()