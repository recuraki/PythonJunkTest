# 点p1 と 点p2で結ばれる線分に対して y軸 = yの直線の交点が存在するかを識別し、交点座標を返す
def isCross(y, p1, p2):
    #print("{0},{1},{2}".format(y, p1, p2))
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    if y1 > y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    if y2 - y1 == 0:
        return (False, None)
    cx = (x1 * (y2 - y) + x2 * (y - y1)) / (y2 - y1)
    cy = y
    if y1 <= y and y < y2:
        return (True, [cx, cy])
    else:
        return (False, None)


print(isCross(0.5, [1, 2], [1,0])) #(True, [1.0, 0.5])
print(isCross(0.5, [0,1], [1,0])) #(True, [0.5, 0.5])
print(isCross(0.5, [0,2], [1,0])) #(True, [0.75, 0.5])
print(isCross(3, [0,2], [0,0]))   #(False, None)
print(isCross(0, [-100, -100], [100, -100])) #(False, None)




# [x,y]で与えられる3直線が同一線上にあるか？
# Verify: https://atcoder.jp/contests/abc181/tasks/abc181_c
def sameLine(p1, p2, p3):
    return (p3[0] - p1[0]) * (p2[1] - p1[1]) == (p2[0] - p1[0]) * (p3[1] - p1[1]) and \
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 < (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2

# 2つの直線が交わるかの判定 p=[x,y]のp1-p2を繋ぐ線とp3-p4を繋ぐせんを調べる
def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1 * tc2 < 0 and td1*td2 < 0

print("Inter")
print(intersect([0, 0], [0, 1], [-1, 0.5], [1, 0.5])) # True
print(intersect([0, 0], [0, 1], [0, 0], [0, 1])) # False(被る)



# ある点が凸多角形内に存在するかを判定する
# p = (x, y)の座標
# poly = [(x1, y1), (x2, y2)...]
# http://uchigle.cocolog-nifty.com/blog/2008/11/post-3a38.html
# http://www.not-enough.org/abe/manual/argo/poly-naibu.html
def isPointInPolygon(p, poly):
    isInside = False
    tx, ty = p[0], p[1] # target x, y
    lp = poly[-1]
    for cp in poly:
        #print("{0} - {1} cross y={2}".format(lp, cp, ty))
        resCross, pCross = isCross(ty, lp, cp)
        if resCross:
            # 交点が存在する場合、それが自分より右側かを判定する
            if pCross[0] > tx:
                isInside = not isInside
        lp = cp
    return isInside


# http://py3.hateblo.jp/entry/2014/03/07/172910
"""
poly = [[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]
>>> print(list(polyToTriangle(poly)))
[([4, 1], [3, 4], [3, 7]), ([4, 1], [3, 7], [4, 8]), ([4, 1], [4, 8], [7, 9]), ([4, 1], [7, 9], [9, 6]), ([4, 1], [9, 6], [7, 1])]
>>> print(areaPoly(poly))
35.5
"""
def polyToTriangle(poly):
    # ポリゴンを三角形に分割します。
    for i in range(len(poly) - 2):
        yield poly[0], poly[i + 1], poly[i + 2]
def areaTriangle(pointsTriangle):
    # 三点から面積を求める
    (x1, y1), (x2, y2), (x3, y3) = pointsTriangle
    return abs((x1 - x3) * (y2 - y1) - (x1 - x2) * (y3 - y1)) / 2
def areaPoly(data):
    # 任意のポリゴンの面積を求める
    return sum(areaTriangle(tri) for tri in polyToTriangle(data))

poly = [[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]
print(list(polyToTriangle(poly)))
print(areaPoly(poly))

poly = [ [-100, -100], [100, -100], [100, 100], [-100, 100] ]
print("ok" if isPointInPolygon([0,0], poly) else "ng")
print("ok" if isPointInPolygon([99, 99], poly) else "ng")
print("ok" if not isPointInPolygon([101, 101], poly) else "ng")
print("ok" if not isPointInPolygon([80, -101], poly) else "ng")
print("ok" if isPointInPolygon([0, -100], poly) else "ng")
poly = [ [0, 0], [200, 0], [200, 200], [0, 200] ]
print("ok" if isPointInPolygon([100, 0], poly) else "ng")



