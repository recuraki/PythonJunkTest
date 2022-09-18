# Mersenne 2^61
# 2^61 - 1
# Original C++: https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
# Verify: https://atcoder.jp/contests/abc141/submissions/me
"""
rollingHash61
init(s) O(N)でハッシュを取る
calc hash [l, r)  r = OPEN
"""
class rollingHash61():
    MOD = (1<<61) - 1
    BASE = 20200213
    MASK30 = (1 << 30) - 1
    MASK31 = (1 << 31) - 1
    hashTable = []
    pow = []
    slen = -1
    sdat = []

    def __init__(self, s: str):
        self.sdat = list(map(lambda x: ord(x), s))
        self.slen = len(s)
        self.hashTable = [0] * (self.slen + 1)
        self.pow = [1] * (self.slen + 1)
        for i in range(self.slen):
            self.hashTable[i + 1] = self.multi(self.hashTable[i], self.BASE)
            self.hashTable[i + 1] += self.xorshift(self.sdat[i] + 1)
            self.pow[i+1] = self.multi(self.pow[i], self.BASE)
            self.hashTable[i + 1] = (self.hashTable[i + 1] - self.MOD) if (self.hashTable[i + 1] >= self.MOD) else self.hashTable[i + 1]

    def hash(self, l, r):
        # calc hash [l, r)  r = OPEN
        res = self.MOD + self.hashTable[r] - self.multi(self.hashTable[l], self.pow[r - l])
        return res if (res < self.MOD) else (res - self.MOD)

    def mod(self, x):
        res = (x >> 61) + (x & self.MOD)
        return res - self.MOD if res >= self.MOD else res

    def multi(self, x, y):
        xu, xd = x >> 31, x & self.MASK31
        yu, yd = y >> 31, y & self.MASK31
        m = xd * yu + xu * yd
        mu = m >> 30
        md = m & self.MASK30
        return self.mod(xu * yu * 2 + mu + (md << 31) + xd * yd)

    def xorshift(self, x):
        return x ^ (x << 13) ^ (x >> 17) ^ (x << 5)

def libtest():
    s = "abcdabcd"
    rh = rollingHash61(s)
    print(rh.sdat)   # DEBUG
    print(rh.hashTable) # DEBUG
    print(rh.pow) # DEBUG
    print(rh.hash(0, 3+1))
    print(rh.hash(4, 7+1))

def abc141():
    n = int(input())
    s = input()
    res = 0
    rh = rollingHash61(s)
    for i in range(n):
        for j in range(i, n):
            while(i + res < j and j + res < n):
                if rh.hash(i, i + res + 1) != rh.hash(j, j + res + 1):
                    break
                res += 1
    print(res)

def ftest():
    # ソートO(NlogN) してから ロリハ O(L*N) とその比較 O(L*N)
    l = ["/usr", "/tmp", "/usr/local/bin", "/var/log", "/bin", "/var/log/hoge", ]
    l.sort() # 短い順に出す
    ans = [] # 答え
    deleted = set() # 消すハッシュ値
    for p in l:
        if p == "/": p = ""
        ok = True
        rh = rollingHash61(p + "/") # 各パスの最後に"/"を含めてローリングハッシュ
        for h in rh.hashTable: # このパスの各文字のハッシュ値を確認し
            if h in deleted: ok = False #１回でも含まれていたらアウト
        if ok is False: continue
        # もし、エラーじゃなかった場合
        deleted.add(rh.hashTable[-1]) # このパス(の”/"を追加したhash値を記録して)
        if p == "":
            ans.append("/")
        else:
            ans.append(p)
    print(ans)

#libtest()
#abc141()
ftest()
