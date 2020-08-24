import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 1000000007
    import collections
    n = int(input())
    dat1 = []
    dat2 = []
    for i in range(n):
        a,b = map(int, input().split())
        dat1.append(a)
        dat2.append(b)
    ngfish = []
    for i in range(n):
        res = 0
        for j in range(i+1, n):
            if dat1[i] * dat1[j] + dat2[i] * dat2[j] == 0:
                res += 1
        ngfish.append(res)

    #print(ngfish)

    res = 0
    for i in range(len(ngfish)):
        res += pow(2, n - i - 1 - ngfish[i], mod)
        res %= mod
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
    def test_input_1(self):
        print("test_input_1")
        input = """3
1 2
-1 1
2 -1"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
3 2
3 2
-1 1
2 -1
-3 -9
-8 12
7 7
8 1
8 2
8 4"""
        output = """479"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()