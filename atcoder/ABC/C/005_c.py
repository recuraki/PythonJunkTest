import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from collections import deque
    t = int(input())
    nt = int(input())
    datt = deque(list(map(int, input().split())))
    nc = int(input())
    datc = deque(list(map(int, input().split())))
    f = True # 最終的には売れる、という期待
    while len(datc) > 0 and f == True:
        ct = datc.popleft() # 次の到着時間
        is_sell = False # この人に売ることができたか？
        for i in range(len(datt)): # 全部のたこ焼きを順番に取っていこうとする
            tt = datt.popleft() # 次のたこ焼きの到着時間
            if (tt > ct): # 待たせすぎ
                f = False
            elif tt == ct: # JIT
                is_sell = True
                break # このたこ焼きで決定
            elif (ct - tt) <= t: #間に合うなら
                is_sell = True
                break # このたこ焼きで決定
            else: # ふるいたこやき
                continue # 捨てて次のたこ焼きに進む
        if is_sell is False: # この人に売れなかったら
            f = False # 失敗
            break

    print("yes" if f else "no")




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
3
1 2 3
3
2 3 4"""
        output = """yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
3
1 2 3
3
2 3 5"""
        output = """no"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1
3
1 2 3
10
1 2 3 4 5 6 7 8 9 10"""
        output = """no"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1
3
1 2 3
3
1 2 2"""
        output = """no"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """2
5
1 3 6 10 15
3
4 8 16"""
        output = """yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()