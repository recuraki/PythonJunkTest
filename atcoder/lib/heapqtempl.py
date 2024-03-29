

"""
削除つきPQ
init: initlist = []
pop: 最小値をとる。ただし、削除フラグが付いているものはスキップ
push: 値を入れる
erase: 削除を予約する。(pop字に消される)
len: 削除文を引いた長さ
制約：eraseする文字列は確実に含まれているものでないといけない
"""
from heapq import heappop, heappush, heapify
from collections import defaultdict
class exhanceHeapq():
    containDict = defaultdict(int)
    willdeleteDict = defaultdict(int)
    willdeletelen = 0
    def __init__(self, initlist = []):
        self.q = initlist
        heapify(initlist, )
        for x in initlist: self.containDict[x] += 1

    def pop(self):
        while len(self.q) > 0:
            candidate = heappop(self.q)
            assert self.willdeleteDict[candidate] >= 0
            self.containDict[candidate] -= 1
            if self.willdeleteDict[candidate] > 0:
                self.willdeletelen -= 1
                self.willdeleteDict[candidate] -= 1
            else: return candidate
        assert False # NOT REACH

    def push(self, x):
        heappush(self.q, x)
        self.containDict[x] += 1

    def len(self):
        return len(self.q) - self.willdeletelen

    def erase(self, x):
        assert self.containDict[x] > 0
        self.willdeletelen += 1 # will delete
        self.willdeleteDict[x] += 1

q = exhanceHeapq([(1,2), (3,4), (1,2)])
q.erase((1,2))
print(q.pop())
print(q.pop())


q = exhanceHeapq([1,2,1,3,3,3,7,4,5])
print(q.len())
q.erase(4)
print(q.len())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.len())
q.erase(3)
print(q.len())




