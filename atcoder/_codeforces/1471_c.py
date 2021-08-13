import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    def do():
        n, m = map(int, input().split())
        dat = list(map(lambda x: int(x) - 1, input().split()))
        datc = list(map(int, input().split()))
        dat.sort(reverse=True)
        #print(dat)
        canuse = 0
        res = 0
        for i in range(n):
            #print(i, "need", dat[i])
            if canuse < dat[i]:
                #print("present", canuse, "cost", datc[canuse])
                res += datc[canuse]
                canuse += 1
                continue
            #print("present nothing", "cost", datc[dat[i]])
            res += datc[dat[i]]
        print(res)
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
        input = """2
5 4
2 3 4 3 2
3 5 12 20
5 5
5 4 3 2 1
10 40 90 160 250"""
        output = """30
190"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
1 1
1
1"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()