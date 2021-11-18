n, k = 200000, 10**11
oa = list(range(0, n))
print(n, k)
oa = oa[1:] + [oa[0]]
print(" ".join(list(map(lambda x: (str(x + 1)), oa))))

oa = oa[1:] + [oa[0]]
print(" ".join(list(map(lambda x: (str(x + 1)), oa))))
oa = oa[1:] + [oa[0]]
print(" ".join(list(map(lambda x: (str(x + 1)), oa))))


import sys
sys.exit(10)
from random import randint, shuffle
n, k = randint(200000-1,200000), randint(10**11, 10**12-1)
oa = []
ob = []
oc = []
for i in range(n):
    oa.append(randint(0, n-1))
    ob.append(randint(0, n-1))
    oc.append(randint(0, n-1))

oa = list(range(0, n-0))
ob = list(range(0, n-0))
oc = list(range(0, n-0))
shuffle(oa)
shuffle(ob)
shuffle(oc)

print(n, k)
print(" ".join(list(map(lambda x: (str(x + 1)), oa))))
print(" ".join(list(map(lambda x: (str(x + 1)), ob))))
print(" ".join(list(map(lambda x: (str(x + 1)), oc))))