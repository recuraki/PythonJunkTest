import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    #input = sys.stdin.readline
    from pprint import pprint
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        num1 = dat.count(1)
        num2 = dat.count(2)
        if num2 % 2 == 0: # same
            if num1 % 2 == 0:
                print("YES")
                return
            print("NO")
            return
        else: # each over 2
            if num1 < 2:
                print("NO")
                return
            num1 -= 2
            if num1 % 2 == 0:
                print("YES")
                return
            print("NO")
            return
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
        input = """5
2
1 1
2
1 2
4
1 2 1 2
3
2 2 2
3
2 1 2"""
        output = """YES
NO
YES
NO
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()