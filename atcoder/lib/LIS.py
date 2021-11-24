
class LIS():
    res = []
    INF = 1 << 61
    longestlen = -1
    def __init__(self):
        pass
    def load(self, l):
        self.longestlen = -1
        from bisect import bisect_left
        self.res = [self.INF] * (len(l) + 1)
        for x in l:
            ind = bisect_left(self.res, x)
            self.res[ind] = x
            self.longestlen = max(self.longestlen, ind + 1)
        self.res = self.res[:self.longestlen]
    def load_sameok(self, l):
        self.longestlen = -1
        from bisect import bisect_left, bisect_right
        self.res = [self.INF] * (len(l) + 1)
        for x in l:
            ind = bisect_right(self.res, x)
            self.res[ind] = x
            self.longestlen = max(self.longestlen, ind + 1)
        self.res = self.res[:self.longestlen]

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D
def dpl_1_d():
    l = []
    n = int(input())
    for x in range(n): l.append(int(input()))
    st = LIS()
    st.load(l)
    print(st.longestlen)

def t1():
    l = [1, 3, 5,2, 2, 2, 2, 4, 6]
    st = LIS()
    st.load(l)
    # 4 [1, 2, 4, 6]
    print(st.longestlen, st.res)
    st.load_sameok(l)
    # 7 [1, 2, 2, 2, 2, 4, 6]
    print(st.longestlen, st.res)


#dpl_1_d()
t1()