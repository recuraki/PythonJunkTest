import sys
input = sys.stdin.readline

n = int(input())
visited = [False] * (400000 + 10)
count = [0] * (400000 + 10)
dat = []
for i in range(n):
    a, b = map(int, input().split())
    count[a] += 1
    count[b] += 1
    dat.append((a,b))
buf = []
for i in range(n):
    a,b = dat[i]
    if count[a] > count[b]:
        buf.append((b,a))
    else:
        buf.append((a,b))
buf.sort(key=lambda x:count[x[0]])
res = 0
for i in range(n):
    a,b = dat[i]
    if visited[a] is False:
        visited[a] = True
        res += 1
        continue
    if visited[b] is False:
        visited[b] = True
        res += 1
        continue
print(res)