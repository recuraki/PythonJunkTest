import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
"""
サンプル2:
5 11
3 7 2 5 11 6 1 9 8 10 4

ふつうはまず最初に
3 7 2 5 11
 ->
2 3 5 7 11
 ->2

3 5 6 7 11
 ->3
問題文では、「順番に追加していく」ですが、この解法では、inputを「逆から消していく」とします
[1,2,3,4,5,6,7,8,9,10,11]

[1,2,3,4,5,6,7] [8,9,10,11]
erased = {}

>input 4
 [1,2,3,4,5,6,7] [8,9,10,11]
 erased = {4} (に追加するのはO(1)
 もしも、del leftqueue.(leftqueue.index(4))すると、O(N)

この状態で、
leftqueue.pop() -> [1,2,3,4,5,6]
leftqueue.pop() -> [1,2,3,4,5]
leftqueue.pop() -> [1,2,3,4]
 ここで、
leftqueue.pop() -> [1,2,3,!!4!!] -> erasedなので、無視して
leftqueue.pop() -> [1,2,3]



[1,2,3,5,6,7] [8,9,10,11]
>10
[1,2,3,5,6] [7,8,9,11]
>8
[1,2,3,5] [6,7,9,11]

[2,3,5] [6,7,9,11]
でも、listに対するeraseという処理は、O(N)かかるので、eraseをsetして管理します。

[1,2,3,4,5,6,7] [8,9,10,11]
  erase 5 (遅延評価する 削除した
pop()



l = [1,2,3]
l.pop()
 = 3で、lが[1,2]になる O(1)
l.pop()
 = 2で、lが[1]になる O(1)

l.append(100)
 = [1,100]になるO(1)
"""
    def do():
        # O(N)
        # 問題文では、「順番に追加していく」ですが、この解法では、inputを「逆から消していく」とします
        # exampleの 11, 5のとき、 [1,2,3,4,5,6,7] [x,x,x,x]に最終的になります。これが基本的な考え方です。
        # もし、xのどれかが最初消されたら、 [1,2,3,4,5,6] [7,x,x,x] になりますし、
        # もし、7以下の数が消されたら、    [1,2,3,5,6,7] [x,x,x,x]になります。
        # でも、listに対するeraseという処理は、O(N)かかるので、eraseをsetして管理します。
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        buf = list(range(1, (n - k + 1) + 1)) # [1,2,3,4,5,6,7]を作ります
        erased = set() # 消した数を管理します。
        resrev = []
        for x in list(reversed(dat[k:])): # 逆に見ていきます
            resrev.append(buf[-1])
            if x > buf[-1]:
                buf.pop()
            erased.add(x)
            while buf[-1] in erased: buf.pop()
        resrev.append(buf[-1])
        for x in reversed(resrev):
            print(x)
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
        input = """3 2
1 2 3"""
        output = """1
2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """11 5
3 7 2 5 11 6 1 9 8 10 4"""
        output = """2
3
3
5
6
7
7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()