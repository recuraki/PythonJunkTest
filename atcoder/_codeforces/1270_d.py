import sys
n, k = map(int, input().split())
buf = []
for i in range(1, k + 2):
    query = []
    for j in range(1, k + 2):
        if i != j:
            query.append(str(j))
    print("? " + " ".join(query), flush=True)
    sys.stdout.flush()
    a, b = map(int, input().split())
    buf.append(b)
print("! ", buf.count(max(buf)), flush=True)
sys.stdout.flush()
sys.exit(0)