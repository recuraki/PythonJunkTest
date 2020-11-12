
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    def do():
        l, r = map(int, input().split())
        if l <3 or r < 3:
            print("NO")
            return
        ool, oor = l, r
        l *= 3
        r *= 3
        x = l // 3 * 2
        #print(l, r, x)
        if (r-l) < (x//2):
            print("YES")
            return

        l, r = ool, oor
        x = r + 1
        if x/2 < r:
            print("YES")
            return

        print("NO")

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
        input = """3
3 4
1 2
120 150"""
        output = """YES
NO
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()