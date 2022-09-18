# Pow
# 基本的にpowで十分(愚直に^xされず、ちゃんと内部で工夫してくれる
# Python3.8以降ではpow(x, -1, mod)で逆元を求められる

# n乗
# 基本的にpow
# pow(n, x, mod)

# https://nagiss.hateblo.jp/entry/2019/07/01/185421
# d,x,y: d = bx + (a mod b) y
# 解が存在しない場合はb,0,1を返す
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

# https://nagiss.hateblo.jp/entry/2019/07/01/185421
# mを法とするaの乗法的逆元
# egcdが必要
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# https://nagiss.hateblo.jp/entry/2019/07/01/185421
# キャッシュを用いないので必要があるなら後述のものを使う
# nCr mod m
# modinvが必要
# rがn/2に近いと非常に重くなる
# 具体的にはr = 2 * 10^5くらいは十分に間に合う
def combinationNoCache(n, r, mod=10 ** 9 + 7):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i + 1, mod) % mod
    return res

"""
ax === b (mod m)を解く
"""
def modularLinearEquationSolver(a, b, m):
    res = []
    d, x, y = egcd(a, m)
    if b % d == 0:
        x0 = (x * (b // d)) % m
        for i in range(d):
            res.append((x0 + i * (m//d)) % m)
    else:
        return None
    return res

# https://qiita.com/drken/items/ae02240cd1f8edfc86fd
# 2元だけを対象にする関数。特にこれを使う意味はない。(移植しただけ。習作
def crtSimple(b1, m1, b2, m2):
    d, x, y = egcd(m1, m2)
    if (b2 - b1) % d != 0:
        return [0, -1]
    m = m1 * (m2 // d) # LCM
    tmp = (b2 - b1) // d * x % (m2 // d)
    r = (b1 + m1 * tmp) % m
    return [r, m]

# https://qiita.com/drken/items/ae02240cd1f8edfc86fd
# https://qiita.com/recuraki/items/11fd78580e03a5a6d58c
# a = b1 (mod m1)
# a = b2 (mod m2)
# となるような、 a = r (mod m) を返す
# r=0

def crt(bList, mList):
    r, m = 0, 1
    for i in range(len(bList)):
        d, x, y = egcd(m, mList[i])
        if (bList[i] - r) % d != 0:
            return [0, -1]
        tmp = (bList[i] - r) // d * x % (mList[i] // d)
        r += m * tmp
        m *= mList[i] // d
    return [r, m]

# Garnerする
# 制約: m1, m2...は互いに素である必然性がある
# a = b1 (mod m1)
# a = b2 (mod m2)
# となるような 最小の a mod MOD(入力する)を求める
def garner(bList: list, mList: list, MOD: int):
    mList.append(MOD)
    coeffs = [1 for _ in range(len(mList))]
    constants = [0 for _ in range(len(mList))]
    for k in range(len(bList)):
        t = ((bList[k] - constants[k]) * modinv(coeffs[k], mList[k])) % mList[k]
        for i in range(k + 1, len(mList)):
            constants[i] += t * coeffs[i]
            constants[i] %= mList[i]
            coeffs[i] *= mList[k]
            coeffs[i] %= mList[i]
    return constants[-1]

##############
#■ 高速cmb mod (cacheする
##############
# https://www.planeta.tokyo/entry/5195/
mod = 998244353
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p

p = mod
N = 5 * 10 ** 5  # N は必要分だけ用意する
N = 20
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


print("fac")
print(fact[:10])
print(inv[:10])
print(factinv[:10])
print(cmb(10,5,p))
# ここまで

a,b,c = 14,30,100
print("modularLinearEquationSolver", a,b,c, "=", modularLinearEquationSolver(a,b,c))

a,b,c = 35,10,50
print("modularLinearEquationSolver", a,b,c, "=", modularLinearEquationSolver(a,b,c))

a,b,c,d = 2,3,3,5
print("CRT",a,b,c,d, "=", crtSimple(a,b,c,d))

a,b,c,d = 2,3,4,5
print("CRT",a,b,c,d, "=", crtSimple(a,b,c,d))

blist = [2,3]
mlist = [3,5]
print("CRT",blist, mlist, "=", crt(blist, mlist))
print(" x = 2 (mod3)")
print(" x = 3 (mod5)")
print(" RES -> x = 8 (mod15)")


blist = [2,4]
mlist = [3,5]
print("CRT",blist, mlist, "=", crt(blist, mlist))

blist = [2,4]
mlist = [3,5]
print("garner",blist, mlist, "=", garner(blist, mlist, mod))

blist = [80712, 320302, 140367]
mlist = [221549, 699312, 496729]
print("CRT",blist, mlist, "=", crt(blist, mlist))

print(modinv(2**10, 10**9+7))  # 71289063
# print(pow(2**10, -1, 10**9+7)) # 71289063

print(egcd(111, 30))
print(egcd(111, 7))
print(egcd(13, 1))

