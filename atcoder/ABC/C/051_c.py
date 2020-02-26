import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x1, y1, x2, y2 = map(int, input().split())
    res = ""

    res += "U" * (y2-y1)
    res += "R" * (x2-x1)
    res += "D" * (y2-y1)
    res += "L" * (x2-x1)
    res += "L" + "U" * (y2-y1 + 1)
    res += "R" * (x2-x1 + 1) + "D"

    res += "R" + "D" * (y2-y1 + 1)
    res += "L" * (x2-x1 + 1) + "U"


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
        input = """0 0 1 2"""
        output = """UURDDLLUUURRDRDDDLLU"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """-2 -2 1 1"""
        output = """UURRURRDDDLLDLLULUUURRURRDDDLLDL"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()