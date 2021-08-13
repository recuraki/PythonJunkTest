import sys

def solve():
    n, k = map(int, input().split())
    p = 0
    cnt = 0

    for i in range(1, n):
        cnt += 1
        x = p ^ i
        print(x, flush=True)
        res = int(input())
        if res == 1:
            return
        if res == -1:
            sys.exit(123)
        p = i

    i = 0
    x = p ^ i
    print(x, flush=True)
    res = int(input())
    if res == 1:
        return
    if res == -1:
        sys.exit(123)
    sys.exit(100)

qall = int(input())
for q in range(qall):
    solve()
sys.exit(0)
