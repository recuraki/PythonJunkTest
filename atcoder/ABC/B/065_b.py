from io import StringIO
import unittest
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = [-1] * (n + 1)
    for i in range(n):
        a = int(input())
        dat_a[i + 1] = a
    cur = 1
    f = False
    for i in range(n):
        if cur == 2:
            f = True
            break
        cur = dat_a[cur]
    if f:
        print(i)
    else:
        print("-1")

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
3
1
2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()