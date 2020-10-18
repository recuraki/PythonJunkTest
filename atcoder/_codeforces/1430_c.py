import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        from collections import deque
        import math
        q = int(input())
        for _ in range(q):
            n = int(input())
            odd = deque(reversed(list(range(1, n+1, 2))))
            even = deque(reversed(list(range(2, n+1, 2))))
            #print(odd,even)
            operation = []
            while len(odd) + len(even) != 1:
                if len(even) > 1:
                    a = even.popleft()
                    b = even.popleft()
                elif len(odd) > 1:
                    a = odd.popleft()
                    b = odd.popleft()
                elif len(odd) == 1:
                    a = odd.popleft()
                    b = even.popleft()
                else: # odd == 0
                    a = even.popleft()
                    b = even.popleft()
                operation.append([a,b])
                x = math.ceil((a+b) / 2)
                #print(a,b)
                #print(x)
                if x & 1 == 0: # even
                    even.appendleft(x)
                else:
                    odd.appendleft(x)
            if len(even) > 0:
                print(even.popleft())
            else:
                print(odd.popleft())
            for i in range(n-1):
                a,b = operation[i]
                print(a,b)
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
        input = """1
4"""
        output = """2
2 4
3 3
3 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()