import queue
import heapq

import time
import random
from copy import deepcopy
n = 2 * 10**5

inqueue = [random.randint(0, 10**9) for _ in range(n)]
inheapq = deepcopy(inqueue)

data = [random.randint(0, 10**9) for _ in range(n)]

resqueue = []
resheapq = []

print("--- Heapq, poppush")
start = time.time()
heapq.heapify(inheapq)
for i in range(n):
    x = heapq.heappushpop(inheapq, data[i])
    resheapq.append(x)
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

print("--- Heapq, pop then push")
start = time.time()
heapq.heapify(inheapq)
for i in range(n):
    x = heapq.heappop(inheapq)
    resheapq.append(x)
    heapq.heappush(inheapq, data[i])
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

print("--- Queue")
print("    Step1: create init queue")
start = time.time()
q = queue.PriorityQueue(n)
start = time.time()
for i in range(n):
    q.put(inqueue[i])
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
print("    Step2: pop then push")
start2 = time.time()
for i in range(n):
    x = q.get()
    resqueue.append(x)
    q.put(data[i])
elapsed_time = time.time() - start2
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
