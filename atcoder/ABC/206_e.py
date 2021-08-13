import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
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

    l = prime_list_eratosthenes(500010)

    from pprint import pprint
    def do():
        N = 500010
        N = 100
        MAXX = 100010
        MAXX = 100
        import collections
        divs = collections.defaultdict(int)
        l, r = map(int, input().split())
        MAXX = r
        dat = [[]  for _ in range(MAXX + 10)]
        primes = prime_list_eratosthenes(N)
        for x in primes:
            i = 2
            while x*i < MAXX:
                dat[x*i].append(x)
                if x*i >= l:
                    divs[x] += 1
                i += 1
        print(dat[:100])
        print(divs)
        finalres = 0
        for i in range(l, r + 1):
            res = 0 # 一旦全部の約数の総和
            buf = []
            for x in dat[i]:
                cnt = 0
                res += divs[x]
                j = 1
                while True:
                    if x**j > r:
                        break
                    if l <= x**j:
                        cnt += 1
                    j += 1
                buf.append(cnt )
            if res == 0: # 素数の場合
                continue
            bufcnt = 1
            for x in buf:
                bufcnt *= x
            bufcnt -= 1 # 0,0,0の選択の除去
            print(i, res, bufcnt)
            res -= bufcnt
            finalres += res
        print(finalres)






    do()# Nを変える


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """3 7"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 10"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 1000000"""
        output = """392047955148"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()