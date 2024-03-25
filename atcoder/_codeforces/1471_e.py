"""
rm /tmp/fifo && mkfifo /tmp/fifo && (python3 1471_e.py < /tmp/fifo)1>&2  | python3 1471_e_interactor.py > /tmp/fifo1>&2
"""
import sys
n, k = map(int, input().split())
def do():
    for i in range(502):
        print("? 1")
        sys.stdout.flush()
        res = int(input())
        if res == k: continue
        if res < k: # is left
            res =  i
            res %= n
            print("!", res + 1)
            sys.stdout.flush()
            return
        if res > k:
            res = -i
            res %= n
            print("!", res + 1)
            sys.stdout.flush()
            return
    if n < 500:
        print("?", (0 + 1) % n + 1)
        resr = int(input())
        print("?", (0 - 1) % n + 1)
        resl = int(input())
        if (resl < k < resr):
            print("!",  1)
            return
        else:
            print("!", n//2 + 1)
            return
    for i in range(400):
        cur = 1 + 500*i
        print("?", cur)
        sys.stdout.flush()
        res = int(input())
        if res == k: continue # cannot judge
        if res < k: # more right
            l = cur
            r = cur + 510+500
            break
        if res > k: # more left
            l = cur - 501
            r = cur
            break
    # start Nibutan
    while l <= r:
        mid = (l + r) // 2
        print("{0} {1}=> mid={2}".format(l, r, mid), file=sys.stderr)
        print("?", mid % n + 1)
        sys.stdout.flush()
        res = int(input())
        if res == k:
            print("?", (mid+1) % n + 1)
            resr = int(input())
            print("?", (mid-1) % n + 1)
            resl = int(input())
            if not (resl < k < resr):
                l -= 501*2
                continue
            print("!", mid % n + 1)
            sys.stdout.flush()
            return
        if res < k: # more right
            l = mid + 1
            continue
        if res > k: # more left
            r = mid - 1
            continue
    print("?", l)
    sys.stdout.flush()
    res = int(input())
    if res == k:
        print("!", l)
        sys.stdout.flush()
        return
    print("?", r)
    res = int(input())
    if res == k:
        print("!", r)
        sys.stdout.flush()
        return
    print("cannot!!!")


sys.stdout.flush()

do()
