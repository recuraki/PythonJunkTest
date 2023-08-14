from collections import defaultdict
n = int(input())
cnt = defaultdict(int)
for _ in range(n):
    x, y = map(int, input().split())
    cnt[x] += 1
ans = []
q = int(input())
queries = map(int, input().split())
for a in queries: ans.append(cnt[a])
print(*ans)