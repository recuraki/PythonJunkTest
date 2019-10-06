import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_s = []
    for i in range(n):
        dat_s.append(int(input()))
    total = sum(dat_s)
    f = True

    if total % 10 != 0:
        print(total)
        f = False
    else:
        dat_s.sort()
        for i in range(len(dat_s)):
            if dat_s[i] % 10 != 0:
                print(total - dat_s[i])
                f = False
                break

    if f:
        print("0")


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
        logging.info("test_input_1")
        input = """3
5
10
15"""
        output = """25"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """3
10
10
15"""
        output = """35"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """3
10
20
30"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()