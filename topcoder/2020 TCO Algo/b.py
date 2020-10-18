cache = dict()
def score(seg, turn, offset):
    ls = len(seg)
    maxval = 0

    if turn == 0:
        if len(seg) == 0:
            return 0
        if len(seg) == 1:
            return seg[0]
        if len(seg) == 2:
            return max(seg)
        s = map(str, seg)
        s = ",".join(s)

        index = 1000*offset + ls
        if index in cache:
            return cache[index]

        for i in range(ls):
            maxval = max(maxval, seg[i] + score(seg[:i], 1, offset + i) + score(seg[i+1:], 1, offset + i))
        cache[s] = maxval
        return maxval

    elif turn == 1:
        if len(seg) == 0:
            return 0
        if len(seg) == 1:
            return 0
        if len(seg) == 2:
            return min(seg)
        return (sum(seg) - score(seg, 0, offset))


print(score([1,2,3,4,5]*100, 0, 0))
