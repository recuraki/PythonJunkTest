def do(x, y, frx=False, fry=False):
    loopmax = x+1
    loop = 0
    rx = x
    ry = y
    cost = 99999999
    while True:
        if loop == loopmax:
            break
        f = False
        for j in range(loop):
            for i in range(loop):
                tx = x - i if frx is False else x
                ty = y - j if fry is False else y
                #print("try",tx, ty)
                if ty % tx == 0:
                    if cost > abs(x - tx) + abs(y - ty):
                        f = True
                        rx = tx
                        ry = ty
                        cost = abs(x - tx) + abs(y - ty)
                    break

            for i in range(loop):
                tx = x + i if frx is False else x
                ty = y - j if fry is False else y
                #print("try",tx, ty)
                if ty % tx == 0:
                    if cost > abs(x - tx) + abs(y - ty):
                        f = True
                        rx = tx
                        ry = ty
                        cost = abs(x - tx) + abs(y - ty)
                    break

            for i in range(loop):
                tx = x - i if frx is False else x
                ty = y + j if fry is False else y
                #rint("try",tx, ty)
                if ty % tx == 0:
                    if cost > abs(x - tx) + abs(y - ty):
                        f = True
                        rx = tx
                        ry = ty
                        cost = abs(x - tx) + abs(y - ty)
                    break

            for i in range(loop):
                tx = x + i if frx is False else x
                ty = y + j if fry is False else y
                #print("try",tx, ty)
                if ty % tx == 0:
                    if cost > abs(x - tx) + abs(y - ty):
                        f = True
                        rx = tx
                        ry = ty
                        cost = abs(x - tx) + abs(y - ty)
                    break


        loop += 1

    return rx, ry, cost

#6 30 46
"""
8
6 24 48
"""
print(do(6 ,46))
print(do(6 ,30))
print(do(30 ,46))

print(do(24 ,45))
print(do(6 ,30))
print(do(30 ,46))

