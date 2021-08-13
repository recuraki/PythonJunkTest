import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        buf = []
        for x in dat:
            buf.append(x)
        buf.sort()
        isadd = set()
        total = k // n
        for i in range(k % n):
            isadd.add(buf[i])
        #print(total, isadd)

        for x in dat:
            if x in isadd:
                print(total + 1)
            else:
                print(total)



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
        input = """2 7
1 8"""
        output = """4
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 3
33"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7 1000000000000
99 8 2 4 43 5 3"""
        output = """142857142857
142857142857
142857142858
142857142857
142857142857
142857142857
142857142857"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()