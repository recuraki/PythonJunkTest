import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    def isparad(s):
        for i in range(len(s)):
            if s[i] == s[len(s)-1-i]:
                continue
            return False
        return True
    s = input()
    can = False
    for i in range(100):
        t = ("0" * i) + s
        if isparad(t):
            can = True
            break
    print("Yes" if can else"No")



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
        input = """1210"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """777"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """123456789"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()