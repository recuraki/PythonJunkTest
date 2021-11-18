

def f1(n, k, a, b, c):
    for i in range(n):
        a[i] -= 1
        b[i] -= 1
        c[i] -= 1

    cur = list(range(n))

    route = [[i] for i in range(n)]
    for i in range(k):
        for j in range(n):
            if i%3 == 0:
                cur[j] = a[cur[j]]
            if i%3 == 1:
                cur[j] = b[cur[j]]
            if i%3 == 2:
                cur[j] = c[cur[j]]
            route[j].append(cur[j])

    for i in range(n):
        for j in range(k+1):
            route[i][j] += 1

    res = []
    for i in range(n):
        res.append(route[i][-1])
    return res



def f2(n, k, a, b, c):
    cur = list(range(n))
    ok = k

    for i in range(n):
        a[i] -= 1
        b[i] -= 1
        c[i] -= 1

    #ベースサインの3回移動を作る
    portala = deepcopy(cur)
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

    if ok%3 >=1 :
        for i in range(n): cur[i] = a[cur[i]]
    if ok%3 >=2 :
        for i in range(n): cur[i] = b[cur[i]]

    res = []
    for i in range(n):
        res.append(cur[i] + 1)
    return res



"""
n, k = 200000,1234
oa = [1,2,4,3,5,6]
ob = [2,1,5,4,3,6]
oc = [1,2,4,3,5,6]
from random import randint
for t in range(1):
    oa = []
    ob = []
    oc = []
    for i in range(n):
        oa.append(randint(1, n))
        ob.append(randint(1, n))
        oc.append(randint(1, n))
    for loop in range(5,6):
        n, k = n, loop
        from copy import deepcopy
        res = f2(n, k, deepcopy(oa), deepcopy(ob), deepcopy(oc))
        #print(res)
        tres = f1(n, k, deepcopy(oa), deepcopy(ob), deepcopy(oc))
        # 典型シミュレーション
        if res == tres:
            print("ok")
        else:
            print("ng", loop)
            print("a",oa)
            print("b",ob)
            print("c",oc)
            print(res)
            print(tres)

"""


n, k = 10,1234
oa = [1,1,1,1,1,1,1,1,1,1]
ob = [1,2,3,4,5,6,7,8,9,10]
oc = [1,2,3,4,5,6,7,8,9,10]
from random import randint
for t in range(1):
    oa = []
    ob = []
    oc = []
    for i in range(n):
        oa.append(randint(1, n))
        ob.append(randint(1, n))
        oc.append(randint(1, n))
    for loop in range(0,100):
        n, k = n, loop
        from copy import deepcopy
        res = f2(n, k, deepcopy(oa), deepcopy(ob), deepcopy(oc))
        #print(res)
        tres = f1(n, k, deepcopy(oa), deepcopy(ob), deepcopy(oc))
        # 典型シミュレーション
        if res == tres:
            print(loop, "ok", res)
        else:
            print("ng", loop)
            print("a",oa)
            print("b",ob)
            print("c",oc)
            print(res)
            print(tres)
