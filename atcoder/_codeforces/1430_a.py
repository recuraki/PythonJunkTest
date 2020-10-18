import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        q = int(input())
        for _ in range(q):
            n = int(input())
            can = False
            for i in range(1000):
                newn = n - 7 * i
                if newn < 0:
                    break
                for j in range(1000):
                    newn2 = newn - 5 * j
                    if newn2 < 0:
                        break
                    if newn2 % 3 == 0:
                        k = newn2 // 3
                        print(k, j, i)
                        can = True
                    if can:
                        break
                if can:
                    break

            if can is False:
                print(-1)


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
        input = """40
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4"""
        output = """2 2 2
7 5 3
-1
0 0 2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()