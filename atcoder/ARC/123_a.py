import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    def do():
        def f(a,b,c):
            can1 = can2 = can3 = can4 = can5 = 10**18

            # a -> bに合わせる
            d1 = b - a
            targetc = b + d1 # cにしたい
            if c <= targetc:
                can1 = abs(targetc - c)

            # b -> cに合わせる
            d1 = c - b
            targeta = b - d1 # cにしたい
            #print(targeta, d1)
            if a <= targeta:
                can2 = abs(targeta - a)

            # 真ん中を合わせる
            d1 = b - a
            d2 = c - b
            if d1 < d2:
                can3 = (d2 - d1) * 2

            if a == max(a,b,c):
                can4 = min(can4, (a-a) + (a-b) + (a-c))
            if b == max(a,b,c):
                can4 = min(can4, (b-a) + (b-b) + (b-c))
            if c == max(a,b,c):
                can4 = min(can4, (c-a) + (c-b) + (c-c))

            d1 = b - a
            d2 = c - b
            if d1 < d2: # bを足せる条件
                can5 = 0
                if abs(d1+d2) % 2 == 1:
                    c += 1
                    d2 += 1
                    can5 = 1
                can5 += (d2-d1)//2



            #print(can1, can2, can3, can4, can5)
            return (min(can1, can2, can3, can4, can5))
        a,b,c = map(int, input().split())
        print(f(a,b,c))
        #print(f(c,b,a))
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
        input = """4 8 10"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 3 4"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 2 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1000000000000000 1 1000000000000000"""
        output = """999999999999999"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """1 2 10"""
        output = """5"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()