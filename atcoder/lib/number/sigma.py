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
dat = [1,2,3]
sdat = list(itertools.accumulate(itertools.chain([0], dat)))
print(sdat) # [0, 1, 3, 6]
print(sdat[2 +1] - sdat[0]) # queryは[a, b)なので注意