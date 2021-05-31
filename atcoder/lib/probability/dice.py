def nCr(n, r):
    import math
    # nCrのr>nは組み合わせが存在しないので0を返す
    # raiseすべきのこともあるかも
    if r > n:
        return 0
    return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))
################################################################

# https://qiita.com/recuraki/items/6ee94805d84955e49585
def do1(n, r, pattern):  # pattern面のさいころをn回降ってr種類出る確率
    res = (1.0 / pattern ** (n * 1.0)) * nCr(pattern, r)
    tmp = 0
    for i in range(r + 1):
        tmp += ((-1) ** (r - i)) * nCr(r, i) * (i ** n)
    return res * tmp

print(do1(1,1,6))
print(do1(1,2,6))
print(do1(2,2,6))

