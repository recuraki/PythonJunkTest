import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c = map(int, input().split())
    aa,bb,cc = a%2, b%2, c%2
    res = 0
    if aa==0 and bb == 1 and cc == 0:
        res += 1
        a,c = a+1, c+1
    elif aa==1 and bb == 0 and cc == 0:
        res += 1
        b,c = b+1, c+1
    elif aa == 0 and bb == 0 and cc == 1:
        res += 1
        b, a = b + 1, a + 1
    elif aa==0 and bb == 1 and cc == 1:
        res += 1
        b,c = b+1, c+1
    elif aa==1 and bb == 0 and cc == 1:
        res += 1
        a,c = a+1, c+1
    elif aa == 1 and bb == 1 and cc == 0:
        res += 1
        b, a = b + 1, a + 1
    l = [a,b,c]
    l.sort()
    res += (l[2] - l[1]) // 2
    res += (l[2] - l[0]) // 2
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
        input = """2 5 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 6 3"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """31 41 5"""
        output = """23"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()