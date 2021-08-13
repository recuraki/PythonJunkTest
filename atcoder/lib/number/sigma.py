# https://rikeilabo.com/sum-formula-of-numerical-sequence

# k = 1からnまでの k の和
def sigma1(n):
    return n * (n+1) // 2

# k = 1からnまでの k^2 の和
def sigma2(n):
    return n * (n + 1) * (2*n + 1) // 6

#  k =  1からnまでの a r^(k-1) の和
def sigma3(n, a, r):
    return (a * ( r ** n - 1)  ) // (r-1)

# 累積和
import itertools
# 注意: あくまで、bは開区間
squery = lambda a, b: sdat[b] - sdat[a] # query [a, b)
def createSDAT(l):
    return list(itertools.accumulate(itertools.chain([0], l)))


import itertools
class CumSum1D():
    def __init__(self):
        pass
    def load(self, a):
        self.sdat = list(itertools.accumulate(itertools.chain([0], a)))
    def queru(self, l ,r):
        return self.sdat[r] - self.sdat[l]

"""
dat = [1,2,3,4,5,6,7,8,9]
sdat = createSDATXor(dat)
print(squeryXor(2, 5)) -> 3^4^5 = dat[2]^dat[3]^dat[4]
"""
squeryXor = lambda a, b: sdat[b] ^ sdat[a] # query [a, b)
def createSDATXor(l):
    f = lambda x, y: x ^ y
    return list(itertools.accumulate(itertools.chain([0], l), func=f))

# 愚直に作る場合
dat = [1,2,3]
sdat = list(itertools.accumulate(itertools.chain([0], dat))) # RMQ
print(sdat) # [0, 1, 3, 6]
print(sdat[2 +1] - sdat[0]) # queryは[a, b)なので注意

# wrapper
dat = [1,2,3]
sdat = createSDAT(dat)
print(sdat)
print(squery(0,2+1)) # 6
print(squery(0,0))  # 0
print(squery(0,0+1)) # 1
print(squery(1,1+1)) # 2


# zipを使って、特定のキーの累積和を作る
dat = []
dat.append([1, 10, "data1"])
dat.append([3, 100, "data3"])
dat.append([2, 1000, "data2"])
dat.sort(key=lambda x: x[0])
print(dat) # [[1, 10, 'data1'], [2, 1000, 'data2'], [3, 100, 'data3']]
print(list(zip(*dat))[1]) # (10, 1000, 100)
sdat = createSDAT(list(zip(*dat))[1])
print(sdat) # [0, 10, 1010, 1110]
print(squery(0,1))

dat = [1,2,3,4,5,6,7,8,9]
sdat = createSDATXor(dat)
print(squeryXor(2, 5))
print(3^4^5)
print(squeryXor(0, 5))
print(1^2^3^4^5)
print(squeryXor(1, 5))
print(2^3^4^5)
