import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    MOD = 1000000000+7
    def lcm(x, y):
        import fractions
        return (x * y) // fractions.gcd(x, y)

    n = int(input())
    dat = list(map(int, input().split()))
    #dat.sort(reverse=True)

    base = 1
    for i in range(len(dat)):
        base = lcm(base, dat[i])
    res = 0

    for i in range(len(dat)):
        res += base // dat[i]

    print(res%MOD)




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
        input = """3
2 3 4"""
        output = """13"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
12 12 12 12 12"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5
7 7 7 7 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """3
1000000 999999 999998"""
        output = """996989508"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()