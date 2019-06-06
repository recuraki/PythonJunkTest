import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, a = map(int, input().split())
    dat_x = list(map(int, input().split()))
    dp = []
    for i in range(50):
        dp.append([[]] * (50 * 50 + 1))

    count = 0

    for i in range(len(dat_x)):
        dp[i][0] = [0]
        for j in range(0, len(dp[i])):
            if dp[i][j] != []:
                cache = dp[i][j]
                new = dp[i+1][j + dat_x[i]]
                cache = map(lambda x: x + 1, cache)
                new.append(cache)
                dp[i+1][j + dat_x[i]] = cache


    print(count)
    for i in range(10):
        print(dp[i][0:30])


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
        input = """4 8
7 9 8 9"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """3 8
6 6 9"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """8 5
3 6 2 8 7 6 5 9"""
        output = """19"""
        self.assertIO(input, output)
    def test_input_4(self):
        logging.info("test_input_4")
        input = """33 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3"""
        output = """8589934591"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()