import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))

    def do():
        class BinaryIndexTreeSum:
            #
            # BE
            #
            def __init__(self, n):
                self.size = n
                self.tree = [0] * (n + 1)

            def sum(self, i):
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & -i
                return s

            def add(self, i, x):
                while i <= self.size:
                    self.tree[i] += x
                    i += i & -i

        class Solution:
            def countTriplets(self, nums):
                N = 1000000
                bitLeft = BinaryIndexTreeSum(1000000)
                bitRight = BinaryIndexTreeSum(1000000)
                ans = 0
                for val in nums:
                    bitLeft.add(val, 1)
                for i in range(len(nums) - 1, -1, -1):
                    # center val = nums[i]
                    valC = nums[i]
                    numSmaller = bitLeft.sum(valC - 1)
                    numGreater = bitRight.sum(N) - bitRight.sum(valC)
                    # print(i, numSmaller, numGreater)
                    ans += numSmaller * numGreater
                    # leave this [i] val
                    bitLeft.add(valC, -1)
                    bitRight.add(valC, 1)
                return (ans)

        n = int(input())
        dat = list(map(int, input().split()))
        dat.sort()
        st = Solution()
        print(st.countTriplets(dat))
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
        input = """4
3 1 4 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
99999 99998 99997 99996 99995 99994 99993 99992 99991 99990"""
        output = """120"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """15
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9"""
        output = """355"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()