import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n,m = map(int, input().split())
        need = False
        if n % 2 == 0 or m % 2 == 0:
            need = True
        for i in range(n):
            s = ""
            for j in range(m):
                if (i % 2 + j % 2) % 2 == 0:
                    s += "B"
                else:
                    if need:
                        s += "B"
                        need = False
                    else:
                        s += "W"
            print(s)




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
3 2
3 3
1 1
2 2
1 5
5 1
1 4
4 1"""
        output = """BW
WB
BB
BWB
BWW
BWB"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()