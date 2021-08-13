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
        import math
        def ddd(num):
            total = 0
            s = list(str(num))
            for x in s:
                total += int(x)
            print(num, total, math.gcd(num, total))
            return math.gcd(num, total)

        n = int(input())
        while True:
            if ddd(n) == 1:
                n+=1
                continue
            break
        print(n)


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
        input = """1
290"""
        output = """"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """1
987654323"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()