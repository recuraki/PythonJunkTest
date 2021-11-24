import sys
import math
input = sys.stdin.readline
from pprint import pprint
INF = 1 << 63

def do():
    f = lambda a, b: (a+b)%10
    g = lambda a, b: (a*b)%10

    mod = 998244353
    dp = [0] * 10
    n = int(input())
    dat = list(map(int, input().split()))
    # 初期構築
    dp[f(dat[0], dat[1])] += 1
    dp[g(dat[0], dat[1])] += 1
    # 2から実行します
    for i in range(2, n):
        newdp = [0] * 10
        # 新しい方をbとします
        b = dat[i]
        # 古いものはaです
        for a in range(10):
            x = f(a, b)
            newdp[x] += dp[a]
            newdp[x] %= mod
            x = g(a, b)
            newdp[x] += dp[a]
            newdp[x] %= mod
        dp = newdp

    for x in dp:
        print(x% mod)
do()

