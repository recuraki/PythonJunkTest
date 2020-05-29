import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    q = int(input())
    for _ in range(q):
        a, k = map(int, input().split())
        pa = -100
        for i in range(min(k,10000) - 1):
            ma, mi = -1, 10
            oa = a
            while a > 0:
                c = a % 10
                #print(" > c", c)
                a //= 10
                ma = max(ma, c)
                mi = min(mi, c)
            #print(oa,mi,ma)
            a = oa + (mi * ma)
            if pa == a:
                break
            pa = a

        print(a)



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
        input = """8
1 4
487 1
487 2
487 3
487 4
487 5
487 6
487 7"""
        output = """42
487
519
528
544
564
588
628"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()