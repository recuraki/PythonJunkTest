import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from heapq import heapify,heappop,heappush
    def do():
        n = int(input())
        dat = list(map(int, input().split()))z
        qeven = []
        qodd = []
        for i in range(n):
            if dat[i] &1 == 0:
                heappush(qeven, -dat[i])
            else:
                heappush(qodd, -dat[i])
        a = 0
        b = 0
        turnAlice = True
        while True:
            if len(qodd) == 0 and len(qeven) == 0:
                break
            o, e = 0,0
            if len(qodd) != 0:
                o = -heappop(qodd)
                heappush(qodd, -o)
            if len(qeven) != 0:
                e = -heappop(qeven)
                heappush(qeven, -e)
            #print(qeven, qodd, o, "vs", e)
            if o > e:
                _ = heappop(qodd)
                if turnAlice is False:
                    b += o
            else:
                _ = heappop(qeven)
                if turnAlice is True:
                    a += e
            turnAlice = not turnAlice
        if a == b:
            print("Tie")
        elif a > b:
            print("Alice")
        else:
            print("Bob")


    q = int(input())
    for _ in range(q):
        do()
    # do()


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
4
5 2 7 3
3
3 2 1
4
2 2 2 2
2
7 8"""
        output = """Bob
Tie
Alice
Alice"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()