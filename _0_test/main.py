a = 954

# get 1000 = 1

# get 100(2)
num = [0] * 10
num[0] = 1
print(num)

# get 10(3)
num = [0] * 10
num[0] = 2
print(num)

# get 1(4)
num = [0] * 10
num[0] = 3
print(num)

# 100 no kurai(5)
val = a // 100
num = [0] * 10
for i in range(val):
    num[i] = 1
print(num)

# 10 no kurai(6)
val = (a % 100) // 10
num = [0] * 10
for i in range(val):
    num[i] = 2
print(num)

# get 1(7)
val = (a%10) // 1
num = [0] * 10
for i in range(val):
    num[i] = 3
print(num)

# merge
num = [-1] * 10
num =
