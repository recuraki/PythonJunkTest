import sys

def query(l, r):
    #if l == r:
    #    ans(l)
    #    sys.exit(0)
    print("?",l,r,flush=True)
    ret = int(input())
    #print("s send l,r,mid",l,r ,"=>", ret, file=sys.stderr)
    return ret

def ans(answer):
    print("!",answer, flush=True)
    sys.exit(0)

n, t = map(int, input().split())
k = int(input())
l, r = 1, n

if n == 1:
    ans(1)

while l < r:
    mid = (l + r) // 2
    last = mid
    lastl = l
    lastr = r
    res = query(1, mid)
    findk = mid - res # 5 - 3 = 2
    if findk < k: # more Right
        l = mid + 0
    else:
        r = mid - 0
    if lastl ==l and lastr == r:
        break
    #print("new lr = ",l,r , file=sys.stderr)


#print("enddd",l,r , file=sys.stderr)
#print("enddd",l,r ,lastl, lastr, file=sys.stderr)


res = query(1, last)
findk = mid - res  # 5 - 3 = 2
if findk == k:
    ans(last)
ans(last+1)
sys.exit(0)
