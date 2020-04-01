import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    import collections
    c = collections.Counter(dat)
    data = []
    for k in c:
        cnt = c[k]
        if cnt > 1:
            data.append((k, cnt//2))
    data.sort(reverse=True)
    #print(data)
    if len(data) == 0:
        print(0)
    else:
        a = data[0]
        x =a[0]
        if a[1] > 1:
            y = a[0]
            print(x*y)
        elif len(data) > 1:
            y = data[1][0]
            print(x*y)
        else:
            print(0)

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
        input = """6
3 1 2 4 2 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
3 3 3 3 4 4 4 5 5 5"""
        output = """20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()