import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, y = map(int, input().split())
    cur = 0
    ok = False
    for i in range(n + 1):
        if ok:
            break
        if i * 10000 > y:
            break
        if (10000 * i == y) and (i == n):
            ok = True
            print("{0} 0 0".format(i))
            break
        cur = y - (10000 * i)
        for j in range((n + 1) - i):
            if ok:
                break
            if j * 5000 > cur:
                break
            if 5000 * j == cur  and (i + j) == n:
                print("{0} {1} 0".format(i,j))
                ok = True
                break
            if ((cur - 5000 * j) % 1000) == 0:
                k = (cur - 5000 * j) / 1000
                k = int(k)
                if (i + j + k) == n:
                    print("{0} {1} {2}".format(i,j, k ))
                    ok = True
                    break
    if not ok:
        print("-1 -1 -1")




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
        input = """9 45000"""
        output = """4 0 5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20 196000"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000 1234000"""
        output = """14 27 959"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """2000 20000000"""
        output = """2000 0 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()