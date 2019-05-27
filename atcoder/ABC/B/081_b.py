import sys
from io import StringIO
import unittest

def resolve():
        n = int(input())
        dat_a = map(int, input().split())
        dat_a = list(dat_a)
        count = 0
        f = True
        while f:
            for i in range(n):
                if dat_a[i] % 2 == 1:
                    f = False
                else:
                    dat_a[i] /= 2
            if f:
                count += 1
            else:
                break
        print(count)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3
8 12 40"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
5 6 8 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6
382253568 723152896 37802240 379425024 404894720 471526144"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()