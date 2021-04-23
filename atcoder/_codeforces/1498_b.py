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
        import itertools
        def countstrs(s):
            return [(k, len(list(g))) for k, g in itertools.groupby(s)]
        n, w = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort(reverse=True)
        #print(dat)
        buf = [w] * n # あまり
        bufcount = countstrs(dat)
        finalres = -1
        for width, num in bufcount:
            i = 0
            while num > 0:
                nokori = buf[i]
                canpush = min(nokori // width, num)
                if canpush != 0:
                    finalres = max(finalres, i)
                buf[i] -= (canpush * width)
                num -= canpush
                i+=1
        print(finalres+1)




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
        input = """2
5 16
1 2 8 4 8
6 10
2 8 8 2 2 8"""
        output = """2
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
6 10
1 1 1 1 1 1"""
        output = """2
3"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()