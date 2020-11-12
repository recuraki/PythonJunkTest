numv = int(input())
rootnode = 0
parentlist = [None] * numv
distlist = [-1] * numv
e = []
for i in range(numv):
    e.append([])
dt = []
for i in range(63):
    l = [-1] * numv
    dt.append(l)

# make edge
for i in range(numv):
    dat = list(map(int, input().split()))
    for j in dat[1:]:
        e[i].append(j)
        e[j].append(i)

# calc depth and parent node
from collections import deque
q = deque([])
q.append([rootnode, -1, 0])
while len(q) != 0:
    node, parent, d = q.popleft()
    parentlist[node] = parent
    distlist[node] = d
    for nextnode in e[node]:
        if parentlist[nextnode] is not None: # visited
            continue
        q.append([nextnode, node, d + 1])

# doubling calc
for i in range(numv):
    dt[0][i] = parentlist[i]
for i in range(1,63):
    for curnode in range(numv):
        p1 = dt[i-1][curnode]
        p2 = dt[i-1][p1] if p1 != -1 else -1
        dt[i][curnode] = p2

def ancestor(node, n):
    i = 0
    cur = node
    while n != 0:
        x = 2 ** i
        if (n & x) != 0: # this bit is 1
            n ^= x # this bit is off
            cur = dt[i][cur]
        i += 1
    return cur

def lca(nodeu, nodev):
    if nodeu == nodev:
        return nodeu
    tu = nodeu
    tv = nodev
    for k in range(60, -1, -1):
        mu = ancestor(tu, 2**k)
        mv = ancestor(tv, 2**k)
        if mu != mv:
            tu = mu
            tv = mv
    assert ancestor(tu, 1) == ancestor(tv, 1)
    return ancestor(tu, 1)

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    # u < v
    if distlist[u] > distlist[v]:
        u, v = v, u
    d = distlist[v] - distlist[u]
    v = ancestor(v, d)
    print(lca(u, v))

