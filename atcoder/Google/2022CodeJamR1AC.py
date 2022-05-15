
import itertools


"""
w ウェイト
e エクササイズ
"""

def solve(qnum, e = None, w = None, dat = None):
    if e is None:
        e, w = map(int, input().split())
        for i in range(e): # 読み込み
            dat = list(map(int, input().split()))

    exs = []
    for l in dat: exs.append(l)
    ans = 1 << 61
    # 前処理
    buf = []
    for i in range(w):
        cur = 1 << 61
        curma = -1
        for j in range(e):
            cur = min(cur, dat[j][i])
            curma = max(curma, dat[j][i])
        buf.append( (cur, curma, i) )
    buf.sort()
    print(buf)
    dat = []
    for l in exs:
        ent = []
        for ll in buf:
            ent.append(l[ll[2]])
        dat.append(ent)
    dat.sort()
    print(dat)



    print("Case #{}:".format(qnum), ans)



#q = int(input())
#for i in range(q): solve(i+1)
solve(1, 3, 1, [[1], [2], [1]])

solve(2, 2,3 , [[1,2,1], [2,1,2]])
solve(3, 3,3 , [[3,1,1], [3,3,3], [2,3,3]])
