import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    def do():
        INF = 2 * 10**18

        n, m = map(int, input().split())
        buf_balance=[]
        buf_unbalance=[]
        needwire = n - 1
        unbalance_min_cost = INF
        costlist = []
        for i in range(m):
            a, c = map(int, input().split( ))
            costlist.append(c)
            if n % a == 0:
                buf_balance.append( (a,c) )
            else:
                unbalance_min_cost = min(unbalance_min_cost, c)
                buf_unbalance.append( (a,c) )

        res = INF

        for a, c in buf_unbalance:
            cost = c * needwire
            res = min(res, cost)

        for a, c in buf_balance:
            needunbalancewire = a - 1
            needbalancewire = needwire - needunbalancewire

            cost = c * needbalancewire + unbalance_min_cost * needunbalancewire
            res = min(res, cost)

        if res >= 10** 18 + 1000:
            print(-1)
            return
        print(res)
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
        input = """4 2
2 3
3 5"""
        output = """11"""
        #self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 1
3 4"""
        output = """-1"""
        #self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """6 1
2 1
3 1000"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()