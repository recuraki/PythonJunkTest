import bisect

seq = [1,2,3,4,5,6,8]
seq = [1,2,3,4,3,4,5,6,7,8,1,2,3,9]

LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

print(len(LIS))
print(LIS)