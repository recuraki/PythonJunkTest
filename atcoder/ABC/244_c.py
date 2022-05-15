
def do():
    n = int(input())
    canuse = set()
    for i in range(1, 2*n + 2):
        canuse.add(i)
    while True:
        x = canuse.pop()
        print(x, flush=True)
        x = int(input())
        if x == 0: return
        canuse.remove(x)

# print("?",l,r,flush=True)

do()