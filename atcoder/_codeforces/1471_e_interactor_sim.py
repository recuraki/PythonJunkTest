import sys, math
n,k,ans = 10,8,6
l = [k] * n
qcount = -1
print(n, k)
while qcount < 1000:
    print("turn{0}: before {1}".format(qcount, l), file=sys.stderr)
    qcount += 1
    s = input()
    if s[0] == "!":
        if int(s.split(" ")[1]) == ans: print("OK!"), sys.exit(0)
        else: print("NG!"), sys.exit(20)
    print(l[int(s.split()[1]) - 1])
    ll = [0] * n
    for ii in range(n):
        lsend = math.floor(l[ii] / 2)
        rsend = math.ceil(l[ii] / 2)
        lnum = ii - 1 if ii!=0 else n-1
        rnum = ii + 1 if ii!=(n-1) else 0
        if (ans-1) == ii:
            ll[rnum] += l[ii]
            continue
        ll[lnum] += lsend
        ll[rnum] += rsend
    l = ll
print("GAMEOVER!")
sys.exit(10)


