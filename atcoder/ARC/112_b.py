import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        def do1(b, c):
            # 初手、マイナスのオペレーション
            if b == 0:  # 0からの場合、愚直に行く # 0を含む
                if c == 0:
                    return 1
                return (c - 1) + 1
            # b = +でも-でも気にしない
            b = abs(b)
            return 1 + min(c, b * 2)

        def do2(b, c):
            # 0じゃない方に進むオペレーション
            # その数と、その数のマイナスを含んでは「いけない」

            # まず、プラスなら、マイナスにしないと話にならない
            if b > 0 and c > 0:
                c -= 1
            if c == 0:
                return 0
            return c - 1

        b, c = map(int, input().split())
        # 0 の時はこれでカバーできる
        if b == 0:
            print(do1(0, c))
            return
        # 初手マイナスのオペレーション
        res = do1(b, c)
        res += do2(b,c)
        print(res)
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
        input = """11 2"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0 4"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """112 20210213"""
        output = """20210436"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """-211 1000000000000000000"""
        output = """1000000000000000422"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()