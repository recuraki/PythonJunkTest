
import sys
from io import StringIO

# AOJ_GRL_4_B
# d,f を打刻する DFS
def call_grl_4_b():
    # eは1 origin
    numv, nume = map(int, input().split())

    # edgeの初期化 color, prev, stime, etime
    # color: W(未訪問), G(探索中), B(探索済み)
    # prev
    # stime = -1なら未訪問
    # etime
    e = [("W", None, -1, -1) for _ in range(nume + 1)]


    # 辺を張る
    v = [[] for _ in range(numv)]
    for _ in range(numv):
        s, t = map(int, input().split())
        v[s].append(t)

    import collections
    q = collections.deque([])
    time = 0

    for targetE in range(1, nume + 1):
        #
        if e[targetE][2] != -1:
            continue
        time = time + 1
        e[targetE][2] = time
        e[targetE][0] = "G"
        





def grl_4_b():
    stdout, stdin = sys.stdout, sys.stdin
    inp = """6 6
0 1
1 2
3 1
3 4
4 5
5 2"""
    sys.stdin = StringIO(inp)
    call_grl_4_b()
    sys.stdout, sys.stdin = stdout, stdin

grl_4_b()