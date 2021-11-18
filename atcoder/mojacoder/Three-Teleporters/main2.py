def solve():
    from copy import deepcopy
    n, k = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))
    b = list(map(lambda x: int(x) - 1, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))


    cur = list(range(n))

    route = [[i] for i in range(n)]
    for i in range(k):
        for j in range(n):
            if i % 3 == 0:
                cur[j] = a[cur[j]]
            if i % 3 == 1:
                cur[j] = b[cur[j]]
            if i % 3 == 2:
                cur[j] = c[cur[j]]
            route[j].append(cur[j])

    for i in range(n):
        for j in range(k + 1):
            route[i][j] += 1

    res = []
    for i in range(n):
        res.append(route[i][-1])
    print(" ".join(list(map(lambda x:(str(x+1)), cur))))

solve()