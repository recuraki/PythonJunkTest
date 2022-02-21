import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63

    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        la = dat[:n]
        lb = dat[n:]
        from copy import deepcopy
        buf = deepcopy(la)
        def f(base):
            select = []
            mi = INF
            miind = 0
            cnt = 0
            for i in range(n):
                if la[i] <= base:
                    if la[i] < mi:
                        mi = la[i]
                        miind = i
                    select.append(i)
            ans = []
            for ind in select:
                if ind < miind: continue
                ans.append(la[ind])
            for ind in select:
                if ind < miind: continue
                ans.append(lb[ind])
            return ans
        buf = list(set(buf))
        buf.sort()
        ans = f(buf[0])

        print(" ".join(list(map(str, ans))))

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
2 1 3 1 2 2"""
        output = """1 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
38 38 80 62 62 67 38 78 74 52 53 77 59 83 74 63 80 61 68 55"""
        output = """38 38 38 52 53 77 80 55"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """12
52 73 49 63 55 74 35 68 22 22 74 50 71 60 52 62 65 54 70 59 65 54 60 52"""
        output = """22 22 50 65 54 52"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()