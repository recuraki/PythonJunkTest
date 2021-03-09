import sys
def query(l, r):
    if l == r:
        ans(l)
        sys.exit(0)
    print("?",l,r,flush=True)
    ret = int(input())
    print("s send l,r,mid",l,r ,"=>", ret, file=sys.stderr)
    return ret
def ans(answer):
    print("!",answer, flush=True)
n = int(input())
l, r = 1, n
v2ind = query(1, n)
ind = -1

if n == 2:
    l,r = 1,2
    last = query(min(l, r), max(l, r))
    if last == l:
        ans(r)
    else:
        ans(l)
    sys.exit(0)

# step1: Left?
if v2ind != 1:
    ind = query(1, v2ind)
if ind == v2ind and v2ind != 1: # Yes! We have!
    l, r = 1, v2ind-1
    if l == r:
        ans(l)
        sys.exit(0)
    while l < r:
        if r - l == 1:
            last = query(min(l, r), max(l, r))
            if last == l:
                ans(r)
            else:
                ans(l)
            sys.exit(0)
        mid = (l + r) // 2
        ind = query(mid, v2ind)
        print("!!!!!!!!!! l,r,mid",l,r,mid,ind, file=sys.stderr)
        if ind != v2ind:
            print("pat1", file=sys.stderr)
            r = mid - 1
        else:
            print("pat2", file=sys.stderr)
            l = mid
    last = query(min(l,r), max(l, r))
    if last == l:
        ans(r)
    else:
        ans(l)
    sys.exit(0)

print("---------------",file=sys.stderr)
# step1: Left
l, r = v2ind+1, n
if l == r:
    ans(l)
    sys.exit(0)

print("!??", l, r, file=sys.stderr)
while l < r:
    if r - l == 1:
        last = query(min(l, r), max(l, r))
        if last == l:
            ans(r)
        else:
            ans(l)
        sys.exit(0)

    mid = (l + r) // 2
    ind = query(v2ind, mid)
    print("!!!!!!!!!! l,r,mid", l, r, mid, ind, file=sys.stderr)
    if ind != v2ind:
        print("pat3", file=sys.stderr)
        l = mid + 1
    else:
        print("pat4", file=sys.stderr)
        r = mid
last = query(min(l, r), max(l, r))
if last == l:
    ans(r)
else:
    ans(l)
