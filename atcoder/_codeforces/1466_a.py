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
        d = dict()
        for i in range(n):
            for j in range(i+1, n):
                d[abs(dat[i] - dat[j])] = True
        print(d)
        print(d.keys())
        print(len(list(d.keys())))


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
        input = """8
4
1 2 4 5
3
1 3 5
3
2 6 8
2
1 2
1
50
5
3 4 5 6 8
3
1 25 26
6
1 2 4 8 16 32"""
        output = """4
2
3
1
0
5
3
15"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()