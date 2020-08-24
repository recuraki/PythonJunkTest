import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    def do():
        n, g3, g2, g1 = map(int, input().split())
        sheet3 = n
        sheet2 = n
        #print("p1", n, g3, g2, g1, sheet3, sheet2)

        # 3人グループを振り分ける
        can3 = min(g3, sheet3)
        g3 -= can3
        sheet3 -= can3
        #print("p2", n, g3, g2, g1, sheet3, sheet2)

        # 3人席に割り当てられない人は2人グループと1人に分ける
        g2 += g3
        g1 += g3

        # 次に1人グループの処理
        # 3人席を要求する
        need3 = math.ceil(g1 / 2) # 1人で欲しい数
        can3 = min(sheet3, need3) # それに対して割り当てられる数
        g1 -= can3 * 2
        g1 = max(g1, 0)
        sheet3 -= can3
        #print("p3", n, g3, g2, g1, sheet3, sheet2)

        if (g1 + g2) <= (sheet2 + sheet3):
            print("YES")
        else:
            print("NO")

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
        input = """3 1 1 5"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 0 3 3"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """1 0 0 0"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """1 1 0 0"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_211(self):
        print("test_input_211")
        input = """1 0 1 0"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_21112(self):
        print("test_input_21112")
        input = """1 0 0 1"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_211121(self):
        print("test_input_211121")
        input = """1 0 1 1"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2111211(self):
        print("test_input_2111211")
        input = """1 1 0 1"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_21112111(self):
        print("test_input_21112111")
        input = """1 1 1 1"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_211121111(self):
        print("test_input_211121111")
        input = """3 4 2 0"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 5 0 0"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 4 0 0"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """3 4 1 0"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_311(self):
        print("test_input_311")
        input = """3 4 2 0"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_411(self):
        print("test_input_311")
        input = """3 0 6 0"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_411(self):
        print("test_input_311")
        input = """3 0 5 3"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_411(self):
        print("test_input_311")
        input = """3 0 5 4"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()