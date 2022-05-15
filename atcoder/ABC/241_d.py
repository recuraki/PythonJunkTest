import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline

    def do():
        q = int(input())
        querys = []
        from collections import defaultdict
        nums = defaultdict(int)
        for _ in range(q):
            ll = list(map(int, input().split()))
            querys.append( ll )
            if ll[0] == 1:
                nums[ll[1]] += 1
            else: # query 2,3
                pass

        # nums = 先よみしたやつ

        keys = list(nums.keys())
        keys.sort()

        # window とは、平方分割した窓のこと
        windowlr = [] # それぞれの窓が含むl, r (inclucive)
        windowsize = math.ceil(math.sqrt(len(keys))) # １つの枠のサイズは最高でkeys
        print(keys)
        print(windowsize)
        for i in range(math.ceil(len(keys) / windowsize)):
            l = keys[i*windowsize]
            r = keys[min(len(keys) -1, (i+1)*windowsize - 1)]
            windowlr.append( [l, r] )
        print(windowlr)





    # 1 time
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
        input = """11
1 20
1 10
1 30
1 20
3 15 1
3 15 2
3 15 3
3 15 4
2 100 5
1 1
2 100 5"""
        output = """20
20
30
-1
-1
1"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_1")
        input = """11
1 1
1 2 
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
1 11"""
        output = """20
20
30
-1
-1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()