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
        res = -99999999999999999999999999999999999
        candidate = []
        buf = []
        isnega = True if dat[0] < 0 else False
        for i in range(n):
            if isnega:
                if dat[i] > 0:
                    candidate.append(max(buf))
                    buf = []
                    isnega = False
                else:
                    pass
            else: # posi
                if dat[i] < 0:
                    candidate.append(max(buf))
                    buf = []
                    isnega = True
                else:
                    pass
            buf.append(dat[i])
        candidate.append(max(buf))
        print(sum(candidate))


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
        input = """4
5
1 2 3 -1 -2
4
-1 -2 -1 -3
10
-2 8 3 8 -4 -15 5 -2 -3 1
6
1 -1000000000 1 -1000000000 1 -1000000000"""
        output = """2
-1
6
-2999999997"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()