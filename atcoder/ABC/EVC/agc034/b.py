import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = list(input())
    c = 0
    state = 0
    res = 0
    stack = 0
    loop = 0
    while c < len(s):
        """
        loop = loop + 1
        if loop > 100:
            break
        print("c" + str(c))
        print("cur: " + "".join(s))
        print("state" + str(state))
        """
        if state == 0:
            if s[c] == "A":
                state = 1
                stack = 0
        elif state == 1:
            if s[c] == "B":
                state = 2
            else:
                if s[c] == "A":
                    state = 1
                    stack += 1
                    #print("stack up:" + str(stack))
                else:
                    state = 0
                    stack = 0
        elif state == 2:
            if s[c] == "C":
                #print("hit")
                #print(" stack:" + str(stack))
                res += 1 + stack
                s[c-2-stack], s[c-1-stack], s[c-stack] = "B", "C", "A"
                for i in range(stack):
                    s[c-i] = "A"
                c = c - 3 - stack
                state = 0
                stack = 0
                if s[c] == "A":
                    state = 1
                    stack = 0
            else:
                state = 0
                stack = 0
                if s[c] == "A":
                    state = 1
                    stack = 0
        c = c + 1
    print(res)


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
        logging.info("test_input_1")
        input = """ABCABC"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """C"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """ABCACCBABCBCAABCB"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()