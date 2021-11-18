def solve():
    from copy import deepcopy
    n, k = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))
    b = list(map(lambda x: int(x) - 1, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))

    cur = list(range(n))
    ok = k

    #ベースサインの3回移動を作る
    portala = list(range(n))
    for i in range(n):
        portala[i] = a[portala[i]]  # 1回
        portala[i] = b[portala[i]]  # 2回
        portala[i] = c[portala[i]]  # 3回

    res = []
    for i in range(n):
        res.append(portala[i] + 1)

    k = k - k % 3

    # まず、最初にportalAだけを使ったダブリングをする
    cnt = 1
    while k > 0:

        curnum = k % 3**(cnt+1) // 3**cnt
        #print("loop", cnt, curnum, k ,  3**(cnt+1) , 3**cnt, portala)

        newportal = deepcopy(portala)

        if curnum == 1:
            for i in range(n):
                cur[i] = newportal[cur[i]]

        for i in range(n):
            newportal[i] = portala[newportal[i]]
        if curnum == 2:
            for i in range(n):
                cur[i] = newportal[cur[i]]

        for i in range(n):
            newportal[i] = portala[newportal[i]]

        portala = newportal
        k -= (3**cnt) * curnum
        cnt += 1

    if ok%3 >= 1:
        for i in range(n): cur[i] = a[cur[i]]
    if ok%3 >= 2:
        for i in range(n): cur[i] = b[cur[i]]

    print(" ".join(list(map(lambda x:(str(x+1)), cur))))


solve()