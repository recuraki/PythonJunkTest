# is_prime
# each_prime
# prime_list_eratosthenes
# factorization


# 素数判定(ミラーラビンテスト)
# https://pashango-p.hatenadiary.org/entry/20090704/1246692091
import random
def is_prime(q, k=50):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q & 1 == 0: return False

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, q - 1)
        t = d
        y = pow(a, t, q)
        while t != q - 1 and y != 1 and y != q - 1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q - 1 and t & 1 == 0:
            return False
    return True


"""
>> each_prime([2,3])
True
>> each_prime([3, 63, 7])
False
"""
# リスト内の数が互いに素かを確認する
def each_prime(l):
    f = True
    import fractions
    for i in range(len(l)):
        #print("try {0}", l[i])
        for j in range(1, len(l)- i):
            #print(" div {0}", l[i + j])
            if fractions.gcd(l[i], l[i+j]) != 1:
                f = False
                break
        if f is False:
            break
    return f


# エトラステネスのふるい
#  https://qiita.com/fantm21/items/5e270dce9f4f1d963c1e
"""
nまでの素数を一覧する。(nを含む)
>> prime_list_eratosthenes(9)
[2, 3, 5, 7, 9]
"""
def prime_list_eratosthenes(n):
    import math
    if n == 1:
        return []
    if n == 2:
        return [2]
    prime = [2]
    limit = math.sqrt(n)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit < p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

"""
n_from以上、n_to以下の素数を一覧する。(fromとtoを含む = [from, to]
>> prime_list_eratosthenes_from(5,9)
[5, 7, 9]
"""
def prime_list_eratosthenes_from(n_from, n_to):
    from bisect import bisect_left
    data = prime_list_eratosthenes(n_to)
    i = bisect_left(data, n_from)
    return data[i:]

# https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
# 素因数分解
"""
>>> factorization(16)
[[2, 4]]
>>> factorization(48)
[[2, 4], [3, 1]]
"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
# [2, 5, 5]
def factorization_expand(n):
    l = factorization(n)
    dat = []
    for a,b in l:
        dat += [a] * b
    return dat

print(prime_list_eratosthenes(100009))

l = factorization(50)
print(l)
l = factorization_expand(50)
print(l)
print(is_prime(4))
print(is_prime(13))
