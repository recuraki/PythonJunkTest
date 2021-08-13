print(1)
import random
buf = []
for i in range(10**5):
    buf.append(random.randint(- 10**9, 10**9))
print(" ".join(list(map(str, buf))))
