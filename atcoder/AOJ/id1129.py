while True:
    n, r = map(int, input().split())
    if n == r == 0: break
    dat = [tuple(map(int, input().split())) for _ in range(r)]
    ans = 1 # 最後の一番上のカード を1とする
    for i in range(len(dat)): # 逆順に見ていく
        p, c = dat[i] # 上からp枚目から, c枚を持ってくる つまり、
        if ans <= c: ans += (p-1)
        elif ans < p+c: ans -= c
    print(n - ans + 1) # 本当は一番の上のカードがnなので変換
