import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if arr == []:
            arr.append([n, 1])
        return arr

    # [2, 5, 5]
    def factorization_expand(n):
        l = factorization(n)
        dat = []
        for a, b in l:
            dat += [a] * b
        return dat

    n = int(input())
    dat = list(map(int, input().split()))
    dat.sort()
    res = set()

    for val in dat:
        divs = factorization_expand(val)
        for x in divs:
            res.add(x)


    #print("---")
    from itertools import combinations
    from math import gcd
    finalres = 10**18
    for i in range(1, len(res) + 1):
        for l in combinations(res, i):
            cand = 1
            for x in l:
                cand *= x
            #print(l, cand)
            isok = True
            for x in dat:
                if gcd(x, cand) == 1:
                    isok = False
                    break
            #print(l, cand, isok)
            if isok:
                finalres = min(finalres, cand)
    print(finalres)





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
        input = """2
4 3"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
47"""
        output = """47"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
3 4 6 7 8 9 10"""
        output = """42"""
        self.assertIO(input, output)
    def test_input_34self(self):
        print("test_input_34")
        input = """2
13 7 5 29"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_14self(self):
        print("test_input_314")
        input = """4
13 7 5 29"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()