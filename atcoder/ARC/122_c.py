import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    ox = int(input())
    for z in range(2, 1000000):
        l = []
        x = ox
        y = z ** int(math.log(x, z)-1)
        for i in range(130):
            # print(x, y, bin(x), bin(y))
            if x == 0 and y == 0:
                break
            if (x + y) < (130 - i) and x > 0:
                inst = 1
            elif (x + y) < (130 - i) and y > 0:
                inst = 2
            elif x > y:
                inst = 3
            elif x < y:
                inst = 4
            l.append(inst)
            if inst == 1:
                x -= 1
            if inst == 2:
                y -= 1
            if inst == 3:
                x = x - y
            if inst == 4:
                y = y - x
        #print(x, y)
        if x == 0 and y == 0:
            break
    if l == None:
        assert False
    print(len(l))
    for x in l:
        print(x)


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
        input = """4"""
        output = """5
1
4
2
3
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()