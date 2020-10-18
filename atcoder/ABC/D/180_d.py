import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x,y,a,b = map(int,input().split())
    res = 0
    while True:
        #print(x,y,a,b)
        if x >= y:
            break
        if x*a < x+b:
            #print("multi")
            if (x * a) >= y:
                break
            x *= a
            res += 1
        else:
            #print("plus")
            val = min( (x*a) , y) - x
            cnt = val // b
            if cnt < 1:
                break
            #print("cnt", cnt)
            x += b * cnt
            res += cnt
            if cnt == 1:
                if x == y:
                    x -= b
                    res -= 1
                    break
            if x == y:
                x-=b
                res -= 1

            if cnt < 1:
                break
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
        input = """4 20 2 10"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1000000000000000000 10 1000000000"""
        output = """1000000007"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()