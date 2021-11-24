n = 100
dat = []
import random
for _ in range(n):
    dat.append(random.randint(0, 100))
print(n)
print(" ".join(list(map(str, dat))))
