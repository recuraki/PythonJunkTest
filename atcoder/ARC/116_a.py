
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
        i = int(input())
        if i % 2 == 1:
            res = "Odd"
        else:
            if (i // 2) % 2 == 1:
                res = "Same"
            else:
                res = "Even"
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
        input = """3
2
998244353
1000000000000000000"""
        output = """Same
Odd
Even"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()