import sys
l, r = 1, 10**6
while l != r:
    mid = (l+r+1)//2
    print("new mid:", mid, file=sys.stderr)
    print(mid, flush=True)
    s = input()
    if s[0] == "<": r = mid - 1
    else: l = mid
print("!", l, flush=True)
sys.exit(100)