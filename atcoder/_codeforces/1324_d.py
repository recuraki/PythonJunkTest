import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    n = int(input())
    data = list(map(int, input().split()))
    datb = list(map(int, input().split()))
    datc = [data[x] - datb[x] for x in range(n)]
    datc.sort()
    import bisect
    #print(datc)
    res = 0
    for i in range(n-1, -1, -1):
        #print("i", i)
        x = datc[i]
        if x <= 0:
            #print("end")
            break
        c = bisect.bisect_right(datc, -x)
        #print(c)
        res += i-c
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
4 8 2 6 2
4 5 4 1 3"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
        4 8 2 6 2 2
        4 5 4 1 3 2000"""
        output = """7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()