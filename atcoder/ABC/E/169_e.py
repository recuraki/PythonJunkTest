import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    adat = []
    bdat = []
    for _ in range(n):
        a,b = map(int, input().split())
        adat.append(a)
        bdat.append(b)
    adat.sort()
    bdat.sort()

    if n % 2 == 1:
        aa = adat[n//2]
        bb = bdat[n//2]
        print(bb-aa + 1)

    else:
        aa1 = adat[n//2-1]
        aa2 = adat[n//2]
        bb1 = bdat[n//2-1]
        bb2 = bdat[n//2]
        #print(aa1,aa2,bb1,bb2)
        aaa = (aa1+aa2) / 2
        bbb = (bb1+bb2) / 2
        cnt = bbb - aaa
        cnt = cnt // 0.5
        print(int(cnt + 1))

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
        input = """2
1 2
2 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
100 100
10 10000
1 1000000000"""
        output = """9991"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()