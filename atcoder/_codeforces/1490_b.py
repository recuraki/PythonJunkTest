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
        n = int(input())
        dat = list(map(int, input().split()))
        buf = [0, 0, 0]
        for x in dat:
            buf[x % 3] += 1
        target = n // 3
        res = 0

        for i in range(2):
            if buf[0] > target:
                gogo = buf[0] - target
                res += gogo
                buf[1] += gogo
                buf[0] -= gogo
            if buf[1] > target:
                gogo = buf[1] - target
                res += gogo
                buf[2] += gogo
                buf[1] -= gogo
            if buf[2] > target:
                gogo = buf[2] - target
                res += gogo
                buf[0] += gogo
                buf[2] -= gogo

        print(res)



    q = int(input())
    for _ in range(q):
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
        input = """1
2
2 8
"""
        output = """---"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()