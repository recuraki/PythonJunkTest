def main():
    import sys
    read = sys.stdin.read
    numv, *indata = map(int, read().split())
    offset = 0
    LCALIM = 18 # max height < 2**18

    rootnode = 0
    parentlist = [None] * numv
    distlist = [-1] * numv
    e = [[] for _ in range(numv)]
    dt = []
    for i in range(LCALIM):
        l = [-1] * numv
        dt.append(l)

    # make edge
    for i in range(numv):
        k = indata[offset]
        offset += 1
        for j in indata[offset:offset + k]:
            e[i].append(j)
            e[j].append(i)
        offset += k

    # calc depth and parent node
    from collections import deque
    q = deque([])
    q.append( (rootnode, -1, 0) )
    while len(q) != 0:
        node, parent, d = q.popleft()
        parentlist[node] = parent
        distlist[node] = d
        for nextnode in e[node]:
            if parentlist[nextnode] is not None: continue # parent
            q.append( (nextnode, node, d + 1) )

    # doubling calc
    for i in range(numv):
        dt[0][i] = parentlist[i]
    for i in range(1,LCALIM):
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
        if nodeu == nodev: return nodeu
        tu = nodeu
        tv = nodev
        for k in range(LCALIM-1, -1, -1):
            mu = ancestor(tu, 2**k)
            mv = ancestor(tv, 2**k)
            if mu != mv:
                tu = mu
                tv = mv

        #assert ancestor(tu, 1) == ancestor(tv, 1)
        return ancestor(tu, 1)

    q = indata[offset]
    offset += 1
    for _ in range(q):
        u, v = indata[offset:offset + 2]
        offset += 2
        # u < v
        if distlist[u] > distlist[v]: u, v = v, u
        d = distlist[v] - distlist[u]
        v = ancestor(v, d)
        print(lca(u, v))

main()