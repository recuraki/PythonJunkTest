from random import randint
import time
from copy import deepcopy
num = 5000

indatsmall = [randint(1, 10) for _ in range(num)]
indatlarge = [randint(10**9, 10**10) for _ in range(num)]

###############
start = time.time()
for loop in range(5000):
    newbuf = [0] * num
    for i in range(num):
        newbuf[i] += indatsmall[i]

elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
###############
###############
start = time.time()
for loop in range(5000):
    newbuf = [0] * num
    for i in range(num):
        newbuf[i] += indatlarge[i]

elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
###############
