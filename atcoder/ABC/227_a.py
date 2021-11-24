import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    n, k, a = map(int, input().split())
    ans = a - 1 # 0から初めて a-1番目の人がカードを持っています
    ans += (k - 1)  # k個進めます。ただし、、1枚目はa-1さんが持っているので"-1"します
    print( (ans % n) + 1) # これで円をシミュレートします


    """
    n, k, a = map(int, input().split())
    
    ans = a
    k -= 1
    for _ in range(k):
        ans += 1
        if ans == (n+1): ans = 1
    print(ans)
    """

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
        input = """3 3 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 100 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 14 2"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()