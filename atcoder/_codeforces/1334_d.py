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
        pass

    s = input()
    a,b = map(int, input().split())
    dat = list(map(int, input().split()))


    dat = [1, 2, 3]
    dat.sort(re)
    print(" ".join(list(map(str, dat))))

    pass
    #sys.setrecursionlimit(100000)
    import math
    math.ceil(1.2)
    math.floor(1.2)
    round(1.2, 3)



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
2 1 3
3 3 6
99995 9998900031 9998900031"""
        output = """1 2 1 
1 3 2 3 
1 """
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()