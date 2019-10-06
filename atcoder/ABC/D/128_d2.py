import sys
from io import StringIO
import unittest

def resolve():
    n, k = map(int, input().split())
    dat_v = map(int, input().split())
    dat_v = list(dat_v)
    res = 0

    for i in range(k):
        pool = dat_v[0:k - i] + dat_v[-(i) + k:]
        print(pool)

        p = []
        m = []
        for j in range(len(pool)):
            if pool[j] >= 0:
                p.append(pool[j])
            else:
                m.append(pool[j])
        p.sort()
        m.sort()
        for j in range(len(m)):
            if len(p) > 0:
                if abs(m[j]) > p[0]:
                    p = p[1:]
                    m[j] = 0
        print(p)
        print(m)
        res = max(res, sum(p) + sum(m))
    print(res)



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test__1(self):
        input = """6 4
-10 8 2 1 2 6"""
        output = """14"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 4
-6 -100 50 -2 -5 -3"""
        output = """44"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 3
-6 -100 50 -2 -5 -3"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()