
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
        n, k = map(int, input().split())
        k += 0
        dat = [(1, 0)]
        from heapq import heapify, heappop, heappush
        erased = []
        used = []
        ans = - (10**64)
        for _ in range(n):
            op, y = map(int, input().split())
            dat.append( (op, y) )
        dat = list(reversed(dat))
        curval = 0
        if k == 0:
            curval = 0
            for op, y in reversed(dat):
                if op == 1:
                    curval = y
                if op == 2:
                    curval += y
            print(curval)
            return


        for op, y in dat:
            if k == -1: break
            if op == 2:
                curval += y
                heappush(used, y)
            if op == 1:
                #print("proc1", k, "era", erased, "use", used, curval)
                while len(erased) < k:
                    if len(used) > 0:
                        x = heappop(used)
                        if x >= 0:
                            heappush(used, x)
                            break
                        else:
                            curval -= x
                            heappush(erased, -x)
                    else:
                        break
                while len(erased) > 0 and len(used) > 0:
                    if -erased[0] > used[0]:
                        a = -heappop(erased)
                        b = heappop(used)
                        curval += a
                        curval -= b
                        heappush(erased, -b)
                        heappush(used, -a)
                    else: break
                while len(erased) > k:
                    x = heappop(erased)
                    x = -x
                    curval += x
                #print("proc1>", k, "era", erased, "use", used, curval)
                ans = max(ans, y + curval)
                k -= 1
        print(ans)

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
        input = """5 1
2 4
2 -3
1 2
2 1
2 -3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 0
2 -1000000000"""
        output = """-1000000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 3
2 3
2 -1
1 4
2 -1
2 5
2 -9
2 2
1 -6
2 5
2 -3"""
        output = """15"""
        self.assertIO(input, output)

    def test_input_31(self):
        print("test_input_31")
        input = """3 1
1 10
1 20
1 0
"""
        output = """20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()