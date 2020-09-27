def findLexSmallest( s):
    l = len(s)
    dat = []
    for n in range(300):
        a, b, c = -1, -1, -1
        for i in range(l):
            print(i, s[i])
            if a == -1:
                if s[i] == ")":
                    print("seta")
                    a = i
            if a != -1 and b == -1:
                if s[i] == "(":
                    print("setb")
                    b = i - 1
            if b != -1 and c == -1:
                if s[i] == ")":
                    print("setc")
                    c = i - 1
                elif i ==l-1 and s[i] == "(":
                    print("setc")
                    c = i
        if c == -1:
            break
        print(a, b, c)
        dat.append(a)
        dat.append(b)
        dat.append(c)
        print(a, b, c)
        print("b", s)
        s = s[:a] + s[b + 1:c + 1] + s[a:b + 1] + s[c + 1:]
        print("a", s)

    return (tuple(dat))


print(findLexSmallest("))(("))