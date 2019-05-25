import sys
from io import StringIO
import unittest

def resolve():
    s = int(input())
    f = lambda n: (n/2) if n%2==0 else (3*n + 1)
    prevval = s
    history = [s]
    c = 2
    while True:
        newval = f(prevval)
        if newval in history:
            break
        history.append(newval)
        c += 1
        prevval = newval
    print(c)


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


