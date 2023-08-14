import random
n = random.randint(1,100)
print(n)
for _ in range(n):
    print(random.randint(0,100),random.randint(0,100))
q = random.randint(1,100)
print(q)
queries = []
for _ in range(q): queries.append(random.randint(1,100))
print(*queries)