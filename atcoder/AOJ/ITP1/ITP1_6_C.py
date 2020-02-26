wall = "#" * 20
n = int(input())
dat = []
for _ in range(12):
    dat.append([0] * 10)

for _ in range(n):
    b,f,r,v = map(int, input().split())
    dat[3 * (b - 1) + ( f-1)][r - 1] += v
for i in range(12):
    print(" ",end="")
    print(" ".join(map(str, dat[i])))
    if i % 3 == 2 and i!=11:
        print(wall)