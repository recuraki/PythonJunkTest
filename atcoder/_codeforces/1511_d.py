import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n, k = map(int, input().split())

        s = []
        curstart = 0
        cur = 0
        while True:
            for i in range(k):
                cur += 1
                s.append(i)
                if cur == n:
                    break
                cur += 1
                s.append(i)
                if cur == n:
                    break
            if cur == n:
                break
            for i in range(k):
                for j in range(i + 1, k):
                    cur += 1
                    s.append(j)
                    if cur == n:
                        break
                    cur += 1
                    s.append(i)
                    if cur == n:
                        break
                if cur == n:
                    break
            if cur == n:
                break

        l = list(map(lambda x: chr(ord("a") + x), s))
        print("".join(l))

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
        input = """9 4"""
        output = """aabacadbb"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 1"""
        output = """aaaaa"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 26"""
        output = """codeforces"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()