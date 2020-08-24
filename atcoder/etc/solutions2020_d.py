import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    minval = maxval = dat[0]
    kabu = 0
    okane = 1000
    prevval = dat[0]
    for i in range(n):
        curval = dat[i]
        #print(">cur", curval)
        if curval == prevval:
            prevval = curval
            continue
        if curval > prevval:
            prevval = curval
            continue
        # curval のほうが小さい
        kabu = okane // minval
        okane -= (minval * kabu)
        #print(" buy ", kabu , "kabu by", (minval * kabu))
        okane += (prevval * kabu)
        #print(" sell ", kabu , "get", (prevval * kabu), "now okane", okane)
        minval = curval
        maxval = prevval
        prevval = curval
    # 最後
    #print("end")
    curval = dat[n-1]
    #print("minval", minval)
    #print("curval", curval)
    if curval > minval:
        kabu = okane // minval
        okane -= (minval * kabu)
        #print(" buy ", kabu , "kabu by", (minval * kabu))
        okane += (curval * kabu)
        #print(" sell ", kabu , "get", (curval * kabu))

    print(okane)









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
        input = """7
100 130 130 130 115 115 150"""
        output = """1685"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
200 180 160 140 120 100"""
        output = """1000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
157 193"""
        output = """1216"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()