import sys
import math
#n, k = 2*10**4, 1000
#ans = 701
#n,k,ans= 10000, 10, 700
#n,k,ans=100000,100,80116
#n,k,ans = 4,2,1
n,k,ans = 7, 4, 4
n,k,ans = 10,8,6
l = [k] * n
qcount = -1
print(n, k)
while qcount < 1000:
    qcount += 1
    s = input()
    #print("recv raw:", s, file=sys.stderr)
    if s[0] == "!":
        if int(s.split(" ")[1]) == ans: print("OK!"), sys.exit(0)
        else: print("NG!"), sys.exit(20)
    qnum = int(s.split()[1])
    if ans == qnum:
        print(k)
        continue
    if n & 1 == 0 and qnum == ( ((ans-1) + (n//2)) % n + 1): # boarder
        print(k)
        continue
    if n & 1 == 1 and qnum == ( ((ans-1) + (n//2)) % n + 1) and qcount >= (n//2) and qcount%2 == 0: # boarder
        print(k)
        continue
    if n & 1 == 1 and qnum == ( ((ans-1) + (n//2) + 1) % n + 1) and qcount >= (n//2) and qcount%2 == 0: # boarder
        print(k)
        continue
    if ans-qcount <= qnum < ans:
        print(k-1)
        continue
    if ans < qnum <= ans+qcount:
        print(k+1)
        continue
    if (ans + qcount) > n:
        if qnum <= (ans + qcount - n + 1):
            print(k + 1)
            continue
    print(k)
    continue
print("GAMEOVER!")
sys.exit(10)


