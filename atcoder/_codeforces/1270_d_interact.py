import sys
import random
#l = [2,0,1,9,3,4]
#m = 3
#k = 4
#4 3 3
#2 0 1 9 3 4
n, k, m = map(int, input().split())
l = list(map(int, input().split()))
print("server: n,k,m,l",n,k,m,l,file=sys.stderr)
print(n,k)
l = list(enumerate(l))
while True:
    s = list(input().split())
    if s[0] == "!":
        if m == int(s[1]): print("OK", file=sys.stderr), sys.exit(0)
        else: print("NG", file=sys.stderr), sys.exit(-1)
    elif s[0] == "?":
        dat = map(int, s[1:])
        buf = []
        for x in dat: buf.append(l[x - 1])
        buf.sort(key=lambda x: x[1])
        print(buf[m-1][0]+1, buf[m-1][1])