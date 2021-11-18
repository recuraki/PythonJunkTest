n = 10
i, j, k = 3,6,8

n = 5
i, j, k = 1,3,5

n = 5
i, j, k = 2,4,5

n = 16
i, j, k = 5,10, 13

print("i,j,k,n" , i, j, k, n)
i -= 1
j -= 1
k -= 1

l = list(range(1, n+1))
#print(l)
l = l[:i] + list(reversed(l[i:j])) + l[j:]
#print(l)
l = l[:j] + list(reversed(l[j:k+1])) + l[k+1:]

print(l)

while True:
    qstr = input().split()
    if qstr[0][0] == "?":
        ll, rr = int(qstr[1]), int(qstr[2])
        ll -= 1
        rr -= 1
        ans = 0
        #print(l)
        for ii in range(ll, rr+1):
            for jj in range(ii+1, rr+1):
                if l[ii] > l[jj]: ans += 1
        print(ans)
    if qstr[0][0] == "!":
        a, b, c = map(int, qstr[1:])
        a -= 1
        b -= 1
        c -= 1
        #print(a,b,c,i,j,k)
        if a==i and b==j and c == k:
            print("OK!")
            break
        else:
            print("NOOOOOOOOOOOOOOOOOOOOOOOOO")
            break

