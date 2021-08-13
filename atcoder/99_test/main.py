
n, m = map(int, input().split())
g = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(m):
    print(len(g[i]))
