import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from copy import deepcopy
    a, b = input().split()
    oa = list(a)
    ob = list(b)
    res = []
    a = deepcopy(oa)
    b = deepcopy(ob)
    res.append(int("".join(a)) - int("".join(b)))
    a = deepcopy(oa)
    b = deepcopy(ob)
    a[0] = "9"
    res.append(int("".join(a)) - int("".join(b)))
    a = deepcopy(oa)
    b = deepcopy(ob)
    b[0] = "1"
    res.append(int("".join(a)) - int("".join(b)))
    a = deepcopy(oa)
    b = deepcopy(ob)
    a[1] = "9"
    res.append(int("".join(a)) - int("".join(b)))
    a = deepcopy(oa)
    b = deepcopy(ob)
    b[1] = "0"
    res.append(int("".join(a)) - int("".join(b)))
    a = deepcopy(oa)
    b = deepcopy(ob)
    a[2] = "9"
    res.append(int("".join(a)) - int("".join(b)))
    a = deepcopy(oa)
    b = deepcopy(ob)
    b[2] = "0"
    res.append(int("".join(a)) - int("".join(b)))
    a = deepcopy(oa)
    b = deepcopy(ob)
    print(max(res))



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """567 234"""
        output = """733"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """999 100"""
        output = """899"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """100 999"""
        output = """-99"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()