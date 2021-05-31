from random import randint
import time
num = 5000
indatsmall = [randint(1, 10) for _ in range(num)]
indatlarge = [randint(10**6, 10**7) for _ in range(num)]
indatsmall2 = [randint(1, 10) for _ in range(num)]
indatlarge2 = [randint(10**6, 10**7) for _ in range(num)]

print(num)
print(" ".join(list(map(str, indatlarge))))
print(" ".join(list(map(str, indatlarge2))))