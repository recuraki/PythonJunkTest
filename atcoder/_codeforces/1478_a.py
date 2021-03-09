
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import collections
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        C = collections.Counter(dat)
        res = 0
        for k in C.keys():
            res = max(res, C[k])
        print(res)

    q = int(input())
    for _ in range(q):
        do()




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
6
1 1 1 2 3 4
5
1 1 2 2 3
4
2 2 2 2
3
1 2 3
1
1"""
        output = """3
2
4
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()