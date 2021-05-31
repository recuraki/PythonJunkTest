
"""
1 2 3 4 5 6 [1,2,3] [3,4,5] のとき、3を中央値
1 2 3 4 5 のときも3を中央値にする
■工夫1: lを大きいか同じにする
L側の一番大きいのを中央値にしたい
 偶数の時、[1,2,3] [4,5,6] (バランス)
 奇数の時、[1,2,3] [4,5] (Lが+1までOK)
■工夫2: とりあえずlに突っ込む
 [1,2,3,10], [4,5,6] などにしてから、l,rをswapして、
 [1,2,3,4], [5,6,10] にすればいい(swap=互いにpop,push)
"""
from heapq import heappop, heappush, heapify,heapreplace
l, r = [], []
# どんどん値を追加していきながら、中央値を-l[0]にする。
def addmedianq(x):
    heappush(l, -x) # とりあえず足す
    if ( len(l) + len(r) ) % 2 == 0:
        if len(l) > len(r):
            x = -heappop(l)
            heappush(r, x)
    else:
        if len(l) > (len(r)+1):
            x = -heappop(l)
            heappush(r, x)
    if len(r) == 0: return
    if (-l[0]) > r[0]:
        x, y = -heappop(l), heappop(r)
        heappush(r, x)
        heappush(l, -y)
getmedianq = lambda : -l[0]

addq = [1,5,3,-2,10,10,10,10,10]
res = []
for x in addq:
    addmedianq(x)
    res.append(getmedianq())
print(res) # [1, 1, 3, 1, 3, 3, 5, 5, 10]
