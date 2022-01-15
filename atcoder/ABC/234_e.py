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
        target = int(input())
        l = []
        keta = 20
        for i in range(1, keta + 1):
            for num in range(1, 10):
                l.append(str(num) * i)

        for delta in range(1, 10):
            for first in range(1, 10):
                cur = first
                s = str(cur)
                l.append(s)
                while True:
                    if not (0 <= cur <= 9): break
                    cur += delta
                    if not (0 <= cur <= 9): break
                    s = s + str(cur)
                    l.append(s)

        for delta in range(1, 10):
            for first in range(1, 10):
                cur = first
                s = str(cur)
                l.append(s)
                while True:
                    if not (0 <= cur <= 9): break
                    cur -= delta
                    if not (0 <= cur <= 9): break
                    s = s + str(cur)
                    l.append(s)

        l = list(set(l))
        l = list(map(int, l))
        l.sort()
        # print(l)
        if target in l:
            print(target)
            return
        from bisect import bisect_right
        ind = bisect_right(l, target)
        print(l[ind])

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
        input = """152"""
        output = """159"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """88"""
        output = """88"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8989898989"""
        output = """9876543210"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_3")
        input = """90"""
        output = """90"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()