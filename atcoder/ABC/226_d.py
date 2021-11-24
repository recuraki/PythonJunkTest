import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    """
    - 同一座標なし
    
    """
    import math
    INF = 1 << 63
    def do():
        n = int(input())
        dat = []
        for _ in range(n):
            dat.append( tuple(map(int, input().split())) )
        needMagic = set()
        for i in range(n):
            for j in range(n):
                if i == j: continue
                needx = dat[i][0] - dat[j][0]
                needy = dat[i][1] - dat[j][1]
                g = math.gcd(abs(needx), abs(needy))
                s = "{0},{1}".format(needx // g, needy // g)
                needMagic.add(hash(s))
        print(len(needMagic))



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
1 2
3 6
7 4"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 2
2 2
4 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
0 0
0 1000000000
1000000000 0
1000000000 1000000000"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()