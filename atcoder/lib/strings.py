# sec 15.4
from pprint import pprint
dna1="ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
dna2="GTCGTTCGGAATGCCGTTGCTCTGTAAA"
dna3="GTCGTCGGAAGCCGGCCGAA"

# >>> [chr(i) for i in range(0x61,0x61+26)]
list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

str_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_lower = 'abcdefghijklmnopqrstuvwxyz'
str_digit = "0123456789"

def lcs_length(x, y):
    m,n  = len(x), len(y)
    b = [[0 for i in range(n+1)] for j in range(m+1)]
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '\\'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "|"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "-"
    return c,b

def lcs_print(b, X, i, j):
    #print("i{0}, j{1}".format(i,j))
    if i == 0 or j == 0:
        return
    if b[i][j] == '\\':
        lcs_print(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j] == "|":
        lcs_print(b, X, i - 1, j)
    else:
        lcs_print(b,X,i, j-1)


import itertools
def countstrs(s):
    return [(k, len(list(g))) for k, g in itertools.groupby(s)]

"""
>>> countstrs("1110000111")->    [('1', 3), ('0', 4), ('1', 3)]
>>> countstrs("") ->    []
>>> countstrs("aaa") ->    [('a', 3)]
"""

from pprint import pprint
str1 = "ABCBDAB"
str2 = "BDCABA"
c, b = lcs_length(str1, str2)
#pprint(c)
#pprint(b)
lcs_print(b, str1, len(str1) - 1, len(str2) - 1 )


str1 = "aabce"
str2 = "ac"
c, b = lcs_length(str1, str2)
#pprint(c)
#pprint(b)
lcs_print(b, str1, len(str1) - 1, len(str2) - 1 )


