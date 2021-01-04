# その場所を中心とする最長の左右に同じ文字数をカウントする
# "abaaababa"
#  121412321
# その文字を、なので例えば、"3"とは、ababaのこと
# 注意は「その文字を中心と」なので、偶数長の回文は見つけられない。
# abaaaabab
# 121221221
# この場合、
# _a_b_a_a_a_a_b_a_b
# 121412349432141311
# --------^--------x
# というようにダミーもじれつを挟む。
# O(N)
# http://snuke.hatenablog.com/entry/2014/12/02/235837
class manacher:
    def __init__(self, s):
        self.sdat = list(map(lambda x: ord(x), s))
        self.sl = len(s)
        self.res = [0] * self.sl

        i = j = 0
        while i < self.sl:
            while True:
                if (i-j) < 0 or (i+j) >= self.sl:
                    break
                if self.sdat[i-j] != self.sdat[i+j]:
                    break
                j += 1
            self.res[i] = j
            k = 1
            while (i - k) >= 0 and k+self.res[i - k] < j:
                self.res[i + k] = self.res[i - k]
                k += 1
            i += k
            j -= k

def test():
    s = "abaaababa"
    m = manacher(s)
    print(s)
    print(m.res)
    s = "abaaaabab"
    m = manacher(s) # cannot find aaaa
    print(m.res)
    s = "abaaaabab"
    s = "".join(["_" + x for x in s]) # _a_b_a_a_a_a_b_a_b
    print(s) # found _a_b_a_a_a_a_b_a_
    m = manacher(s)
    print(m.res)

test()