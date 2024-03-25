import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, c = map(int, input().split())
        ops = [[] for _ in range(32)]
        cur = c

        def f(opnum, sft):
            if opnum == 0:
                ops[sft] = [0]
            elif opnum == 1:
                ops[sft].append(1)
            elif opnum == 2:
                pass
            elif opnum == 3:
                ops[sft] = [3]
            elif opnum == 4:
                pass
            elif opnum == 5:
                ops[sft].append(5)
            while len(ops[sft]) > 1:
                op2 = ops[sft].pop()
                op1 = ops[sft].pop()
                if op1 == op2 == 1:
                    ops[sft].append(1) # AND 1 AND 1 -> AND 1
                    continue
                if op1 == op2 == 5:
                    # NOT NOT -> nothing
                    continue
                if op1 == 1 and op2 == 5:
                    ops[sft].append(5)
                    continue
                if op2 == 1 and op1 == 5:
                    ops[sft].append(5)
                    continue

                ops[sft].append(op1)
                ops[sft].append(op2)
                break




        for _ in range(n):
            #print(ops)
            ans = 0
            op, x = map(int, input().split())

            for sft in range(31): # bit目を得る

                b = (x >> sft) & 1 # sftbit目の値
                if False:
                    assert False
                elif op == 1 and b == 0: f(0, sft) # AND 0 # set 0
                elif op == 1 and b == 1: f(1, sft) # AND 1 # CHECK 1
                elif op == 2 and b == 0: f(2, sft) # OR 0 # nothing
                elif op == 2 and b == 1: f(3, sft) # OR 1 # set 1
                elif op == 3 and b == 0: f(4, sft) # XOR 0 # nothing
                elif op == 3 and b == 1: f(5, sft) # XOR 1 = NOT
                curbit = (cur >> sft) & 1
                #print(" ", sft, curbit)
                for opnum in ops[sft]:
                    if False: pass
                    elif opnum == 0: curbit = 0
                    elif opnum == 1: curbit&= 1
                    elif opnum == 2: pass
                    elif opnum == 3: curbit = 1
                    elif opnum == 4: pass
                    elif opnum == 5: curbit^= 1
                    #print("op", opnum)
                curbit &= 1
                #print("a", sft, curbit)
                ans |= (curbit << sft)
            #print("r", ops)
            print(ans)
            cur = ans
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
        input = """3 10
3 3
2 5
1 12"""
        output = """9
15
12"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """9 12
1 1
2 2
3 3
1 4
2 5
3 6
1 7
2 8
3 9"""
        output = """0
2
1
0
5
3
3
11
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()