# 10進数 -> base進数変換
#
def base10int(value, base):
    if (int(value // base)):
        return base10int(int(value // base), base) + str(value % base)
    return str(value % base)

print(base10int(100,3))# -> 10201
print(base10int(16, 4))# -> 100
print(base10int(10**18, 3))# -> 20122212221021011100201020220212020001
print(int(str(base10int(10**18, 3)), 3) == 10**18)# -> 10e18 になるのかの確認

