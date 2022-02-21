import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from collections import deque
    S = deque(list(input()))
    # STEP1: L,Rが同じ文字なら全部削る (残りは""  か  回文 + "aaa...")
    while len(S) >= 2 and S[0] == S[-1]: S.pop(), S.popleft()
    # STEP2: Rが"a"である分には削る  (回文 + "aaa..."のaを削りたい)
    while len(S) > 0 and S[-1] == "a": S.pop()
    # STEP3: 回文か確認すればいい
    while len(S) >= 2:
        if S[0] == S[-1]:
            S.pop(), S.popleft()
            continue
        print("No")
        exit(0)
    print('Yes')



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
        input = """kasaka"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """atcoder"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """php"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """aaabddbaaaa"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_312(self):
        print("test_input_31")
        input = """aaaaaa"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_311(self):
        print("test_input_311")
        input = """aaaaabddbaaaa"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3412(self):
        print("test_input_31")
        input = """aaafaaa"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_3411(self):
        print("test_input_311")
        input = """aaaaabdfdbaaaa"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()