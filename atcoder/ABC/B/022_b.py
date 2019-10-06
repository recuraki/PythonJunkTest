import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    d = [False] * 100001
    res = 0
    for i in range(n):
        x = int(input())
        if d[x]:
            res += 1
        d[x] = True
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
    def test_input1(self):
        print("test_input1")
        input = """5
1
2
3
2
1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """11
3
1
4
1
5
9
2
6
5
3
5"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()