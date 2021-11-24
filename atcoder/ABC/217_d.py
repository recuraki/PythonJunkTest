import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        l, qnum = map(int, input().split())
        dat = [0, l]
        from bisect import bisect_left
        needsort = False
        for _  in range(qnum):
            c, x = map(int, input().split())
            if c == 1:
                dat.append(x)
                needsort = True
                continue
            else: # c == 2
                if needsort:
                    needsort = False
                    dat.sort()
                ind = bisect_left(dat, x)
                a = dat[ind-1]
                b = dat[ind]
                print(b - a)
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
        input = """5 3
2 2
1 3
2 2"""
        output = """5
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 3
1 2
1 4
2 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100 10
1 31
2 41
1 59
2 26
1 53
2 58
1 97
2 93
1 23
2 84"""
        output = """69
31
6
38
38"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()