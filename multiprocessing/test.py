import datetime
import pandas
tmp = dict()

tmp[datetime.datetime(2021, 5, 24, 0, 0, 0)] = 10
tmp[datetime.datetime(2021, 5, 24, 0, 2, 0)] = 10
tmp[datetime.datetime(2021, 5, 24, 0, 4, 0)] = 10
tmp[datetime.datetime(2021, 5, 24, 0, 6, 0)] = 10
tmp[datetime.datetime(2021, 5, 24, 0, 8, 0)] = 10
tmp[datetime.datetime(2021, 5, 24, 0, 10, 0)] = 10

total = 0
for k in tmp.keys():
    total += tmp[k]
median = total // 2 + 1
print("total={0}, median={1}".format(total, median))
timekey = list(tmp.keys())
timekey.sort()
curtotal = 0
for key in timekey:
    curtotal += tmp[key]
    if curtotal >= median:
        print("median datetime", key)
        break
