import sys
import itertools
import random
ll = list(range(1, 17))
ans, qcount = None, 0
ll = [13, 2, 10, 8, 3, 14, 7, 1, 5, 6, 11, 15, 4, 12, 9, 16]
ll = [16, 13, 2, 10, 8, 3, 14, 7, 1, 5, 6, 11, 15, 4, 12, 9]
ll=[6, 1, 12, 11, 15, 9, 16, 14, 3, 2, 13, 5, 7, 10, 4, 8]
ll=[6, 5, 14, 11, 3, 1, 8, 10, 16, 9, 4, 15, 2, 7, 12, 13]
random.shuffle(ll)
ll=[5,1,4,2,3]
#ll.reverse()

print(ll, file=sys.stderr)
maval = max(ll)
for i in range(len(ll)):
    if ll[i] == maval:
        ans = i + 1 # +1!

print(len(ll))
while qcount < 40:
    qcount += 1
    s = input().split()
    #print("recv raw:", s, file=sys.stderr)
    if s[0] == "!":
        if int(s[1]) == ans: print("OK!"), sys.exit(0)
        else: print("NG!"), sys.exit(20)
    l, r = int(s[1]), int(s[2])
    print("<<? q",l, r, file=sys.stderr)
    if l>=r or l < 1 or len(ll) < r:
        print("ERROR INPUT!")
        sys.exit(10)
    l -= 1
    r -= 1


    maval = max(ll[l: r+1])
    v2 = -1

    for i in range(l, r+1):
        if ll[i] == maval:
            continue
        v2 = max(v2, ll[i])
    for i in range(l, r+1):
        if ll[i] == v2:
            v2ind = i+1
    print("<<int",ll[l: r+1], file=sys.stderr)
    print("<<int",v2, v2ind, file=sys.stderr)
    print(v2ind)

print("GAMEOVER!")
sys.exit(10)


