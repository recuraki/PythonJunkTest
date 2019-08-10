m = 2
t = ["12", "34"]
print(t)

p = []
for i in range(m):
    s = ""
    for j in range(m):
        s += t[m-j-1][i]
    p.append(s)
print(p)

p = []
for i in range(m):
    s = ""
    for j in range(m):
        s += t[m-i-1][m-j-1]
    p.append(s)
print(p)

p = []
for i in range(m):
    s = ""
    for j in range(m):
        s += t[j][m-i-1]
    p.append(s)
print(p)
