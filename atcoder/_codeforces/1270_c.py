import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
def test():
    l = [1, 2, 3, 4, 5, 5, 16, 2, 2]  # 20, 8
    l = [3, 4, 5, 2, 6, 12, 32, 10, 10]  # 64, 84 -> 21,14
    l = [5, 4, 2, 4, 5, 6, 32, 7, 7]  # 42, 40 -> 21,14
    l = [3, 3, 4, 5, 6, 17]  # 37,46 -> 21,14
    l = [1, 1, 2]  # 37,46 -> 21,14
    l = [1, 1, 4, 1, 1]  # 37,46 -> 21,14
    cur = 0
    for x in range(len(l)):
        cur ^= l[x]
    print(sum(l))
    print(2 * cur)

def resolve():

    import sys
    #input = sys.stdin.readline


    from pprint import pprint
    def do():
        n = int(input())
        l = list(map(int, input().split()))
        cur = 0
        for x in range(len(l)):
            cur ^= l[x]
        ss = sum(l)
        xx = 2 * cur
        diff = abs(ss-xx)
        #print(diff)
        if diff == 0:
            print(0)
            print()
            return
        import math
        a = 2 ** math.ceil(math.log2(ss) + 1)
        if diff &1 == 1:
            a += 1
        res = [a]
        l.append(a)
        cur = 0
        for x in range(len(l)):
            cur ^= l[x]
        ss = sum(l)
        xx = 2 * cur
        diff = abs(ss-xx)
        if diff == 0:
            print(1)
            print(res[0])
            return
        print(3)
        print(res[0], diff//2, diff//2)

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
        input = """3
4
1 2 3 6
1
8
2
1 1"""
        output = """0

2
4 4
3
2 6 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """1
6
3 4 5 2 6 12
"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()