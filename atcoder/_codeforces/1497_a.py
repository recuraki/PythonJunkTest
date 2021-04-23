import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        dat.sort()
        res = []
        tmp = []
        d = dict()
        for x in dat:
            if x not in d:
                d[x] = True
                res.append(x)
            else:
                tmp.append(x)
        res.extend(tmp)
        print(" ".join(list(map(str, res))))

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
        input = """3
7
4 2 0 1 3 3 7
5
2 2 8 6 9
1
0"""
        output = """0 1 2 3 4 7 3
2 6 8 9 2
0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()