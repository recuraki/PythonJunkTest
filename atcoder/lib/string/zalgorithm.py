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

def abc141_e():
    n = int(input())
    s = input()
    res = 0
    for i in range(n - 1):
        t = s[i:]
        z = zAlgorithm(t)
        #int(t, z.res)
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

abc141_e()
#test()

