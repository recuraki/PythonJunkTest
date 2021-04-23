# https://drken1215.hatenablog.com/entry/2019/09/16/014600
# O(N)であるので、全ての部分文字列文s[0～n:n]について計算してもO(N^2)

# aaabaaaab
# 921034210

class zAlgorithm():
    def __init__(self, s):
        self.sdat = list(map(lambda x: ord(x), s))
        self.sl = len(s)
        self.res = [0] * self.sl
        self.res[0] = self.sl
        i, j = 1, 0
        while i < self.sl:
            while (i+j) < self.sl:
                if self.sdat[j] != self.sdat[i+j]:
                    break
                j += 1
            self.res[i] = j
            if(j == 0):
                i += 1
                continue
            k = 1
            while (i+k) < self.sl and (k+self.res[k] < j):
                self.res[i+k] = self.res[k]
                k += 1
            i += k
            j -= k

"""
文字列の約数のような文字列とそのカウントを返す。
ababab = ab,3
aaaaaa = a,6 aa,3 aaa,2
abc = None
つまり、x,cnt で x * cntするとその文字列になる
必ず、元の文字列,1は入る。
実行時間: O(N + NlogN)
課題: 毎回文字列をコピーするので定数倍のNが少し重い
"""
def stringDivisors(s):
    z = zAlgorithm(s)
    res = dict()
    slen = len(s)
    for i in range(len(s) // 2): # longest divisor is //2 (exclude itself)
        curTryLen = i+1
        if slen % curTryLen != 0: # target-len * n = original len ?
            continue
        target = s[:i+1] # make divisors
        t = s[:i+1] + ":" + s # for z-algo
        z = zAlgorithm(t)
        can = True
        for j in range(0, slen, curTryLen): # check each unit of orig
            if z.res[len(target) + 1 + j] >= len(target):
                continue
            can = False
            break
        if can:
            res[target] = slen // curTryLen
    res[s] = 1 # add itself
    return res
def testsd():
    s = "ababab"
    print(stringDivisors(s)) # {'ab': 3, 'ababab': 1}
    s = "abababab"
    print(stringDivisors(s)) # {'ab': 4, 'abab': 2, 'abababab': 1}
    s = "aaaaaa"
    print(stringDivisors(s)) # {'a': 6, 'aa': 3, 'aaa': 2, 'aaaaaa': 1}
    s = "abcabc"
    print(stringDivisors(s)) # {'abc': 2, 'abcabc': 1}
    s = "abc"
    print(stringDivisors(s)) # {'abc': 1}
    s = "ababc"
    print(stringDivisors(s)) # {'ababc': 1}

def cf1473b():
    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)
    q = int(input())
    for _ in range(q):
        s, t = input(), input()
        sdiv = stringDivisors(s)
        tdiv = stringDivisors(t)
        reslen = 0
        resval = ""
        for k in list(sdiv.keys()):
            if k not in tdiv:
                continue
            tmps = str(k) * lcm(sdiv[k], tdiv[k])
            if len(tmps) > reslen:
                reslen = len(tmps)
                resval = tmps
        if resval == "":
            print(-1)
        else:
            print(resval)

def abc141_e():
    n = int(input())
    s = input()
    res = 0
    for i in range(n - 1):
        t = s[i:]
        z = zAlgorithm(t)
        for j in range(len(z.res)):
            if j < z.res[j]:
                continue
            res = max(res, z.res[j])
    print(res)

def test():
    s = "abaaaabab"
    s = "abaaaabab"
    s = "abaaababa"
    s = "aaabaaaab"
    z = zAlgorithm(s)
    print(z.res)





#abc141_e()
#testsd()
#cf1473b()
test()