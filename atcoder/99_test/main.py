def do(n, k, offset):
    #print(n,k,offset)
    cur = dat[0] + offset
    for i in range(1, n):
        #print(n,k,(dat[i]*100 / cur), dat[i], cur, k/100)
        if (dat[i] / cur) > (k/100):
            return False
        cur += dat[i]
    return True

qq = int(input())
for q in range(qq):
    n, k = map(int, input().split())
    dat = map(int, input().split())
    dat = list(dat)
    l = 0
    h = 10000000000000
    while l <= h:
        mid = (l + h) // 2
        if do(n, k, mid):  # 買うことができるなら
            h = mid - 1  # 買えないのでそれ以下の数をトライ
        else:  # 買えないなら
            l = mid + 1  # 買えるのでそれ以上の数
    if h == -1:
        print(0)
    else:
        print(h if (do(n,k,h)) else l)


