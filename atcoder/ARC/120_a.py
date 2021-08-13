
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
        # 累積和
        import itertools
        # 注意: あくまで、bは開区間
        squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)

        def createSDAT(l):
            return list(itertools.accumulate(itertools.chain([0], l)))

        n = int(input())
        dat = list(map(int, input().split()))
        sdat = createSDAT(dat)
        total = 0
        mm = -1
        for i in range(n):
            total += squery(0, i + 1)
            mm = max(mm, dat[i])
            print(total + mm*(i+1))



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
1 2 3"""
        output = """2
8
19"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
1"""
        output = """2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()