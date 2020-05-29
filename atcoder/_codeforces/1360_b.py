import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n = int(input())
        dat = list(map(int, input().split()))
        a = 0
        b = 0
        dat.sort()
        res = 9999999999999999999999999999
        for i in range(n-1):
            res = min(res, dat[i+1] - dat[i])
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
        input = """5
5
3 1 2 6 4
6
2 1 3 2 4 3
4
7 9 3 1
2
1 1000
3
100 150 200"""
        output = """1
0
2
999
50"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()