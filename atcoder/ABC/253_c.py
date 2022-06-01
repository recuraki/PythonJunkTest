"""
削除つきPQ
pythonのheapqを利用して削除をO(1)で行います(予約します)

init: initlist = []
front: 最小値をgetする。ただし、削除フラグが付いているものはスキップ
pop: 最小値をpopする。(front()して、popする)
push: 値を入れる
erase: 削除を予約する。(pop字に消される)
count(x): このqに含まれているxの数を答える(削除予約分は引かれる)
__len__: 削除文を引いた長さ
制約：eraseする文字列は確実に含まれているものでないといけない
"""
from heapq import heappop, heappush, heapify
from collections import defaultdict
from copy import deepcopy

class exhanceHeapq():
    def __init__(self, initlist=[]):
        self.containDict = defaultdict(int)
        self.willdeleteDict = defaultdict(int)
        self.willdeletelen = 0
        self.q = deepcopy(initlist)
        heapify(initlist)
        for x in initlist: self.containDict[x] += 1

    def front(self):
        while len(self.q) > 0:
            candidate = self.q[0]
            assert self.willdeleteDict[candidate] >= 0
            if self.willdeleteDict[candidate] > 0:
                heappop(self.q)
                self.containDict[candidate] -= 1
                self.willdeletelen -= 1
                self.willdeleteDict[candidate] -= 1
            else:
                return candidate
        assert False  # NOT REACH

    def pop(self):
        ret = self.front()
        heappop(self.q)
        self.containDict[ret] -= 1
        return ret

    def push(self, x):
        heappush(self.q, x)
        self.containDict[x] += 1

    def __len__(self):
        return len(self.q) - self.willdeletelen

    def erase(self, x):
        assert self.containDict[x] > 0
        self.willdeletelen += 1  # will delete
        self.willdeleteDict[x] += 1

    def count(self, x):
        return self.containDict[x] - self.willdeleteDict[x]

"""
削除つきmax/min を得られるPQ
exhanceHeapqを2つ用意して使って


init: initlist = []
popMin, popMax: min/maxを得てその要素を消す
getMin, getMax: min/maxを得てその要素を得るだけ(消さない)
push: 値を入れる
erase: 削除を予約する。(pop字に消される)
count(x): このqに含まれているxの数を答える(削除予約分は引かれる)
__len__: 削除文を引いた長さ
制約：eraseする文字列は確実に含まれているものでないといけない
"""
class minmaxQueue:
    def __init__(self, initlist=[]):
        self.minQ = exhanceHeapq(initlist)
        self.maxQ = exhanceHeapq([])
        for x in initlist: self.maxQ.push(-x)

    def popMin(self):
        x = self.minQ.pop()
        self.maxQ.erase(-x)
        return x

    def popMax(self):
        x = -self.maxQ.pop()
        self.minQ.erase(x)
        return x

    def getMin(self):
        return self.minQ.front()

    def getMax(self):
        return -self.maxQ.front()

    def push(self, x):
        self.minQ.push(x)
        self.maxQ.push(-x)

    def __len__(self):
        return len(self.minQ)

    def erase(self, x):
        self.minQ.erase(x)
        self.maxQ.erase(-x)

    def count(self, x):
        return self.minQ.count(x)

q = int(input())
mmq = minmaxQueue()
for _ in range(q):
    l = list(map(int, input().split()))
    if l[0] == 1: mmq.push(l[1])
    elif l[0] == 2:
        x, c = l[1], l[2]
        for _ in range(min(c, mmq.count(x))):
            mmq.erase(x)
    elif l[0] == 3:
        print(mmq.getMax() - mmq.getMin())
