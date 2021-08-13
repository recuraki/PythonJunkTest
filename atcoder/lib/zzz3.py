a, b, x = map(int, input().split())

func = lambda arg: a * arg + b * len(str(arg)) <= x

# [ok, ng) for max value
# (ng, ok] for min value
# CATION: ok is result  (NOT mid)
ok = 0
ng = 10**9 + 1
while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2;
    if(func(mid)) :ok = mid;
    else : ng = mid;
print(ok)