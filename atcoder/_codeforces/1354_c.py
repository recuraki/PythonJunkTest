import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys

    q = int(input())
    import math
    for _ in range(q):
        on = int(input())
        n = on * 2
        a = 1
        m = on - 1
        v1 = ( a * math.sin(m * math.pi / n)) / math.sin(math.pi / n)
        print(v1)
        #v2 = ( a * math.sin(m * math.pi / n) / sin(math.pi / n)





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
2
4
200"""
        output = """1.000000000
2.414213562
127.321336469"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()