n = int(input())
dat = list(map(int, input().split()))
total = 3 ** n
countzero = 0
countodd = []

for i in range(n):
    if dat[i] % 2 == 0:
        countodd.append(2)
    else:
        countodd.append(1)
xxx = 1
for i in range(n):
    xxx *= countodd[i]

total -= xxx
print(total)