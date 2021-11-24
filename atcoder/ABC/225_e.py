import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint

    from fractions import Fraction

    import math
    INF = 1 << 63

    def do():
        from decimal import Decimal
        n = int(input())
        dat = []
        for _ in range(n):
            x, y = map(int, input().split())
            x1, y1 = x - 1, y
            x2, y2 = x, y - 1
            if x1 == 0: p1 = 2 ** 50
            else: p1 = Fraction(y1, x1)
            p2 = Fraction(y2, x2)
            dat.append((p2, p1))
        dat.sort(key=lambda x: (x[1], x[0]))
        ans = 0
        curtime = -1
        for s, t in dat:
            if s >= curtime:
                ans += 1
                curtime = t
        print(ans)
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
2 1
1 1
1 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
414598724 87552841
252911401 309688555
623249116 421714323
605059493 227199170
410455266 373748111
861647548 916369023
527772558 682124751
356101507 249887028
292258775 110762985
850583108 796044319"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()