# https://rikeilabo.com/sum-formula-of-numerical-sequence

# 1-nまでの k の和
def sigma1(n):
    return n * (n+1) // 2

# 1-nまでの k^2 の和
def sigma2(n):
    return n * (n + 1) * (2*n + 1) // 6


# 1-nまでの a r^(k-1) の和
def sigma3(n, a, r):
    return (a * ( r ** n - 1)  ) // (r-1)


