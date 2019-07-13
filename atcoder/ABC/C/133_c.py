import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    l, r = map(int, input().split())
    # 2019 = 3 * 673

    rr = min(r, l + 2020)

    res = 1000000
    for i in range(l, rr+1):
        for j in range(l + 1, rr + 1):
            #print("{0}, {1}".format(i, j))
            if i >= j:
                #print("skip")
                continue

            if res > i*j % 2019:
                #print("{0}, {1}".format(i, j))
                res = i*j % 2019
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
        input = """2020 2040"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 5"""
        output = """20"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3_2(self):
        print("test_input_3")
        input = """0 5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3_3(self):
        print("test_input_33")
        input = """0 3"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()