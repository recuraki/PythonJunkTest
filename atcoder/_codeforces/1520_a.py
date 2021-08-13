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
        visited = set()
        n = int(input())
        s = input()
        p = None
        res = True
        for x in s:
            if x == p:
                continue
            p = x
            if p in visited:
                res = False
                break
            visited.add(p)
        print("YES" if res else "NO")


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
3
ABA
11
DDBBCCCBBEZ
7
FFGZZZY
1
Z
2
AB"""
        output = """NO
NO
YES
YES
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()