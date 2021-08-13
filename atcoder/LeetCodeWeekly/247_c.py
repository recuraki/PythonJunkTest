from typing import List, Tuple
from pprint import pprint



def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# nCr mod m
# modinvが必要
# rがn/2に近いと非常に重くなる
def combination(n, r, mod=10 ** 9 + 7):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i + 1, mod) % mod
    return res

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        dat = list(map(lambda x: ord(x) - ord("a"), word))
        count = [0] * 10
        for x in dat:
            count[x] += 1

        oddcombinetion = [0] * 10
        evencombinetion = [0] * 10
        for i in range(10):

            tmp = 0 # odd
            for select in range(1, count[i]+1, 2): # 全ての奇数個を選ぶ
                tmp += combination(count[i], select)
            oddcombinetion[i] = tmp

            tmp = 0 # even
            for select in range(2, count[i]+1, 2): # 全ての偶数
                tmp += combination(count[i], select)
            evencombinetion[i] = tmp + 1 # + 1は0個選択

        print(dat)
        print(count)
        res = 0
        print(oddcombinetion)
        print(evencombinetion)

        for oddnum in range(10):
            x = oddcombinetion[oddnum]
            for evennum in range(10):
                if oddnum == evennum: continue
                x *= evencombinetion[evennum]
            print(oddnum, x)
            res += x



        return res




st = Solution()

#print(st.wonderfulSubstrings(word = "aba"))
print(st.wonderfulSubstrings(word = "aabb"))
#print(st.wonderfulSubstrings(word = "he"))
