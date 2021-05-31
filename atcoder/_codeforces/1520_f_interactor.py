l = 3
k = 1

num0 = 1
res = [0] * num0
res.extend([1]* (l-num0))
#print(res)
import random
import sys
random.shuffle(res)
#print(res)
print(l, 1)
print(k)
print(res, file=sys.stderr)
work = k
for i in range(l):
    if res[i] == 0:
        work -= 1
    if work == 0:
        ans = i+1
        break
qcount = 0
print("ans", ans , file=sys.stderr)
while qcount < 40:
    qcount += 1
    s = input().split()
    if s[0] == "!":
        if int(s[1]) == ans: print("OK!"), sys.exit(0)
        else: print("NG!"), sys.exit(20)

    l, r = int(s[1]), int(s[2])
    print("<<? q",l, r, file=sys.stderr)
    l -= 1
    r -= 1
    print(sum(res[l:r+1]))


print("GAMEOVER!")
sys.exit(10)


