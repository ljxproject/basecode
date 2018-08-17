# 概念:while循环用于循环执行部分语句,即在一定条件下,反复多次的执行循环体, 以处理需要反复处理的相同任务
# 格式：　
# while 条件语句:
#     循环体

# 1  2   3   4  5
'''
num = 1
i = 1  #i用来计数
while i < 6:
    print(num)
    num +=1
    i +=1


num = 1
while num < 6:
    print(num)
    num +=1


wen = "wen is a  nice man"
num = 0
while num < len(wen):
    print( "wen[%d]=%s"%(num,wen[num]))
    num += 1



#需求:  完成  求1 +2 + 3 + 4 ..... 100 的和
0

上次的和+1
上次的和+2
+3
+4
+5
+6
'''


# 和 = 上次和 + 当前的数

num = 1
count = 0
while num <= 100:
  # count += num
  count = count + num
  num += 1
print(count)


















