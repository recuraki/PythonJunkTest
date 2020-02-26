
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

