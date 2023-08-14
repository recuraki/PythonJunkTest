# python3 makeCasePythonKiller.py > testcases/in/pythondictkiller.txt
n = 200000
mask = (1<<17) - 1 # 0xffff
fill = int((1<<15)*1.3+1) # 43599
arr = [mask+2]*2
x = 6 # magic number
for i in range(1,fill):
    arr += [x]+[x]
    x = (x * 5 + 1) & mask
arr += [1]*(n-len(arr))
# output points
print(len(arr)) # N
for i in range(len(arr)): print(arr[i], i) # x, y
# output queries
print(n)
queries = []
for _ in range(n): queries.append(1)
print(*queries)