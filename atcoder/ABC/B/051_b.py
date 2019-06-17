import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    k, s = map(int, input().split())
    res = 0
    for x in range(k + 1):
        if (s - x) < 0:
            break
        for y in range(0, s - x + 1):
            if (s - x - y) < 0:
                break
            z = s - y - x
            if z >= 0 and x <= k and y <= k and z <= k:
                #print("{0}, {1} {2}".format(str(x), str(y), str(z)))
                res += 1
    print(res)


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
        input = """2 2"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 15"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()