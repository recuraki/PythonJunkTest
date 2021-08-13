import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():

    from pprint import pprint
    def do():
        import sys
        read = sys.stdin.read
        n, *indata = map(int, read().split())
        q = []
        offset = 0
        for _ in range(n):
            a, b = indata[offset], indata[offset+1]
            offset += 2
            q.append( (a, b) )
        from collections import deque
        q.sort(key=lambda x: x[1])
        #print(q)
        q = deque(q)
        buyedItems = 0
        spendGold = 0
        def buy(currentbuyeditem, currentwaribiki, willbuy):
            if currentbuyeditem >= currentwaribiki: return willbuy
            x2 = currentwaribiki - currentbuyeditem
            kau2 = min(x2, willbuy)
            res = 2 * kau2
            willbuy -= kau2
            return res + willbuy
        while len(q) > 0:
            curcnt, curwaribiki = q.popleft() # want to buy
            if buyedItems < curwaribiki: # cannot get waribiki
                # want to go curwaribiki
                want2buy = curwaribiki - buyedItems # hoshii!
                while len(q) > 0: # try right
                    if buyedItems >= curwaribiki: # mou OK!
                        break
                    nextcnt, nextwaribiki = q.pop() # from right
                    if nextcnt >= want2buy:
                        spendGold += buy(buyedItems, nextwaribiki, want2buy)
                        nextcnt = nextcnt - want2buy
                        buyedItems += want2buy
                        want2buy = 0
                        if nextcnt != 0:
                            q.append( (nextcnt, nextwaribiki) )
                        break # break
                    else: # nextcnt < curwaribiki
                        spendGold += buy(buyedItems, nextwaribiki, nextcnt)
                        want2buy -= nextcnt
                        buyedItems += nextcnt
            spendGold += buy(buyedItems, curwaribiki, curcnt)
            buyedItems += curcnt
        print(spendGold)

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
        input = """3
3 4
1 3
1 5"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
2 7
2 8
1 2
2 4
1 8"""
        output = """12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()