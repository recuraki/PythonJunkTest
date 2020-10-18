import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        q = int(input())
        for _ in range(q):
            n = int(input())
            s = input()
            if s.find("<") == -1:
                print(n)
                continue
            if s.find(">") == -1:
                print(n)
                continue
            s = s[-1] + s + s[0]
            res = 0
            for i in range(1, n+1):
                if s[i-1] == "-" or s[i] == "-":
                    res += 1
            print(res)


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
        input = """5
4
-><-
5
>>>>>
3
<--
2
<>
6
-<-->-"""
        output = """3
5
3
0
4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()