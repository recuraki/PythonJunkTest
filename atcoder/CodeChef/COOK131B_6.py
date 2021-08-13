import sys

def do():
    def query(n): # 0 origin is ok
        print("?", n + 1, flush=True)
        ret = input()
        if ret == "W": return False
        if ret == "B": return True
        assert False

    def ans():
        print("!", flush=True)
        for s in g:
            res = ["0"] * n
            for i in s: res[i] = "1"
            print("".join(res), flush=True)

    n = int(input())

    color = [None] * n
    g = [set() for _ in range(n)]

    color[0] = query(0)
    for i in range(1, n):
        color[i] = query(i)
        for j in range(i):
            jcolor = query(j)
            if jcolor is not color[j]:

                g[j].add(i)
                g[i].add(j)
            for nextnode in g[j]:

                color[nextnode] = not color[nextnode]
    #print(g)
    ans()

do()