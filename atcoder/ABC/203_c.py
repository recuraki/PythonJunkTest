import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    from heapq import heappop, heappush
    e = []
    heappush(e,  (0, k) )
    for i in range(n):
        a, b = map(int, input().split())
        heappush(e,  (a, b) )
    res = 0
    while len(e) > 0:
        time, powerup = heappop(e)
        if res < time:
            break
        prev = time
        res += powerup
    print(res)




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
        input = """2 3
2 1
5 10"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 1000000000
1 1000000000
2 1000000000
3 1000000000
4 1000000000
5 1000000000"""
        output = """6000000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 2
5 5
2 1
2 2"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()