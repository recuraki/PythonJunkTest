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

    n = int(input())

    dat = factorization(n)
    #print(dat)

    buf = []

    for a,b in dat:
        for j in range(b):
            buf.append(a)
    dat.sort(key=lambda x: x[0])

    used = dict()
    cur = 1
    res = 1

    for a, b in dat:
        if a == 1:
            continue
        cur = 1
        for i in range(b):
            cur *= a
            if cur not in used:
                used[cur] = True
                res += 1
                cur = 1

    print(len(used))





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
        input = """24"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """64"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1000000007"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """997764507000"""
        output = """7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()