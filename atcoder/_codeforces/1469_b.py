import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    #input = sys.stdin.readline

    import itertools
    # 注意: あくまで、bは開区間
    squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)
    def createSDAT(l):
        return list(itertools.accumulate(itertools.chain([0], l)))

    from pprint import pprint
    def do():
        n = int(input())
        datn = list(map(int, input().split()))
        m = int(input())
        datm = list(map(int, input().split()))
        s1=createSDAT(datn)
        s2=createSDAT(datm)
        print(max(0,max(s1)+max(s2)))
    q = int(input())
    for _ in range(q):
        do()
    # do()


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
4
6 -5 7 -3
3
2 3 -4
2
1 1
4
10 -3 2 2
5
-1 -2 -3 -4 -5
5
-1 -2 -3 -4 -5
1
0
1
0"""
        output = """13
13
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()