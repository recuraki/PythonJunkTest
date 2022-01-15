
# https://www.interviewkickstart.com/interview-questions/google-phone-screen-interview-questions

# Write a code to find the median of two sorted arrays, ‘X’ and ‘Y,’ of sizes m and n.
def q1():
    a = [1, 5, 4, 2, 3]
    b = [1, 3, 2, 1, 3]
    a = [1,2,3,4,5]
    b = [6,7,8,9]
    # 4, 5 = 9 -> index 4
    # ()
    a.sort()
    b.sort()
    print(sorted(a+b))
    tl = len(a) + len(b)
    if tl % 2 == 0: targetind = [tl // 2 - 1, tl // 2]
    else: targetind = [tl // 2]
    i1 = i2 = 0
    curind = 0
    searchInd = 0
    choose1 = None
    ans = []
    while True:
        if searchInd >= len(targetind): break
        if i1 >= len(a): choose1 = False
        elif i2 >= len(b): choose1 = True
        else: # both ok
            if a[i1] <= b[i2]: choose1 = True
            else: choose1 = False
        if choose1:
            if curind == targetind[searchInd]:
                ans.append(a[i1])
                searchInd += 1
            i1 += 1
        else:
            if curind == targetind[searchInd]:
                ans.append(b[i2])
                searchInd += 1
            i2 += 1
        curind += 1
    print(ans)

q1()


# Find all magic triplets in a given integer array arr of size n. (A magic triplet is a group of three numbers whose sum is zero).
def q2():
