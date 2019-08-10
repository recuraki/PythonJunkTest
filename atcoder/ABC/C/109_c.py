import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, x =  map(int, input().split())
    dat = list(map(int, input().split()))
    dat.append(x)
    dat.sort()
    dist = []
    cur = dat[0]
    for i in range(1, len( dat)):
        dist.append(dat[i] - cur)
        cur = dat[i]
    #print(dist)

    res = 0
    import fractions
    for i in range(len(dist)):
        res = fractions.gcd(res, dist[i])

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
        input = """3 3
1 7 11"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 81
33 105 57"""
        output = """24"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 1
1000000000"""
        output = """999999999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()