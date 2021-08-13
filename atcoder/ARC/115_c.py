import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    res = [0] * (10**5+1)
    for i in range(1, 10**5 + 2):
        cur = 1
        while i * cur <= 10**5:
            res[cur] += 1
            cur += 1
    print(res[:100])

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
        input = """4"""
        output = """1 2 2 3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()