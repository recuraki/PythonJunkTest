import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    can = False
    for b in range(1, 100):
        y = 5 ** b
        nokori = n - y

        if nokori < 0:
            break

        if nokori == 0 or nokori == 1:
            break

        a = 0

        while True:
            if nokori == 1:
                can = True
                break
            if nokori % 3 == 0:
                a += 1
                nokori //= 3
            else:
                break

        if can:
            break


    if can is False:
        print(-1)
    else:
        print(a, b)

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
        input = """106"""
        output = """4 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1024"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10460353208"""
        output = """21 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()