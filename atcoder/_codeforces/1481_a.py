import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    def do():
        x, y = map(int, input().split())
        s = input()
        if x < 0:
            s = s.replace("R", "_")
            s = s.replace("L", "R")
            s = s.replace("_", "L")
            x = -x
        if y < 0:
            s = s.replace("U", "_")
            s = s.replace("D", "U")
            s = s.replace("_", "D")
            y = -y
        cntx = s.count("R")
        cnty = s.count("U")
        #print(x, y)
        #print(cntx, cnty)
        if cntx == x and cnty == y:
            print("YES")
            return
        if cntx < x or cnty < y:
            print("NO")
            return
        print("YES")



    q = int(input())
    for _ in range(q):
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
        input = """6
10 5
RRRRRRRRRRUUUUU
1 1
UDDDRLLL
-3 -5
LDLDLDDDR
1 2
LLLLUU
3 -2
RDULRLLDR
-1 6
RUDURUUUUR"""
        output = """YES
YES
YES
NO
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()