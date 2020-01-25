
# https://docs.python.org/ja/3/library/bisect.html#searching-sorted-lists
def index(a, x):
    'indexが存在することを前提にxという値のindexを得る。存在しない場合raise'
    from bisect import bisect_left
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    from bisect import bisect_left
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    from bisect import bisect_right
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    from bisect import bisect_right
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    from bisect import bisect_left
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError