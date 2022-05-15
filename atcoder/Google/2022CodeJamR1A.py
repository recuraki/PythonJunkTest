
import itertools

def countstrs(s):
    return [(k, len(list(g))) for k, g in itertools.groupby(s)]


def solve(qnum):
    s = input()
    ans = ""
    l = countstrs(s)
    for i in range(len(l) - 1):
        if ord(l[i][0]) < ord(l[i+1][0]):
            ans += l[i][0] * (l[i][1] * 2)
        else:
            ans += l[i][0] * l[i][1]
    ans += l[-1][0] * l[-1][1]



    print("Case #{}:".format(qnum), ans)


q = int(input())
for i in range(q): solve(i+1)
