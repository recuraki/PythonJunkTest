import sys

def query(a, b, c):
    print(a, b, c, flush=True)
    ret = int(input())
    #print("query",a,b,c,"=",ret, file=sys.stderr, flush=True)
    if ret == -1:
        raise
    return ret
def ans(l):
    print("ans:",l, file=sys.stderr, flush=True)
    print(" ".join(list(map(str, l))), flush=True)
    ret = int(input())
    if ret == 1:
        return True
    raise

def do(clist):
    print("do", clist, file=sys.stderr, flush=True)
    if len(clist) in [1]:
        return clist
    if len(clist) in [2]:
        return clist
    ll = clist[0]
    rr = clist[1]
    aa, bb, cc = [], [], []
    for x in clist[2:]:
        res = query(ll, rr, x)
        if res == x:
            bb.append(x)
        elif res == ll:
            aa.append(x)
        elif res == rr:
            cc.append(x)

    res = str(aa) + "_" + str([ll]) + "_" + str(bb) + "_" + str([rr]) + "_"  + str(cc)
    #print(">cut status", clist ,">", res, file=sys.stderr, flush=True)

    #print("  check aa", aa, file=sys.stderr, flush=True)
    if len(aa) > 1:
        aa = do(aa)
        res = query(aa[0], aa[-1], ll)
        assert res != ll
        if res == aa[0]:
            aa.reverse()

    #print("  check bb", bb, file=sys.stderr, flush=True)
    if len(bb) > 1:
        bb = do(bb)
        res = query(bb[0], bb[-1], rr)
        assert res != rr
        if res == bb[0]:
            bb.reverse()

    #print("  check cc", cc, file=sys.stderr, flush=True)
    if len(cc) > 1:
        cc = do(cc)
        res = query(cc[0], cc[-1], rr)
        assert res != rr
        if res == cc[-1]:
            cc.reverse()


    res = str(aa) + "_" + str([ll]) + "_" + str(bb) + "_" + str([rr]) + "_"  + str(cc)
    print(">do", clist ,">", res, file=sys.stderr, flush=True)
    return aa + [ll] + bb + [rr] + cc

t, n, q = map(int, input().split())
for testcase in range(1, t+1):
    print("case",testcase, file=sys.stderr, flush=True)
    l = do(list(range(1, n + 1)))
    ans(l)

