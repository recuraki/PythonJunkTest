def do(x, y):
    a1 = y // x
    a2 = a1 + 1
    print("a1,a2",a1,a2)
    if abs (y - x*a1) <= abs(x*a2 - y):
        ny = x * a1
    else:
        ny = x * a2
    cost = abs(y - ny)
    return x, ny, cost

print(do(3,10))
print(do(123 ,321 ))
print(do(369,456))
print(do(321 ,456))
print(do(123  ,456))
print(do(321,492))

