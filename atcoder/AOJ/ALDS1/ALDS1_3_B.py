import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    d = collections.deque([])
    n, p = map(int, input().split())
    for i in range(n):
        name, t = input().split()
        d.append((name, int(t)))
    tt = 0
    while len(d) > 0:
        name, t = d.popleft()
        if t <= p:
            tt += t
            print("{0} {1}".format(name, tt))
        elif t > p:
            t = t - p
            tt += p
            d.append((name, t))

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
        input = """5 100
p1 150
p2 80
p3 200
p4 350
p5 20"""
        output = """p2 180
p5 400
p1 450
p3 550
p4 800"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()