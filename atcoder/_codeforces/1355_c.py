import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c,d = map(int, input().split())
    #print(a,b,c,d)
    res = 0
    for x in range(a, b+1):
        zmin = c
        zmax = min(x + c - 1, d)
        if zmin > zmax:
            continue
        zcan = zmax - zmin + 1
        howmany = (c - b) + 1
        howmany = min(howmany, zmax - c) + 1
        res += (zcan + zcan - howmany + 1) * howmany // 2
        #print(x,y)
        #print(" > ({0}, {1})".format(zmin, zmax))
        #print(" > z = {0} ({1}, {2})".format(zcan, zmin, zmax))
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
        input = """1 10 20 40"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 2 2 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """500000 500000 500000 500000"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()