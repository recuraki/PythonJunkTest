import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for _ in range(q):
        s = input()
        res = s[0:2]
        i = 2
        l = len(s)
        while i < l:
            res += s[i+1]
            i+=2
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
        input = """4
abbaac
ac
bccddaaf
zzzzzzzzzz"""
        output = """abac
ac
bcdaf
zzzzzz"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()