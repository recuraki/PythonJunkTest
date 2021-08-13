import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n = int(input())
        for i in range(1, 10010):
            nokori = n - (i*i*i)
            if nokori < 1:
                break
            can = int((nokori ** (1/3)))
            can -= 1
            if can != 0 and nokori == can * can * can:
                print("YES")
                return
            can += 1
            if nokori == can * can * can:
                print("YES")
                return
            can += 1
            if nokori == can * can * can:
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
        input = """7
1
2
1000000000001
34
35
16
703657519796"""
        output = """NO
YES
NO
NO
YES
YES
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()