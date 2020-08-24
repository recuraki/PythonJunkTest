def findWinner(L, B, H):
    def do(a,b,c):
        p = a
        c = a-1
        c += (b-1) * p
        p = (b-1) * p
        c += (c-1) * p
        return False if c % 2 == 0 else True

    dat = [L, B, H]
    dat.sort()
    a, b, c = dat

    x = 0
    x += c - 1
    x *= b
    x += b - 1
    x *= a
    x += a - 1
    print(a, b, c, "=:", x)
    v = False
    v = v or do(a,b,c)
    v = v or do(a,c,b)
    v = v or do(b,a,c)
    v = v or do(b,c,a)
    v = v or do(c,a,c)
    v = v or do(c,b,a)
    print("??", 1 if a%2==0 or b%2==0 or c%2==0   else 2)
    if x % 2 == 1:
        return 1
    else:
        return 2

print(findWinner(1,1,1))
print(findWinner(1,1,2))
print(findWinner(1,1,3))
print(findWinner(2,2,1))
print(findWinner(4,4,1))
print(findWinner(2,3,1))
print(findWinner(4,5,1))
print(findWinner(1,1,1))
