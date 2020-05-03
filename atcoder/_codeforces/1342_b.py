import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint

    q = int(input().strip())
    for _ in range(q):
        s = input()
        #print(">", s)
        #print(s.count("0"))
        #print(s.count("1"))
        if s.count("0") == 0 or s.count("1") == 0:
            print(s)
        else:
            ll = len(s)
            print("10" * ll)







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
00
01
111
110"""
        output = """00
01
11111
1010"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()

# 1001001
# 10011001