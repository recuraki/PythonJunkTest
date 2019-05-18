import sys
from io import StringIO
import unittest

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
        input = """8"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7"""
        output = """18"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """54"""
        output = """114"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()


def resolve():
    s = int(input())
    l = [-1] * 300
    l[1] = s
    for i in range(2,200):
        if i % 2 == 0:
            l[i] = l[i - 1] / 2
        else:
            l[i] = 3*l[i - 1] + 1

        print(str(i)+":"+str(l[i]))

        if l[i] in l[:i]:
            print(i)
            break
