
# 組み合わせ
def nCr(n, r):
    import math
    # nCrのr>nは組み合わせが存在しないので0を返す
    # raiseすべきのこともあるかも
    if r > n:
        return 0
    return math.factorial(n) //  ( (math.factorial(n - r) * math.factorial(r)) )


def nCr_with_replacement(n, r):
    # 重複を許容するコンビネーション
    if r > n:
        return 0
    return nCr(n + r - 1, r)

# 並び変えるときの組み合わせ
def nPr(n, r):
    import math
    # nCrのr>nは組み合わせが存在しないので0を返す
    if r > n:
        return 0
    return math.factorial(n) // math.factorial(n - r)

# 最小公倍数
# x,yに0が入ると0になるので、適当に初期値を入れましょう。(最悪1でいいと思います)
def lcm(x, y):
    import fractions
    return (x * y) // fractions.gcd(x, y)