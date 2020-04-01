import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def nCr(n, r):
        import math
        # nCrのr>nは組み合わせが存在しないので0を返す
        # raiseすべきのこともあるかも
        if r > n:
            return 0
        return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))

    memo = [-1] * 300000
    memo2 = [-1] * 300000
    memo3 = [-1] * 300000

    n = int(input())
    dat = list(map(int, input().split()))
    from collections import Counter
    c = Counter(dat)
    total = 0
    #print(c)
    for k in c:
        if c[k] > 1:
            memo[k] = nCr(c[k], 2)
            memo2[k] = nCr(c[k]-1, 2)
            memo3[k] = memo[k] - memo2[k]
            total += memo[k]
    #print(memo[:10])
    #print(memo2[:10])
    #print(memo3[:10])
    #print(total)
    for i in range(n):
        if memo3[dat[i]] == -1:
            print(total)
        else:
            print(total - memo3[dat[i]])


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
        input = """5
1 1 2 1 2"""
        output = """2
2
3
2
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 2 3 4"""
        output = """0
0
0
0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
3 3 3 3 3"""
        output = """6
6
6
6
6"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """8
1 2 1 4 2 1 4 1"""
        output = """5
7
5
7
7
5
7
5"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """3
3 3 3"""
        output = """1
1
1"""
        self.assertIO(input, output)

    def test_input_6(self):
        print("test_input_6")
        input = """3
1 2 3"""
        output = """0
0
0"""
        self.assertIO(input, output)

    def test_input_7(self):
        print("test_input_7")
        input = """4
1 2 1 1"""
        output = """1
3
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()