import sys
input = sys.stdin.readline
from pprint import pprint

import math
INF = 1 << 63
turn = 0
def do():
    turn = 0
    n = int(input())


    res = [None] * n

    for i in range(n):
        if res[i] is not None: continue

        candidate = []
        while True:
            print("?", i + 1, flush=True)
            val = int(input()) - 1
            turn += 1
            if val in candidate: break
            candidate.append(val)
        if len(candidate) == 1:
            res[candidate[0]] = candidate[0]
            continue
        for j in range(len(candidate)):
            val = candidate[j]
            res[val] = candidate[ (j + turn) % (len(candidate)) ]
    print("! " + " ".join(list(map(lambda x: str(x + 1), res))), flush=True)


# n questions
q = int(input())
for _ in range(q):
    do()
