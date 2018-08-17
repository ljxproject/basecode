# import time
# time.clock()
# count = 0
# for i in  range(100000000):
#     count += 1
# print(count)
# print(time.clock())


import time
timeStart = time.time()
count = 0
for i in  range(100000000):
    count += 1
print(count)
endTime = time.time()
print(endTime - timeStart)

