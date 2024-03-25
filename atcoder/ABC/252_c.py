n = int(input())
dat = [list(map(int, list(input()))) for _ in range(n)]
ans = 1 << 61
# cnt[i][j]: index=iにjという数が何個あるか？
cnt = [[0] * 10 for _ in range(10)]
for reel in dat: # 各リールを読み込み
    for i in range(10): # index 0-9をみて
        cnt[i][reel[i]] += 1 # cntを足す
for choice in range(10): # 揃えたい数
    maxindtime = -1
    for ind in range(10):
        maxindtime = max(maxindtime, 10*(cnt[ind][choice]-1)+ind)
    ans = min(ans, maxindtime)
print(ans)