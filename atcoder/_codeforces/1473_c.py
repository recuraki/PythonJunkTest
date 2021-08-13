import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    
    from pprint import pprint
    import sys
    def do():
        n, k = map(int, input().split())
        diff = n - k
        p = []
        for i in range(k - diff - 1):
            p.append(i + 1)
        for i in range(diff + 1):
            p.append(k - i)
        print(" ".join(list(map(str, p))))

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
        input = """4
1 1
2 2
3 2
4 3"""
        output = """1
1 2
2 1
1 3 2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()