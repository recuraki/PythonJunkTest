import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    cnt = 0
    for i in range(1,1000000000000):
        s = str(i)
        x = int(s + s)
        if x > n:
            break
        cnt += 1
    print(cnt)



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
        input = """33"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1333"""
        output = """13"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10000000"""
        output = """999"""
        self.assertIO(input, output)
    def test_input_33(self):
        print("test_input_33")
        input = str(10**12)
        output = """999"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()