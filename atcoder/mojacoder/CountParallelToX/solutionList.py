from bisect import bisect_left, bisect_right
n = int(input())
xs = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
xs.sort()
ans = []
q = int(input())
queries = map(int, input().split())
for a in queries: ans.append(bisect_right(xs, a) - bisect_left(xs, a))
print(*ans)