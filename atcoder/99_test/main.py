def do():
    q = int(input())
    for _ in range(q):
        n = int(input())
        s = input()
        res = ""
        for i in range(n):
            res += s[2 * i]
        print(res)

do()
