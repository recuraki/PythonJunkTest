import sys

l = [(300000,12314)]
print(len(l))
for n, ans in l:
    cnt = 0
    print(n, ans)
    print("---------------------", ans, file=sys.stderr)

    while cnt < n:
        print("curans", ans, file=sys.stderr)
        x = int(input())
        ans ^= x
        print("   ans", ans, file=sys.stderr)
        if ans == 0:
            print(1)
            break
        print(0)
    if cnt <= n:
        pass
    else:
        print("!!!!!!!!!!!!")
        sys.exit(-100)
print("okok!")
sys.exit(0)
