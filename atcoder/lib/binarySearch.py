
# https://atcoder.jp/contests/abc146/tasks/abc146_c
# 条件を満たせるなるべく大きな数を探したい
def abc146_c():
    a, b, x = map(int, input().split())
    pl = lambda x: a * x + b * len(str(x))
    l = 0
    h = 1000000000
    while l <= h:
        mid = (l + h) // 2
        if pl(mid) <= x: # 買うことができるなら
            l = mid + 1 # 買えるのでそれ以上の数
        else: # 買えないなら
            h = mid - 1 # 買えないのでそれ以下の数をトライ
    print(h if ( pl(h) <= x ) else l)


#やりたいこと「一番近い数字を探す」
from bisect import bisect_left, bisect_right
def mindiffsearch(x):
    l = [1, 5, 10, 100, 200]
    ll = len(l)
    indl = bisect_left(l, x)
    if indl == 0:
        return abs(x-l[0])
    if indl == ll:
        return abs(x-l[-1])
    else:
        return min(abs(x-l[indl]), abs(x - l[indl-1]))
print(mindiffsearch(-1))