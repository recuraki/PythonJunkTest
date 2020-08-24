import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k =map(int, input().split())
    used = [False] * (n + 10)
    for i in range(k):
        x = int(input())
        #print("x", x)
        dat = list(map(int, input().split()))
        #print(dat)
        for j in range(len(dat)):
            used[dat[j]] = True
    res = 0
    #print(used)
    for i in range(n):
        #print(i)
        if used[i + 1] is False:
            res += 1
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
        input = """3 2
2
1 3
1
3"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3
1
3
1
3
1
3"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()