import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    import collections
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n = int(input())
        dat = list(map(int, input().split()))
        dat = collections.deque(dat)

        cnt = 0
        alice, bob = 0,0
        prevEat = 0
        isAliceTurn = True

        while len(dat) > 0:
            cnt += 1
            #print("Turn:{0} Prev:{1} IsAlice:{2}, A{3}, B{4}".format(cnt, prevEat, isAliceTurn, alice, bob))
            canEat = False
            curEat = 0
            while len(dat) > 0:
                if isAliceTurn:
                    xx = dat.popleft()
                    #print("> Alice: ", xx)
                    curEat += xx
                else:
                    xx = dat.pop()
                    #print("> Bob: ", xx)
                    curEat += xx
                if curEat > prevEat:
                    prevEat = curEat
                    canEat = True
                    break

            if isAliceTurn:
                alice += curEat
            else:
                bob += curEat

            if canEat is False:
                break

            isAliceTurn = not isAliceTurn

        print(cnt, alice, bob)





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
        input = """1
12
5 8 10 1 1 10 7 3 12 3 3 7"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()